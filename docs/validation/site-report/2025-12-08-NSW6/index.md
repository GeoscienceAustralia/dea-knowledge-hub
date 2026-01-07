# 2025-12-08 NSW6: Transect NSW Site 6, Sentinel-2C and Landsat 9 dual overpass

This is a report of the field data collected on 8 December 2025 at the location of Transect NSW Site 6
to validate the satellite data of the Sentinel-2C and Landsat 9 dual overpass.
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
"Time of field site measurements (UTC)","2025-12-07 21:58:10 to 2025-12-07 22:39:15"
"Time of Sentinel-2C overpass (UTC)", 2025-12-09 00:05:21
"Time of Landsat 9 overpass (UTC)", 2025-12-07 23:49:50
"GPS quality","Good"
"Reference position","150.02466938E, 30.78663632S (WGS84)"
"Matchup quality","Mediocre for Sentinel2c, Good for Landsat9"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-12-08-NSW6.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.051","0.002","0.032","0.004"
"blue","0.056","0.002","0.041","0.005"
"green","0.079","0.004","0.067","0.007"
"red","0.127","0.01","0.113","0.012"
"RE1","0.14","0.012","0.124","0.014"
"RE2","0.152","0.013","0.133","0.016"
"RE3","0.175","0.016","0.165","0.022"
"NIR1","0.182","0.017","0.173","0.023"
"NIR2","0.189","0.018","0.177","0.024"
"SWIR2","0.248","0.027","0.225","0.036"
"SWIR3","0.197","0.026","0.189","0.031"
:::

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.042","0.002","0.033","0.005"
"blue","0.049","0.002","0.04","0.005"
"green","0.076","0.005","0.069","0.007"
"red","0.124","0.013","0.111","0.012"
"NIR","0.186","0.026","0.174","0.024"
"SWIR1","0.247","0.039","0.224","0.036"
"SWIR2","0.204","0.037","0.189","0.031"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-12-08-NSW6.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-12-08-NSW6.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-12-08-NSW6.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    