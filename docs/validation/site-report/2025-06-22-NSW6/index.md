# 2025-06-22 NSW6: Transect NSW Site 6, Landsat 9 and Sentinel-2C dual overpass

This is a report of the field data collected on 22 June 2025 at the location of Transect NSW Site 6
to validate the satellite data of the Landsat 9 and Sentinel-2C dual overpass.
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

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2025-06-22 00:18:56 to 2025-06-22 00:49:33"
"Time of Landsat 9 overpass (UTC)", 2025-06-21 23:54:56
"Time of Sentinel-2C overpass (UTC)", 2025-06-22 00:05:32
"GPS quality","Good"
"Reference position","150.02461333E, 30.78657S (WGS84)"
"Matchup quality for Landsat 9","Excellent"
"Matchup quality for Sentinel-2C","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-22-NSW6.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.041","0.003","0.045","0.008"
"blue","0.051","0.005","0.053","0.011"
"green","0.084","0.007","0.085","0.015"
"red","0.103","0.011","0.103","0.022"
"NIR","0.289","0.011","0.275","0.025"
"SWIR1","0.26","0.018","0.271","0.033"
"SWIR2","0.165","0.015","0.177","0.031"
:::

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.045","0.002","0.044","0.014"
"blue","0.05","0.002","0.054","0.017"
"green","0.073","0.003","0.076","0.016"
"red","0.116","0.008","0.123","0.022"
"RE1","0.131","0.009","0.135","0.026"
"RE2","0.145","0.012","0.146","0.029"
"RE3","0.148","0.013","0.155","0.032"
"NIR1","0.152","0.012","0.163","0.036"
"NIR2","0.161","0.014","0.169","0.039"
"SWIR2","0.232","0.02","0.252","0.066"
"SWIR3","0.191","0.018","0.214","0.042"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-22-NSW6.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-22-NSW6.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-22-NSW6.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
