# 2025-03-02 MUL: Mullion, Landsat 9 and Sentinel-2B dual overpass

This is a report of the field data collected on 2 March 2025 at the location of Mullion
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
"Time of field site measurements (UTC)","2025-03-01 22:55:48 to 2025-03-01 23:33:13"
"Time of Landsat 9 overpass (UTC)", 2025-03-01 23:56:32
"Time of Sentinel-2B overpass (UTC)", 2025-03-02 00:16:30
"GPS quality","Good"
"Reference position","148.86257287E, 35.12269702S (WGS84)"
"Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-03-02-MUL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.038","0.002","0.046","0.005"
"blue","0.048","0.002","0.055","0.006"
"green","0.083","0.002","0.092","0.008"
"red","0.091","0.004","0.097","0.012"
"NIR","0.329","0.008","0.355","0.029"
"SWIR1","0.314","0.013","0.334","0.034"
"SWIR2","0.182","0.011","0.195","0.029"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.043","0.001","0.044","0.005"
"blue","0.054","0.003","0.057","0.006"
"green","0.086","0.003","0.091","0.007"
"red","0.095","0.005","0.093","0.012"
"RE1","0.148","0.003","0.151","0.012"
"RE2","0.253","0.005","0.271","0.022"
"RE3","0.286","0.006","0.31","0.026"
"NIR1","0.31","0.009","0.335","0.027"
"NIR2","0.329","0.007","0.35","0.028"
"SWIR2","0.329","0.011","0.328","0.032"
"SWIR3","0.188","0.01","0.19","0.028"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-03-02-MUL.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-03-02-MUL.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-03-02-MUL.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
