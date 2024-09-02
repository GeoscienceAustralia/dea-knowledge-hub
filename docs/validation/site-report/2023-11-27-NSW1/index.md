
    # 2023-11-27-NSW1: Transect NSW Site 1, Landsat 9 and Sentinel-2B dual overpass
    
    A Site Validation Summary Report of the surface reflectance data collected on the date of 2023-11-27-NSW1 by Geoscience&nbsp;Australia.
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
    "Time of field site measurements (UTC)","2023-11-26 22:37:46 to 2023-11-26 23:37:06"
    "Time of Landsat 9 overpass (UTC)", 2023-11-27 00:26:53
"Time of Sentinel-2B overpass (UTC)", 2023-12-07 00:45:52
    "GPS quality","Good"
    "Reference position","142.1036962E, 31.8135401S (WGS84)"
    "Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2B","Good"
    :::
    
    ## Results
    
    The surface reflectance statistics collected on this day are grouped into bands.
    This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.
    
    ```{eval-rst}
    .. container:: validation-report-download
    
       :download:`Download as CSV <./SiteValidationResults-2023-11-27-NSW1.csv>`
    ```
    
    :::{csv-table} Results of Field data versus Landsat 9 Satellite
    :class: validation-report-results-table
    
    "Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.072","0.01","0.048","0.003"
"blue","0.082","0.009","0.06","0.004"
"green","0.122","0.007","0.105","0.011"
"red","0.197","0.011","0.18","0.028"
"NIR","0.27","0.011","0.248","0.03"
"SWIR1","0.407","0.011","0.389","0.038"
"SWIR2","0.321","0.012","0.314","0.039"
:::

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./SiteValidationResults-2023-11-27-NSW1.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.055","0.0","0.049","0.003"
"blue","0.066","0.001","0.064","0.004"
"green","0.102","0.005","0.104","0.01"
"red","0.185","0.014","0.188","0.028"
"RE1","0.208","0.014","0.209","0.031"
"RE2","0.224","0.015","0.225","0.033"
"RE3","0.234","0.015","0.237","0.033"
"NIR1","0.244","0.015","0.246","0.031"
"NIR2","0.25","0.012","0.251","0.03"
"SWIR2","0.387","0.011","0.395","0.038"
"SWIR3","0.307","0.012","0.322","0.039"
    :::
    
    ## Figures
    
    Click an image to view it at full size.
    
    :::::{grid} 1 1 2 3
    ::::{grid-item}
    :::{figure} ./RGB-2023-11-27-NSW1.png
    
    Satellite imagery tiles of true colour (RGB) surface reflectance.
    They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
    The white box indicates the size and location
    of the field site.
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./SiteComparison-2023-11-27-NSW1.png
    
    Band-by-band plots of surface reflectance for field data versus each satellite.
    Satellite uncertainty error bars for each band are the standard deviation
    of pixel values over and surrounding the field site.
    Field uncertainty error bars are the standard deviation of values after
    averaging all spectra within the same satellite pixels.
    
    :::
    ::::
    ::::{grid-item}
    :::{figure} ./OverallComparison-2023-11-27-NSW1.png
    
    Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
    The solid line represents the one-to-one equality between field and satellite measurements.
    The black dots are the values from all field site measurements prior to this date.
    The line of best fit is not shown, but its parameters are given in the bottom-right corner.
    
    :::
    ::::
    :::::
    
    % :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
    % :::
    