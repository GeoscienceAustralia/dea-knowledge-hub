# 2025-12-03 NSW2: Transect NSW Site 2, Landsat 8 and Sentinel-2B dual overpass

This is a report of the field data collected on 3 December 2025 at the location of Transect NSW Site 2
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
"Time of field site measurements (UTC)","2025-12-03 05:30:04 to 2025-12-03 05:56:53"
"Time of Landsat 8 overpass (UTC)", 2025-12-03 00:20:38
"Time of Sentinel-2B overpass (UTC)", 2025-12-03 00:35:32
"GPS quality","Good"
"Reference position","143.48308167E, 31.596075S (WGS84)"
"Matchup quality for Landsat 8","Excellent"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-12-03-NSW2.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.052","0.001","0.049","0.005"
"blue","0.065","0.001","0.063","0.006"
"green","0.12","0.005","0.121","0.018"
"red","0.216","0.013","0.223","0.038"
"NIR","0.29","0.014","0.302","0.037"
"SWIR1","0.423","0.012","0.447","0.042"
"SWIR2","0.348","0.012","0.371","0.046"
"CA","0.111","0.003","0.111","0.012"
"blue","0.13","0.003","0.131","0.015"
"green","0.173","0.005","0.17","0.02"
"red","0.215","0.006","0.212","0.024"
"NIR","0.272","0.006","0.267","0.028"
"SWIR1","0.342","0.004","0.347","0.027"
"SWIR2","0.296","0.004","0.304","0.024"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.058","0.001","0.049","0.005"
"blue","0.072","0.001","0.067","0.007"
"green","0.122","0.004","0.117","0.017"
"red","0.23","0.012","0.229","0.039"
"RE1","0.26","0.012","0.256","0.041"
"RE2","0.275","0.013","0.277","0.042"
"RE3","0.288","0.013","0.291","0.041"
"NIR1","0.3","0.013","0.298","0.039"
"NIR2","0.3","0.011","0.302","0.038"
"SWIR2","0.433","0.01","0.448","0.042"
"SWIR3","0.359","0.01","0.37","0.046"
"CA","0.115","0.001","0.11","0.012"
"blue","0.14","0.005","0.134","0.015"
"green","0.175","0.007","0.167","0.019"
"red","0.223","0.008","0.212","0.025"
"RE1","0.24","0.007","0.226","0.026"
"RE2","0.25","0.007","0.237","0.027"
"RE3","0.261","0.007","0.248","0.027"
"NIR1","0.275","0.009","0.259","0.027"
"NIR2","0.278","0.007","0.264","0.028"
"SWIR2","0.348","0.005","0.344","0.027"
"SWIR3","0.3","0.004","0.3","0.024"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-12-03-NSW2.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-12-03-NSW2.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-12-03-NSW2.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    