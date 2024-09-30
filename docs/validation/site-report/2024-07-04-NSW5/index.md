# 2024-07-04-NSW5: Transect NSW Site 5, Landsat 8 overpass

This is a report of the field data collected on 4 July 2024 at the location of Transect NSW Site 5
to validate the satellite data of the Landsat 8 overpass.
The full collection of data is contained in the [National Spectral Database]
(https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
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
"Time of field site measurements (UTC)","2024-07-04 00:00:17 to 2024-07-04 00:32:31"
"Time of overpass (UTC)", 2024-07-04 00:01:10
"GPS quality","Good"
"Reference position","148.21046358E, 32.20980347S (WGS84)"
"Matchup quality","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2024-07-04-NSW5.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.033","0.001","0.045","0.005"
"blue","0.046","0.001","0.055","0.007"
"green","0.079","0.002","0.088","0.008"
"red","0.092","0.003","0.097","0.013"
"NIR","0.238","0.016","0.247","0.027"
"SWIR1","0.256","0.005","0.275","0.027"
"SWIR2","0.164","0.004","0.175","0.02"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2024-07-04-NSW5.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2024-07-04-NSW5.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2024-07-04-NSW5.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    