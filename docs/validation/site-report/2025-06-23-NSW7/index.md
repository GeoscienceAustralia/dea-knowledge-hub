# 2025-06-23 NSW7: Transect NSW Site 7, Sentinel-2C overpass

This is a report of the field data collected on 23 June 2025 at the location of Transect NSW Site 7
to validate the satellite data of the Sentinel-2C overpass.
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
"Time of field site measurements (UTC)","2025-06-23 00:38:12 to 2025-06-23 01:07:31"
"Time of overpass (UTC)", 2025-06-22 00:05:43
"GPS quality","Good"
"Reference position","151.4831771E, 30.98591782S (WGS84)"
"Matchup quality","Poor"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-23-NSW7.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.031","0.002","0.043","0.004"
"blue","0.041","0.004","0.055","0.005"
"green","0.075","0.006","0.087","0.007"
"red","0.084","0.008","0.095","0.009"
"RE1","0.163","0.011","0.154","0.012"
"RE2","0.265","0.023","0.26","0.026"
"RE3","0.285","0.024","0.289","0.029"
"NIR1","0.32","0.028","0.335","0.032"
"NIR2","0.33","0.027","0.339","0.031"
"SWIR2","0.258","0.014","0.318","0.022"
"SWIR3","0.139","0.009","0.177","0.017"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-23-NSW7.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-23-NSW7.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-23-NSW7.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    