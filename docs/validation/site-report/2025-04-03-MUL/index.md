# 2025-04-03 MUL: Mullion, Landsat 9 and Sentinel-2C dual overpass

This is a report of the field data collected on 3 April 2025 at the location of Mullion
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

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2025-04-02 23:54:27 to 2025-04-03 00:28:23"
"Time of Landsat 9 overpass (UTC)", 2025-04-02 23:56:16
"Time of Sentinel-2C overpass (UTC)", 2025-04-03 00:06:54
"GPS quality","Good"
"Reference position","148.86261238E, 35.12274652S (WGS84)"
"Matchup quality for Landsat 9","Excellent"
"Matchup quality for Sentinel-2C","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-04-03-MUL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.054","0.001","0.058","0.005"
"blue","0.065","0.002","0.069","0.006"
"green","0.093","0.002","0.101","0.008"
"red","0.109","0.002","0.117","0.01"
"NIR","0.283","0.007","0.3","0.023"
"SWIR1","0.341","0.011","0.374","0.027"
"SWIR2","0.226","0.011","0.251","0.027"
:::

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.057","0.001","0.057","0.005"
"blue","0.071","0.002","0.07","0.006"
"green","0.097","0.003","0.099","0.007"
"red","0.114","0.004","0.115","0.01"
"RE1","0.163","0.003","0.156","0.011"
"RE2","0.231","0.006","0.235","0.018"
"RE3","0.252","0.006","0.264","0.021"
"NIR1","0.273","0.008","0.284","0.022"
"NIR2","0.284","0.006","0.296","0.022"
"SWIR2","0.352","0.008","0.369","0.026"
"SWIR3","0.226","0.009","0.246","0.026"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-04-03-MUL.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-04-03-MUL.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-04-03-MUL.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    