# 2021-11-15-WLC: Wilcannia, Landsat 8 overpass

This is a report of the field data collected on 15 November 2021 at the location of Wilcannia
to validate the satellite data of the Landsat 8 overpass.
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
"Time of field site measurements (UTC)","2021-11-14 12:21:40 to 2021-11-15 00:41:26"
"Time of overpass (UTC)", 2021-11-15 00:14:34
"GPS quality","Good"
"Reference position","143.82192228E, 31.4493214S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2021-11-15-WLC.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.107","0.005","0.095","0.012"
"blue","0.122","0.006","0.11","0.015"
"green","0.16","0.007","0.148","0.02"
"red","0.188","0.009","0.174","0.024"
"NIR","0.269","0.009","0.255","0.026"
"SWIR1","0.301","0.01","0.292","0.031"
"SWIR2","0.267","0.009","0.262","0.031"
"CA","0.208","0.012","0.189","0.052"
"blue","0.248","0.013","0.221","0.06"
"green","0.33","0.013","0.284","0.076"
"red","0.402","0.013","0.336","0.089"
"NIR","0.494","0.011","0.41","0.108"
"SWIR1","0.496","0.01","0.412","0.11"
"SWIR2","0.467","0.011","0.388","0.11"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2021-11-15-WLC.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2021-11-15-WLC.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2021-11-15-WLC.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    