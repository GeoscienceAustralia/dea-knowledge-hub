import os
import numpy as np
import matplotlib.pyplot as plt


def band_plot(ls_finner_df, ls_fstat_WSdf, s2_finner_df, PlatNamesSpace, formDate, field_data):

    if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
        #
        # Plot single day sat/field comparison for dual overpass
        #
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10.5, 5.5))
    
        plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)
    
        if 'Landsat' in field_data[3]:
            fid = ls_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                                columns={'Field_inner_mean': 'Field'})
            fsd = ls_fstat_WSdf.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                            columns={'Sat_mean': field_data[3]})
            fsd.plot(y=field_data[3], ax=axes[0], color='red', linewidth=0.7)
            axes[0].errorbar(x=fsd.index, y=fsd[field_data[3]], yerr=fsd['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
            fid2 = s2_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7',
                                    'Band8': '8', 'Band8a': '8a', 'Band11': '11', 'Band12': '12'},
                            columns={'Field_inner_mean': 'Field', 'Sat_inner_mean': PlatNamesSpace[field_data[6]]})
            fid2.plot(y=PlatNamesSpace[field_data[6]], ax=axes[1], color='blue', linewidth=0.7)
            axes[1].errorbar(x=fid2.index, y=fid2[PlatNamesSpace[field_data[6]]], yerr=fid2['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
    
        elif 'Sentinel' in field_data[3]:
            fid = s2_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7',
                                    'Band8': '8', 'Band8a': '8a', 'Band11': '11', 'Band12': '12'},
                            columns={'Field_inner_mean': 'Field', 'Sat_inner_mean': PlatNamesSpace[field_data[3]]})
            fid.plot(y=PlatNamesSpace[field_data[3]], ax=axes[0], color='blue', linewidth=0.7)
            axes[0].errorbar(x=fid.index, y=fid[PlatNamesSpace[field_data[3]]], yerr=fid['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
            fid2 = ls_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                                columns={'Field_inner_mean': 'Field'})
            fsd2 = ls_fstat_WSdf.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                            columns={'Sat_mean': afield_data[6]})
            fsd2.plot(y=PlatNamesSpace[field_data[6]], ax=axes[1], color='blue', linewidth=0.7)
            axes[1].errorbar(x=fsd2.index, y=fsd2[PlatNamesSpace[field_data[6]]], yerr=fsd2['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
        else:
            print('Satellite name should be one of Landsat8/9 or Sentinel2a/b. I got', afield_data[3])
    
        fid.plot(y='Field', ax=axes[0], color='red', linewidth=0.7)
        fid2.plot(y='Field', ax=axes[1], color='red', linewidth=0.7)
        axes[0].errorbar(x=fid.index, y=fid['Field'], yerr=fid['Field_SD'], color='red', capsize=3, linewidth=0.7)
        axes[1].errorbar(x=fid2.index, y=fid2['Field'], yerr=fid2['Field_SD'], color='red', capsize=3, linewidth=0.7)
    
        axes[0].set_xlabel('Band Number')
        axes[1].set_xlabel('Band Number')
        axes[0].set_ylabel('Surface Reflectance')
        axes[0].legend([PlatNamesSpace[field_data[3]], 'Field'], prop={'size': 9})
        axes[1].legend([PlatNamesSpace[field_data[6]], 'Field'], prop={'size': 9})
    
        bandPlot = '../../../site-report/'+formDate+'-'+field_data[0]+'/SiteComparison-'+formDate+'-'+field_data[0]+'.png'
        if not os.path.exists(bandPlot):
            plt.savefig(bandPlot, dpi=300)
            print('New Figure Saved')
            
    else:
        #
        # Plot single day sat/field comparison for single overpass
        #
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5.5, 5.5))
    
        plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)
    
        if 'Landsat' in field_data[3]:
            #axes.set_xticklabels(['1','2','3','4','5','6', '7'])
            fid = ls_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                                columns={'Field_inner_mean': 'Field'})
            fsd = ls_fstat_WSdf.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7'},
                            columns={'Sat_mean': field_data[3]})
            fsd.plot(y=field_data[3], ax=axes, color='blue', linewidth=0.7)
            plt.errorbar(x=fsd.index, y=fsd[field_data[3]], yerr=fsd['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
    
        elif 'Sentinel' in field_data[3]:
            fid = s2_finner_df.rename(index={'Band1': '1', 'Band2': '2', 'Band3': '3', 'Band4': '4', 'Band5': '5', 'Band6': '6', 'Band7': '7',
                                    'Band8': '8', 'Band8a': '8a', 'Band11': '11', 'Band12': '12'},
                            columns={'Field_inner_mean': 'Field', 'Sat_inner_mean': PlatNamesSpace[field_data[3]]})
            fid.plot(y=PlatNamesSpace[field_data[3]], ax=axes, color='blue', linewidth=0.7)
            plt.errorbar(x=fid.index, y=fid[PlatNamesSpace[field_data[3]]], yerr=fid['Sat_SD'], color='blue', capsize=3, linewidth=0.7)
    
        else:
            print('Satellite name should be one of Landsat8/9 or Sentinel2a/b. I got', afield_data[3])
    
        fid.plot(y='Field', ax=axes, color='red', linewidth=0.7)
        plt.errorbar(x=fid.index, y=fid['Field'], yerr=fid['Field_SD'], color='red', capsize=3, linewidth=0.7)
    
        axes.set_xlabel('Band Number')
        axes.set_ylabel('Surface Reflectance')
        axes.legend([PlatNamesSpace[field_data[3]], 'Field'], prop={'size': 9})
    
        bandPlot = '../../../site-report/'+formDate+'-'+field_data[0]+'/SiteComparison-'+formDate+'-'+field_data[0]+'.png'
        if not os.path.exists(bandPlot):
            plt.savefig(bandPlot, dpi=300)
            print('New Figure Saved')
    
