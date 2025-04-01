# 2025-02-07 MUL: Mullion, Landsat 9 and Sentinel-2B dual overpass

This is a report of the field data collected on 7 February 2025 at the location of Mullion
to validate the satellite data of the Landsat 9 and Sentinel-2B dual overpass.
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

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2025-02-07 00:01:21 to 2025-02-07 00:33:16"
"Time of Landsat 9 overpass (UTC)", 2025-02-06 23:50:48
"Time of Sentinel-2B overpass (UTC)", 2025-02-07 00:06:33
"GPS quality","Good"
"Reference position","148.86258533E, 35.12278745S (WGS84)"
"Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-02-07 MUL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.051","0.001","0.042","0.004"
"blue","0.056","0.001","0.049","0.005"
"green","0.084","0.001","0.082","0.006"
"red","0.081","0.003","0.08","0.01"
"NIR","0.337","0.009","0.343","0.028"
"SWIR1","0.286","0.009","0.298","0.026"
"SWIR2","0.151","0.007","0.168","0.024"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.049","0.001","0.046","0.005"
"blue","0.059","0.002","0.058","0.006"
"green","0.088","0.002","0.093","0.007"
"red","0.085","0.004","0.089","0.012"
"RE1","0.137","0.002","0.147","0.011"
"RE2","0.257","0.007","0.281","0.02"
"RE3","0.3","0.009","0.323","0.027"
"NIR1","0.325","0.011","0.346","0.028"
"NIR2","0.339","0.009","0.36","0.028"
"SWIR2","0.3","0.008","0.325","0.028"
"SWIR3","0.161","0.007","0.187","0.027"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-02-07 MUL.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-02-07 MUL.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-02-07 MUL.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    