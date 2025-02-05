import os
import numpy as np
from datetime import datetime


def reformDate(field_data):
    
    # Parse the string into a datetime object
    date_obj = datetime.strptime(field_data[1], '%d%b%y')
    
    # Get the day with a suffix (st, nd, rd, th)
    day = int(date_obj.strftime('%d'))
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    
    # Format the final string
    #formatted_date = date_obj.strftime(f"{day}{suffix} of %B, %Y")
    formatted_date = date_obj.strftime(f"{day} %B %Y")
    
    return formatted_date


def overlapBands(ls_fstat_WSdf):
    # Determine the lower and upper bounds for Sat_mean and Field_mean considering the errors
    ls_fstat_WSdf['Sat_lower'] = ls_fstat_WSdf['Sat_mean'] - ls_fstat_WSdf['Sat_SD']
    ls_fstat_WSdf['Sat_upper'] = ls_fstat_WSdf['Sat_mean'] + ls_fstat_WSdf['Sat_SD']
    ls_fstat_WSdf['Field_lower'] = ls_fstat_WSdf['Field_mean'] - ls_fstat_WSdf['Field_SD']
    ls_fstat_WSdf['Field_upper'] = ls_fstat_WSdf['Field_mean'] + ls_fstat_WSdf['Field_SD']

    # Determine if there's any overlap between Sat_mean and Field_mean errors
    ls_fstat_WSdf['Overlap'] = (ls_fstat_WSdf['Sat_lower'] <= ls_fstat_WSdf['Field_upper']) & \
                                (ls_fstat_WSdf['Sat_upper'] >= ls_fstat_WSdf['Field_lower'])

    # Count the number of bands with overlapping errors
    num_bands_with_overlap = ls_fstat_WSdf['Overlap'].sum()

    return num_bands_with_overlap


def create_markdown(today_data, today_data1, today_data2, allASDdata, allSR3500data, PlatNamesSpace, FieldNames, ls_sat_array, s2_sat_array,
                    ls_fstat_WSdf, s2_fstat_df, formDate, Corners, field_data):
    
    #
    # Edit band names for output
    #
    mapping = {
        'nir': 'NIR',
        'nir_1': 'NIR1',
        'nir_2': 'NIR2',
        'swir1': 'SWIR1',
        'swir2': 'SWIR2',
        'swir_2': 'SWIR2',
        'swir_3': 'SWIR3'
    }
    
    # Replace elements in the "BAND" column using the mapping
    if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
        today_data1['BAND'] = today_data1['BAND'].replace(mapping)
        today_data2['BAND'] = today_data2['BAND'].replace(mapping)
    else:
        today_data['BAND'] = today_data['BAND'].replace(mapping)
    
    
    
    if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
        markdownData = [
            "\"Band\",\"Sat Mean\",\"Sat rms\",\"Field mean\",\"Field rms\""
        ]
    
        # Append rows from DataFrame to data
        for _, row in today_data1.iterrows():
            # Capitalize certain strings
            band = row['BAND']
            if band == "Ca":
                band = "CA"
            elif band == "Swir1":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR1</a>"
            elif band == "Swir2":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR2</a>"
            elif band == "Swir3":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR3</a>"
            elif band == "Nir":
                band = "<a href='/guides/about/glossary/#nir' target='_blank'>NIR</a>"
    
            # Append formatted row to data
            markdownData.append(
                "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format(
                    band,
                    str(row['satmean']),
                    str(row['satstd']),
                    str(row['fieldmean']),
                    str(row['fieldstd'])
                )
            )
    
        # Append empty line
        markdownData.append(
            ":::\n\n:::{csv-table} Results of Field data versus PaNaSp2 Satellite\n:class: validation-report-results-table\n"
        )
    
        # Append column headers line
        markdownData.append("\"Band\",\"Sat Mean\",\"Sat rms\",\"Field mean\",\"Field rms\"")
    
    
        # Append rows from DataFrame to data
        for _, row in today_data2.iterrows():
            # Capitalize certain strings
            band = row['BAND']
            if band == "Ca":
                band = "CA"
            elif band == "Swir1":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR1</a>"
            elif band == "Swir2":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR2</a>"
            elif band == "Swir3":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR3</a>"
            elif band == "Nir":
                band = "<a href='/guides/about/glossary/#nir' target='_blank'>NIR</a>"
    
            # Append formatted row to data
            markdownData.append(
                "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format(
                    band,
                    str(row['satmean']),
                    str(row['satstd']),
                    str(row['fieldmean']),
                    str(row['fieldstd'])
                )
            )
    
    else:
    
        markdownData = [
            "\"Band\",\"Sat Mean\",\"Sat rms\",\"Field mean\",\"Field rms\""
        ]
    
        # Append rows from DataFrame to data
        for _, row in today_data.iterrows():
            # Capitalize certain strings
            band = row['BAND']
            if band == "Ca":
                band = "CA"
            elif band == "Swir1":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR1</a>"
            elif band == "Swir2":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR2</a>"
            elif band == "Swir3":
                band = "<a href='/guides/about/glossary/#swir' target='_blank'>SWIR3</a>"
            elif band == "Nir":
                band = "<a href='/guides/about/glossary/#nir' target='_blank'>NIR</a>"
    
            # Append formatted row to data
            markdownData.append(
                "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format(
                    band,
                    str(row['satmean']),
                    str(row['satstd']),
                    str(row['fieldmean']),
                    str(row['fieldstd'])
                )
            )
    
    # Convert data to Markdown table
    markdown_table = "\n".join(markdownData)
    
    
    
    
    # Define your content with a placeholder for dynamic values
    content_template = """# FieldDay: SiteName, PNS overpass

This is a report of the field data collected on FieldTxtDay at the location of SiteName
to validate the satellite data of the PNS overpass.
The full collection of data is contained in the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/#share=s-i2o7JwB5gvXOQefhMmTLJaA14b0).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (instNum)"
"Time of field site measurements (UTC)","startDateTime to endDateTime"
"Time of overpass (UTC)", overpassDateTime
"GPS quality","GPSQual"
"Reference position","firstLonE, firstLatS (WGS84)"
"Matchup quality","MatchQual"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-FieldDay.csv>`
```

:::{csv-table} TableTitle
:class: validation-report-results-table

MarkDownTable
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-FieldDay.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-FieldDay.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-FieldDay.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    """
    
    
    # Replace the placeholder with the dynamic value
    #content_template = content_template.replace("{current_datetime_placeholder}", current_datetime)
    try:
        content_template = content_template.replace("instNum", allASDdata.Inst_number.iloc[0])
    except (NameError, AttributeError):
        content_template = content_template.replace("ASD FR4 (instNum)", "SR-3500_20680T1")
        allASDdata = allSR3500data.copy()
    
    content_template = content_template.replace("startDateTime", str(allASDdata.date_saved.min()))
    content_template = content_template.replace("endDateTime", str(allASDdata.date_saved.max()))
    content_template = content_template.replace("firstLat", str(round(abs(allASDdata.Latitude.iloc[0]),8)))
    content_template = content_template.replace("firstLon", str(round(allASDdata.Longitude.iloc[0],8)))
    
    content_template = content_template.replace("TableTitle", "Results of Field data versus " + PlatNamesSpace[field_data[3]] + " Satellite")
    
    content_template = content_template.replace("MarkDownTable", markdown_table)
    
    content_template = content_template.replace("FieldTxtDay", reformDate(field_data))
    content_template = content_template.replace("FieldDay", formDate+'-'+field_data[0])
    
    if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
        content_template = content_template.replace("PNS", PlatNamesSpace[field_data[3]]+" and "+PlatNamesSpace[field_data[6]]+" dual")
        content_template = content_template.replace("PaNaSp2", PlatNamesSpace[field_data[6]])
        content_template = content_template.replace("A satellite imagery tile", "Satellite imagery tiles")
        content_template = content_template.replace("It covers an area", "They each cover an area")
        content_template = content_template.replace("the white box indicates", "the white box in each indicates")
        content_template = content_template.replace("A band-by-band plot of surface reflectance for satellite and field data", "Band-by-band plots of surface reflectance for field data versus each satellite")
        content_template = content_template.replace("A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day", "Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day")
    else:
        content_template = content_template.replace("PNS", PlatNamesSpace[field_data[3]])
    
    content_template = content_template.replace("SiteName", FieldNames[field_data[0]])
    
    #
    # Following logic is to define matchup quality, depending on whether we have single or dual overpasses and which satellite
    # is listed first for dual overpass.
    #
    
    # If first overpass is a Landsat
    if field_data[3] == 'Landsat8' or field_data[3] == 'Landsat9':
        # If dual overpass, where second listed is a Sentinel
        if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
            replStr1 = "Time of " + PlatNamesSpace[field_data[3]] + " overpass (UTC)"
            replStr2 = ", " + np.datetime_as_string(ls_sat_array.time.values[0], unit='s').replace('T', ' ') + '\n"Time of ' + \
                       PlatNamesSpace[field_data[6]] +' overpass (UTC)"' + ", " + np.datetime_as_string(s2_sat_array.time.values[0], unit='s').replace('T', ' ')
            content_template = content_template.replace("Time of overpass (UTC)", replStr1)
            content_template = content_template.replace(", overpassDateTime", replStr2)
        else:
            # If only single Landsat overpass
            content_template = content_template.replace("overpassDateTime", np.datetime_as_string(ls_sat_array.time.values[0], unit='s').replace('T', ' '))
    
        # If dual overpass with Sentinel listed 2nd
        if 'Sentinel' in field_data[6]:
            # qual2 is for Sentinel
            if overlapBands(s2_fstat_df) == 11:
                qual2 = "Excellent"
            elif overlapBands(s2_fstat_df) > 8:
                qual2 = "Good"
            else:
                qual2 = "Poor"
            # qual1 is for Landsat (listed first)
            if overlapBands(ls_fstat_WSdf) == 7:
                qual1 = "Excellent"
            elif overlapBands(ls_fstat_WSdf) > 4:
                qual1 = "Good"
            else:
                qual1 = "Poor"
            content_template = content_template.replace('"Matchup quality","MatchQual"', '"Matchup quality for ' + PlatNamesSpace[field_data[3]] + '","' + qual1 + \
                                                        '"\n"Matchup quality for ' + PlatNamesSpace[field_data[6]] + '","' + qual2 +'"')
            #content_template = content_template.replace("MatchQual", qual1 + " for " + field_data[3] + ", " + qual2 + " for " + field_data[6])
        else:
            # If there is only a single overpass
            if overlapBands(ls_fstat_WSdf) == 7:
                content_template = content_template.replace("MatchQual","Excellent")
            elif overlapBands(ls_fstat_WSdf) > 4:
                content_template = content_template.replace("MatchQual","Good")
            else:
                content_template = content_template.replace("MatchQual","Poor")
    
    # If Sentinel overpass listed first
    else:
        # If dual overpass with Landsat listed 2nd
        if 'Landsat' in field_data[6]:
            replStr1 = "Time of " + PlatNamesSpace[field_data[3]] + " overpass (UTC)"
            content_template = content_template.replace("Time of overpass (UTC)", replStr1)
            content_template = content_template.replace(", overpassDateTime", replStr2)
        else:
            content_template = content_template.replace("overpassDateTime", np.datetime_as_string(s2_sat_array.time.values[0], unit='s').replace('T', ' '))
    
        # Define matchup quality first for Sentinel as qual1 and then Landsat as qual2
        if 'Landsat' in field_data[6]:
            if overlapBands(s2_fstat_df) == 11:
                qual1 = "Excellent"
            elif overlapBands(s2_fstat_df) > 8:
                qual1 = "Good"
            else:
                qual1 = "Poor"
            if overlapBands(ls_fstat_WSdf) == 7:
                qual2 = "Excellent"
            elif overlapBands(ls_fstat_WSdf) > 4:
                qual2 = "Good"
            else:
                qual2 = "Poor"
            content_template = content_template.replace("MatchQual", qual1 + " for " + field_data[3] + ", " + qual2 + " for " + field_data[6])
    
        # If only single Sentinel overpass
        else:
            if overlapBands(s2_fstat_df) == 11:
                content_template = content_template.replace("MatchQual","Excellent")
            elif overlapBands(s2_fstat_df) > 8:
                content_template = content_template.replace("MatchQual","Good")
            else:
                content_template = content_template.replace("MatchQual","Poor")
    
    # Define GPS quality
    if all(element == 0 for element in Corners):
        content_template = content_template.replace("GPSQual", 'Good')
    else:
        content_template = content_template.replace("GPSQual", 'Bad')
    
    indexMD = '../../../site-report/'+formDate+'-'+field_data[0]+'/index.md'
    if not os.path.exists(indexMD):
        with open(indexMD, 'w') as file:
            file.write(content_template)
        print('New index.md file created')
