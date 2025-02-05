import shutil
import pandas as pd
import numpy as np
from datetime import datetime as dt


def addSite2(ls_fstat_WSdf, all_data, field_data, PlatNames):

    date_obj = dt.strptime(field_data[1], '%d%b%y')
    timestamp = pd.Timestamp(date_obj)
    Platf = PlatNames[field_data[3]]

    if all_data[(all_data.Site==field_data[0]) & (all_data.Date==timestamp) & (all_data.Platform==Platf)].empty:
        if 'L' in PlatNames[field_data[3]]:
            bands = ['CA', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2']
        else:
            bands = ['CA', 'blue', 'green', 'red', 'RE1', 'RE2', 'RE3', 'nir_1', 'nir_2', 'swir_2', 'swir_3']

        newdf = ls_fstat_WSdf[['Sat_mean', 'Sat_SD', 'Field_mean', 'Field_SD']]
        newdf.index=bands
        newdf.columns=['satmean', 'satstd', 'fieldmean', 'fieldstd']
        newdf['BAND']=bands
        newdf['Platform']=Platf
        newdf['Date']=timestamp
        newdf['Date'] = newdf['Date'].dt.strftime('%d%b%y').str.upper()
        newdf['Site']=field_data[0]
        all_data['Date'] = all_data['Date'].dt.strftime('%d%b%y').str.upper()

        combined_df = pd.concat([all_data, newdf])
        all_data = combined_df.reset_index(drop=True)
        all_data = all_data.round(3)

        shutil.copy('/gdata1/projects/CalVal/Phase1/MISC/COMBINE-SITES/ALL.txt', '/gdata1/projects/CalVal/Phase1/MISC/COMBINE-SITES/ALL.'+field_data[1])
        all_data.to_csv('/gdata1/projects/CalVal/Phase1/MISC/COMBINE-SITES/ALL.txt', index=False)

        all_data.Date = [dt.strptime(x, '%d%b%y') for x in all_data.Date]

    return all_data

def addSite(ls_fstat_WSdf, s2_fstat_df, PlatNames, field_data):

    #
    # Reformat date strings to datetime objects
    #
    all_data = pd.read_csv('/gdata1/projects/CalVal/Phase1/MISC/COMBINE-SITES/ALL.txt')
    all_data.Date = [dt.strptime(x, '%d%b%y') for x in all_data.Date]
    
    #
    # Reformat field_data[0] date string to datetime object
    #
    today_date = dt.strptime(field_data[1], '%d%b%y')
    
    if 'Landsat' in field_data[3]:
        all_data = addSite2(ls_fstat_WSdf, all_data, field_data, PlatNames)
        if field_data[6] != '':
            dual_data = field_data.copy()
            dual_data[3] = dual_data[6]
            all_data = addSite2(s2_fstat_df, all_data, dual_data, PlatNames)
    else:
        all_data = addSite2(s2_fstat_df, all_data, field_data, PlatNames)
        if field_data[6] != '':
            dual_data = field_data.copy()
            dual_data[3] = dual_data[6]
            all_data = addSite2(ls_fstat_WSdf, all_data, dual_data, PlatNames)
    
    #
    # Break DataFrame into parts for today and previously.
    # Ensure we only keep data relevant to the platform that overpassed.
    #
    
    if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
        prev_data1 = all_data[np.logical_and(all_data.Date < today_date, all_data.Platform == PlatNames[field_data[3]])]
        today_data1 = all_data[np.logical_and(all_data.Date == today_date, all_data.Platform == PlatNames[field_data[3]])]
        prev_today_data1 = all_data[np.logical_and(all_data.Date <= today_date, all_data.Platform == PlatNames[field_data[3]])]
        prev_data2 = all_data[np.logical_and(all_data.Date < today_date, all_data.Platform == PlatNames[field_data[6]])]
        today_data2 = all_data[np.logical_and(all_data.Date == today_date, all_data.Platform == PlatNames[field_data[6]])]
        prev_today_data2 = all_data[np.logical_and(all_data.Date <= today_date, all_data.Platform == PlatNames[field_data[6]])]

        return prev_data1, today_data1, prev_today_data1, prev_data2, today_data2, prev_today_data2
    
    else:
        prev_data = all_data[np.logical_and(all_data.Date < today_date, all_data.Platform == PlatNames[field_data[3]])]
        today_data = all_data[np.logical_and(all_data.Date == today_date, all_data.Platform == PlatNames[field_data[3]])]
        prev_today_data = all_data[np.logical_and(all_data.Date <= today_date, all_data.Platform == PlatNames[field_data[3]])]

        return prev_data, today_data, prev_today_data
