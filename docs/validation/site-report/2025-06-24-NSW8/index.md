# 2025-06-24 NSW8: Transect NSW Site 8, Landsat 9 and Sentinel-2B dual overpass

This is a report of the field data collected on 24 June 2025 at the location of Transect NSW Site 8
to validate the satellite data of the Landsat 9 and Sentinel-2B dual overpass.
This site was measured by both ASD and SR3500. Both field datasets are compared to the satellite overpass datasets.
Note that this site is over sand dunes that show significant terrain. This terrain is not expected to be properly
modelled in the satellite data, so validations from this day are not used in the overall validation results.
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

"Instrument(s) used","SR-3500_20680T1 and ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2025-06-24 00:21:00 to 2025-06-24 01:01:17 (SR-3500) and 2025-06-24 00:35:26 to 2025-06-24 01:04:16 (ASD)"
"Time of Landsat 9 overpass (UTC)", 2025-06-23 23:42:59
"Time of Sentinel-2B overpass (UTC)", 2025-06-23 23:55:26
"GPS quality","Both Good"
"Reference position","153.03737372E, 31.08354823S (WGS84 - SR-3500) and 153.037335E, 31.08352667S (WGS84 - ASD)"
"Matchup quality for Landsat 9","Both Excellent"
"Matchup quality for Sentinel-2B","Both Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-24-NSW8.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean (SR-3500)","Field rms (SR-3500)","Field mean (ASD)","Field rms (ASD)"
"CA","0.213","0.032","0.214","0.015","0.228","0.014"
"blue","0.26","0.04","0.241","0.018","0.257","0.017"
"green","0.396","0.071","0.34","0.029","0.364","0.028"
"red","0.489","0.091","0.393","0.037","0.422","0.035"
"NIR","0.553","0.111","0.445","0.04","0.46","0.041"
"SWIR1","0.639","0.126","0.522","0.051","0.543","0.051"
"SWIR2","0.62","0.124","0.516","0.05","0.54","0.051"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean (SR-3500)","Field rms (SR-3500)","Field mean (ASD)","Field rms (ASD)"
"CA","0.217","0.008","0.213","0.015","0.229","0.014"
"blue","0.275","0.065","0.25","0.019","0.268","0.018"
"green","0.392","0.1","0.34","0.029","0.368","0.028"
"red","0.483","0.135","0.397","0.037","0.43","0.037"
"RE1","0.517","0.122","0.408","0.036","0.447","0.039"
"RE2","0.543","0.129","0.423","0.038","0.462","0.041"
"RE3","0.517","0.121","0.435","0.04","0.451","0.04"
"NIR1","0.526","0.152","0.441","0.04","0.483","0.043"
"NIR2","0.541","0.131","0.447","0.041","0.463","0.041"
"SWIR2","0.629","0.136","0.522","0.051","0.57","0.055"
"SWIR3","0.602","0.137","0.515","0.05","0.533","0.05"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-24-NSW8.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-24-NSW8.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-24-NSW8.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
