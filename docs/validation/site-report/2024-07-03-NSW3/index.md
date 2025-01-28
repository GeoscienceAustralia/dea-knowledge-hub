# 2024-07-03 NSW3: Transect NSW Site 3, Landsat 9 and Sentinel-2A dual overpass

This is a report of the field data collected on 3 July 2024 at the location of Transect NSW Site 3
to validate the satellite data of the Landsat 9 and Sentinel-2A dual overpass.
The full collection of data is contained in the 
[National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/#share=s-i2o7JwB5gvXOQefhMmTLJaA14b0).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2024-07-03 00:03:31 to 2024-07-03 00:37:57"
"Time of Landsat 9 overpass (UTC)", 2024-07-03 00:07:15
"Time of Sentinel-2A overpass (UTC)", 2024-07-13 00:25:38
"GPS quality","Good"
"Reference position","145.47862483E, 31.52123898S (WGS84)"
"Matchup quality for Landsat 9","Excellent"
"Matchup quality for Sentinel-2A","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2024-07-03-NSW3.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.03","0.003","0.032","0.007"
"blue","0.038","0.003","0.038","0.008"
"green","0.07","0.006","0.069","0.013"
"red","0.105","0.019","0.088","0.032"
"NIR","0.225","0.013","0.232","0.033"
"SWIR1","0.291","0.027","0.269","0.054"
"SWIR2","0.213","0.031","0.19","0.064"
:::

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.025","0.002","0.029","0.006"
"blue","0.035","0.003","0.036","0.007"
"green","0.063","0.005","0.062","0.011"
"red","0.087","0.021","0.08","0.03"
"RE1","0.132","0.013","0.12","0.026"
"RE2","0.206","0.013","0.192","0.028"
"RE3","0.211","0.014","0.21","0.03"
"NIR1","0.214","0.017","0.219","0.031"
"NIR2","0.222","0.018","0.225","0.032"
"SWIR2","0.258","0.024","0.259","0.051"
"SWIR3","0.175","0.028","0.18","0.06"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2024-07-03-NSW3.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2024-07-03-NSW3.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2024-07-03-NSW3.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
