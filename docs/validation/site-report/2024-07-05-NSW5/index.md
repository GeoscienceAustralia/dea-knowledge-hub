
    # 2024-07-05-NSW5: Transect NSW Site 5, Landsat 9 overpass
    
    A Site Validation Summary Report of the surface reflectance data collected on the date of 2024-07-05-NSW5 by Geoscience&nbsp;Australia.
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
    "Time of field site measurements (UTC)","2024-07-05 00:11:30 to 2024-07-05 00:56:23"
    "Time of overpass (UTC)", 2024-07-04 23:55:21
    "GPS quality","Good"
    "Reference position","148.21042853E, 32.20982427S (WGS84)"
    "Matchup quality","Excellent"
    :::
    
    ## Results
    
    The surface reflectance statistics collected on this day are grouped into bands.
    This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.
    
    ```{eval-rst}
    .. container:: validation-report-download
    
       :download:`Download as CSV <./SiteValidationResults-2024-07-05-NSW5.csv>`
    ```
    
    :::{csv-table} Results of Field data versus Landsat 9 Satellite
    :class: validation-report-results-table
    
    "Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.04","0.001","0.045","0.005"
"blue","0.052","0.001","0.055","0.007"
"green","0.084","0.002","0.087","0.008"
"red","0.098","0.003","0.097","0.013"
"NIR","0.247","0.017","0.25","0.028"
"SWIR1","0.269","0.006","0.279","0.026"
"SWIR2","0.171","0.005","0.179","0.021"
"CA","0.019","0.004","0.033","0.007"
"blue","0.022","0.004","0.037","0.009"
"green","0.046","0.01","0.068","0.016"
"red","0.039","0.01","0.054","0.025"
"NIR","0.304","0.137","0.42","0.191"
"SWIR1","0.14","0.021","0.189","0.053"
"SWIR2","0.073","0.018","0.098","0.05"
    :::
    
    ## Figures
    
    Click an image to view it at full size.
    
    :::::{grid} 1 1 2 3
    ::::{grid-item}
    :::{figure} ./RGB-2024-07-05-NSW5.png
    
    A satellite imagery tile of true colour (RGB) surface reflectance.
    It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
    The white box indicates the size and location
    of the field site.
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./SiteComparison-2024-07-05-NSW5.png
    
    A band-by-band plot of surface reflectance for satellite and field data.
    Satellite uncertainty error bars for each band are the standard deviation
    of pixel values over and surrounding the field site.
    Field uncertainty error bars are the standard deviation of values after
    averaging all spectra within the same satellite pixels.
    
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./OverallComparison-2024-07-05-NSW5.png
    
    A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
    The solid line represents the one-to-one equality between field and satellite measurements.
    The black dots are the values from all field site measurements prior to this date.
    The line of best fit is not shown, but its parameters are given in the bottom-right corner.
    
    :::
    ::::
    :::::
    
    % :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
    % :::
    