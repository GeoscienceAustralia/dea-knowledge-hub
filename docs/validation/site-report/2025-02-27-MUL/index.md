# 2025-02-27 MUL: Mullion, Sentinel-2B overpass

This is a report of the field data collected on 27 February 2025 at the location of Mullion
to validate the satellite data of the Sentinel-2B overpass.
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
"Time of field site measurements (UTC)","2025-02-27 00:02:42 to 2025-02-27 00:37:35"
"Time of overpass (UTC)", 2025-02-27 00:06:35
"GPS quality","Good"
"Reference position","148.86256665E, 35.12276877S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-02-27 MUL.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.043","0.0","0.046","0.004"
"blue","0.055","0.002","0.058","0.005"
"green","0.087","0.002","0.093","0.006"
"red","0.087","0.004","0.092","0.01"
"RE1","0.139","0.002","0.15","0.01"
"RE2","0.258","0.006","0.277","0.021"
"RE3","0.299","0.008","0.319","0.026"
"NIR1","0.319","0.01","0.344","0.027"
"NIR2","0.34","0.008","0.358","0.027"
"SWIR2","0.311","0.008","0.327","0.024"
"SWIR3","0.167","0.008","0.191","0.023"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-02-27 MUL.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-02-27 MUL.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-02-27 MUL.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
