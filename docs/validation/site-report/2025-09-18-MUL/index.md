# 2025-09-18 MUL: Mullion, Landsat 8 and Sentinel-2B dual overpass

This is a report of the field data collected on 18 September 2025 at the location of Mullion
to validate the satellite data of the Landsat 8 and Sentinel-2B dual overpass.
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
"Time of field site measurements (UTC)","2025-09-17 23:50:36 to 2025-09-18 00:26:03"
"Time of Landsat 8 overpass (UTC)", 2025-09-17 23:56:40
"Time of Sentinel-2B overpass (UTC)", 2025-09-18 00:16:25
"GPS quality","Good"
"Reference position","148.86311712E, 35.12339972S (WGS84)"
"Matchup quality for Landsat 8","Excellent"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-09-18-MUL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.021","0.001","0.022","0.004"
"blue","0.024","0.002","0.024","0.005"
"green","0.057","0.003","0.059","0.008"
"red","0.033","0.004","0.031","0.009"
"NIR","0.48","0.034","0.535","0.063"
"SWIR1","0.18","0.006","0.193","0.017"
"SWIR2","0.078","0.003","0.083","0.011"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.024","0.001","0.021","0.004"
"blue","0.028","0.002","0.027","0.005"
"green","0.061","0.004","0.063","0.008"
"red","0.031","0.005","0.029","0.009"
"RE1","0.104","0.006","0.105","0.015"
"RE2","0.376","0.02","0.407","0.043"
"RE3","0.454","0.029","0.502","0.063"
"NIR1","0.475","0.036","0.523","0.064"
"NIR2","0.494","0.03","0.535","0.064"
"SWIR2","0.193","0.005","0.196","0.016"
"SWIR3","0.081","0.003","0.084","0.011"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-09-18-MUL.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-09-18-MUL.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-09-18-MUL.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    