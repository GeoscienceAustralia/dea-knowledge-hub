# 2025-06-19 NSW3: Transect NSW Site 3, Sentinel-2C overpass

This is a report of the field data collected on 19 June 2025 at the location of Transect NSW Site 3
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
"Time of field site measurements (UTC)","2025-06-18 23:55:46 to 2025-06-19 00:30:23"
"Time of overpass (UTC)", 2025-06-18 00:25:54
"GPS quality","Good"
"Reference position","145.47852618E, 31.5213356S (WGS84)"
"Matchup quality","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-19-NSW3.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.035","0.001","0.04","0.004"
"blue","0.049","0.002","0.051","0.004"
"green","0.086","0.005","0.086","0.007"
"red","0.152","0.02","0.139","0.022"
"RE1","0.192","0.013","0.174","0.018"
"RE2","0.242","0.01","0.227","0.019"
"RE3","0.243","0.012","0.233","0.021"
"NIR1","0.252","0.016","0.254","0.025"
"NIR2","0.255","0.015","0.248","0.027"
"SWIR2","0.391","0.018","0.382","0.03"
"SWIR3","0.3","0.023","0.29","0.038"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-19-NSW3.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-19-NSW3.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-19-NSW3.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    