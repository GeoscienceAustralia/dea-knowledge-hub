
    # 2023-09-22-MUL: Mullion, Landsat 8 overpass
    
    A Site Validation Summary Report of the surface reflectance data collected on the date of 2023-09-22-MUL by Geoscience&nbsp;Australia.
    The full collection of data is contained in the [National Spectral Database](https://www.dea.ga.gov.au/products/national-spectral-database).
    Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/).
    
    :::{contents} In this report
    :local:
    :backlinks: none
    :::
    
    ## Variables
    
    These variables and environmental factors were present on the day the data were collected.
    
    :::{csv-table}
    :class: validation-report-variables-table
    
    "Instrument(s) used","ASD FR4 (18179/3)"
    "Time of field site measurements (UTC)","2023-09-21 23:55:28 to 2023-09-22 00:29:26"
    "Time of overpass (UTC)", 2023-09-21 23:50:45
    "GPS quality","Good"
    "Reference position","148.86259775E, 35.12273865S (WGS84)"
    "Matchup quality","Excellent"
    :::
    
    ## Results
    
    The surface reflectance statistics collected on this day are grouped into bands.
    This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.
    
    ```{eval-rst}
    .. container:: validation-report-download
    
       :download:`Download as CSV <./SiteValidationResults-2023-09-22-MUL.csv>`
    ```
    
    :::{csv-table} Results of Field data versus Landsat 8 Satellite
    :class: validation-report-results-table
    
    "Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.037","0.001","0.036","0.007"
"blue","0.043","0.002","0.043","0.009"
"green","0.074","0.002","0.077","0.013"
"red","0.065","0.004","0.068","0.017"
"NIR","0.373","0.022","0.39","0.058"
"SWIR1","0.234","0.008","0.251","0.038"
"SWIR2","0.118","0.004","0.128","0.024"
    :::
    
    ## Figures
    
    Click an image to view it at full size.
    
    :::::{grid} 1 1 2 3
    ::::{grid-item}
    :::{figure} ./RGB-2023-09-22-MUL.png
    
    A satellite imagery tile of true colour (RGB) surface reflectance.
    It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
    The white box indicates the size and location
    of the field site.
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./SiteComparison-2023-09-22-MUL.png
    
    A band-by-band plot of surface reflectance for satellite and field data.
    Satellite uncertainty error bars for each band are the standard deviation
    of pixel values over and surrounding the field site.
    Field uncertainty error bars are the standard deviation of values after
    averaging all spectra within the same satellite pixels.
    
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./OverallComparison-2023-09-22-MUL.png
    
    A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
    The solid line represents the one-to-one equality between field and satellite measurements.
    The black dots are the values from all field site measurements prior to this date.
    The line of best fit is not shown, but its parameters are given in the bottom-right corner.
    
    :::
    ::::
    :::::
    
    % :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
    % :::
    