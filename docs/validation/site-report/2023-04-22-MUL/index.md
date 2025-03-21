# 2023-04-22 MUL: Mullion, Sentinel-2B overpass

This is a report of the field data collected on 22 April 2023 at the location of Mullion
to validate the satellite data of the Sentinel-2B overpass.
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
"Time of field site measurements (UTC)","2023-04-22 00:06:39 to 2023-04-22 01:06:24"
"Time of overpass (UTC)", 2023-04-22 00:16:29
"GPS quality","Good"
"Reference position","148.86276E, 35.123137S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2023-04-22-MUL.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.038","0.001","0.039","0.007"
"blue","0.052","0.004","0.054","0.01"
"green","0.084","0.005","0.084","0.015"
"red","0.099","0.008","0.097","0.02"
"RE1","0.142","0.007","0.135","0.024"
"RE2","0.229","0.012","0.214","0.041"
"RE3","0.241","0.014","0.242","0.046"
"NIR1","0.257","0.016","0.262","0.049"
"NIR2","0.274","0.014","0.273","0.05"
"SWIR2","0.264","0.009","0.268","0.047"
"SWIR3","0.144","0.006","0.152","0.029"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-04-22-MUL.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2023-04-22-MUL.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-04-22-MUL.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
