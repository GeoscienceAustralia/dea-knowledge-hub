
    # 2024-06-30-SA1: Transect South Australia Site 1, Landsat 8 overpass
    
    A Site Validation Summary Report of the surface reflectance data collected on the date of 2024-06-30-SA1 by Geoscience&nbsp;Australia.
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
    
    "Instrument(s) used","SR-3500_20680T1"
    "Time of field site measurements (UTC)","2024-06-30 00:16:43 to 2024-06-30 00:43:32"
    "Time of overpass (UTC)", 2024-06-30 00:25:52
    "GPS quality","Good"
    "Reference position","140.64083333E, 32.17500667S (WGS84)"
    "Matchup quality","Excellent"
    :::
    
    ## Results
    
    The surface reflectance statistics collected on this day are grouped into bands.
    This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.
    
    ```{eval-rst}
    .. container:: validation-report-download
    
       :download:`Download as CSV <./SiteValidationResults-2024-06-30-SA1.csv>`
    ```
    
    :::{csv-table} Results of Field data versus Landsat 8 Satellite
    :class: validation-report-results-table
    
    "Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.04","0.002","0.042","0.005"
"blue","0.051","0.002","0.05","0.006"
"green","0.087","0.003","0.087","0.017"
"red","0.143","0.007","0.141","0.04"
"NIR","0.206","0.009","0.2","0.044"
"SWIR1","0.258","0.012","0.26","0.042"
"SWIR2","0.199","0.009","0.206","0.038"
"CA","0.04","0.002","0.042","0.005"
"blue","0.051","0.002","0.05","0.006"
"green","0.087","0.003","0.087","0.017"
"red","0.143","0.007","0.141","0.04"
"NIR","0.206","0.009","0.2","0.044"
"SWIR1","0.258","0.012","0.26","0.042"
"SWIR2","0.199","0.009","0.206","0.038"
    :::
    
    ## Figures
    
    Click an image to view it at full size.
    
    :::::{grid} 1 1 2 3
    ::::{grid-item}
    :::{figure} ./RGB-2024-06-30-SA1.png
    
    A satellite imagery tile of true colour (RGB) surface reflectance.
    It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
    The white box indicates the size and location
    of the field site.
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./SiteComparison-2024-06-30-SA1.png
    
    A band-by-band plot of surface reflectance for satellite and field data.
    Satellite uncertainty error bars for each band are the standard deviation
    of pixel values over and surrounding the field site.
    Field uncertainty error bars are the standard deviation of values after
    averaging all spectra within the same satellite pixels.
    
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./OverallComparison-2024-06-30-SA1.png
    
    A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
    The solid line represents the one-to-one equality between field and satellite measurements.
    The black dots are the values from all field site measurements prior to this date.
    The line of best fit is not shown, but its parameters are given in the bottom-right corner.
    
    :::
    ::::
    :::::
    
    % :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
    % :::
    