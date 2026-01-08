# 2025-12-03 NSW1: Transect NSW Site 1, Landsat 8 and Sentinel-2B dual overpass

This is a report of the field data collected on 3 December 2025 at the location of Transect NSW Site 1
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

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2025-12-02 22:45:48 to 2025-12-02 23:22:12"
"Time of Landsat 8 overpass (UTC)", 2025-12-03 00:20:38
"Time of Sentinel-2B overpass (UTC)", 2025-12-03 00:35:51
"GPS quality","Good"
"Reference position","142.10369333E, 31.81348667S (WGS84)"
"Matchup quality for Landsat 8","Excellent"
"Matchup quality for Sentinel-2B","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-12-03-NSW1.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.052","0.001","0.049","0.005"
"blue","0.065","0.001","0.063","0.006"
"green","0.119","0.005","0.121","0.018"
"red","0.215","0.013","0.223","0.038"
"NIR","0.288","0.014","0.302","0.037"
"SWIR1","0.421","0.012","0.447","0.041"
"SWIR2","0.348","0.012","0.371","0.046"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.058","0.001","0.049","0.005"
"blue","0.072","0.002","0.067","0.007"
"green","0.122","0.004","0.117","0.017"
"red","0.23","0.012","0.229","0.039"
"RE1","0.257","0.012","0.256","0.041"
"RE2","0.272","0.012","0.277","0.042"
"RE3","0.285","0.013","0.291","0.041"
"NIR1","0.292","0.013","0.298","0.039"
"NIR2","0.297","0.011","0.302","0.038"
"SWIR2","0.432","0.01","0.448","0.042"
"SWIR3","0.361","0.01","0.37","0.046"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-12-03-NSW1.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-12-03-NSW1.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-12-03-NSW1.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    