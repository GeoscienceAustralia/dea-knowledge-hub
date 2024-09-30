# 2024-07-01-NSW1: Transect NSW Site 4, Landsat 9 and Sentinel-2B dual overpass

This is a report of the field data collected on 1 July 2024 at the location of Transect NSW Site 4
to validate the satellite data of the Landsat 9 and Sentinel-2B dual overpass.
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
"Time of field site measurements (UTC)","2024-07-01 01:16:53 to 2024-07-01 01:44:53"
"Time of Landsat 9 overpass (UTC)", 2024-07-01 00:19:34
"Time of Sentinel-2B overpass (UTC)", 2024-07-14 00:45:57
"GPS quality","Good"
"Reference position","142.10367762E, 31.81348317S (WGS84)"
"Matchup quality for Landsat 9","Poor"
"Matchup quality for Sentinel-2B","Poor"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2024-07-01-NSW1.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.148","0.013","0.056","0.011"
"blue","0.153","0.014","0.068","0.014"
"green","0.175","0.013","0.126","0.029"
"red","0.22","0.014","0.214","0.057"
"NIR","0.265","0.015","0.286","0.069"
"SWIR1","0.344","0.014","0.449","0.106"
"SWIR2","0.282","0.012","0.379","0.102"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.07","0.008","0.052","0.01"
"blue","0.064","0.009","0.067","0.014"
"green","0.079","0.011","0.116","0.026"
"red","0.112","0.016","0.207","0.055"
"RE1","0.127","0.017","0.233","0.061"
"RE2","0.142","0.017","0.255","0.066"
"RE3","0.145","0.017","0.266","0.068"
"NIR1","0.144","0.019","0.273","0.067"
"NIR2","0.149","0.018","0.276","0.066"
"SWIR2","0.203","0.024","0.435","0.103"
"SWIR3","0.158","0.022","0.364","0.097"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2024-07-01-NSW1.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2024-07-01-NSW1.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2024-07-01-NSW1.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    