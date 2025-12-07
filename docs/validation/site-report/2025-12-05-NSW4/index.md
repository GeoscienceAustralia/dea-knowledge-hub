# 2025-12-05 NSW4: Transect NSW Site 4, Landsat 8 and Sentinel-2C dual overpass

This is a report of the field data collected on 5 December 2025 at the location of Transect NSW Site 4
to validate the satellite data of the Landsat 8 and Sentinel-2C dual overpass.
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
"Time of field site measurements (UTC)","2025-12-04 22:30:46 to 2025-12-04 23:04:06"
"Time of Landsat 8 overpass (UTC)", 2025-12-05 00:08:17
"Time of Sentinel-2C overpass (UTC)", 2025-12-05 00:25:40
"GPS quality","Good"
"Reference position","146.978075E, 31.52689S (WGS84)"
"Matchup quality for Landsat 8","Excellent"
"Matchup quality for Sentinel-2C","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-12-05-NSW4.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.038","0.001","0.039","0.003"
"blue","0.047","0.001","0.048","0.003"
"green","0.087","0.004","0.093","0.008"
"red","0.17","0.008","0.181","0.023"
"NIR","0.262","0.009","0.272","0.023"
"SWIR1","0.402","0.018","0.436","0.034"
"SWIR2","0.352","0.018","0.389","0.04"
:::

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.04","0.001","0.039","0.003"
"blue","0.049","0.002","0.051","0.003"
"green","0.085","0.003","0.09","0.008"
"red","0.173","0.008","0.188","0.024"
"RE1","0.201","0.007","0.215","0.026"
"RE2","0.221","0.008","0.238","0.026"
"RE3","0.241","0.008","0.253","0.026"
"NIR1","0.258","0.01","0.265","0.025"
"NIR2","0.259","0.009","0.273","0.024"
"SWIR2","0.401","0.014","0.44","0.034"
"SWIR3","0.344","0.013","0.391","0.041"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-12-05-NSW4.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-12-05-NSW4.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-12-05-NSW4.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    