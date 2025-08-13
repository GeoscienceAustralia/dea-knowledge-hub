# 2025-06-18 NSW1: Transect NSW Site 1, Landsat 9 and Sentinel-2B dual overpass

This is a report of the field data collected on 18 June 2025 at the location of Transect NSW Site 1
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
"Time of field site measurements (UTC)","2025-06-18 00:09:57 to 2025-06-18 00:41:30"
"Time of Landsat 9 overpass (UTC)", 2025-06-18 00:20:00
"Time of Sentinel-2B overpass (UTC)", 2025-06-19 00:45:50
"GPS quality","Good"
"Reference position","142.10420015E, 31.8140458S (WGS84)"
"Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-18-NSW1.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.04","0.002","0.05","0.007"
"blue","0.055","0.003","0.062","0.009"
"green","0.112","0.008","0.12","0.021"
"red","0.201","0.017","0.203","0.044"
"NIR","0.287","0.017","0.287","0.04"
"SWIR1","0.423","0.024","0.427","0.063"
"SWIR2","0.337","0.022","0.345","0.062"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.046","0.001","0.05","0.007"
"blue","0.062","0.004","0.064","0.009"
"green","0.113","0.008","0.115","0.019"
"red","0.212","0.02","0.204","0.044"
"RE1","0.245","0.018","0.234","0.045"
"RE2","0.277","0.018","0.265","0.042"
"RE3","0.284","0.018","0.274","0.042"
"NIR1","0.29","0.02","0.284","0.041"
"NIR2","0.296","0.017","0.285","0.04"
"SWIR2","0.436","0.023","0.429","0.063"
"SWIR3","0.347","0.022","0.346","0.062"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-18-NSW1.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-18-NSW1.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-18-NSW1.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    