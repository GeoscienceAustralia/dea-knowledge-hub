# 2024-07-02-NSW2: Transect NSW Site 2, Landsat 8 overpass

A Site Validation Summary Report of the surface reflectance data collected on the date of 2024-07-02-NSW2 by Geoscience&nbsp;Australia.
The full collection of data is contained in the [National Spectral Database](https://www.dea.ga.gov.au/products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2024-07-02 00:15:44 to 2024-07-02 01:17:09"
"Time of overpass (UTC)", 2024-07-02 00:13:30
"GPS quality","Good"
"Reference position","143.48095333E, 31.595245S (WGS84)"
"Matchup quality","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./SiteValidationResults-2024-07-02-NSW2.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.055","0.003","0.068","0.007"
"blue","0.067","0.004","0.077","0.008"
"green","0.092","0.004","0.103","0.008"
"red","0.104","0.007","0.114","0.013"
"NIR","0.185","0.006","0.182","0.011"
"SWIR1","0.22","0.008","0.226","0.014"
"SWIR2","0.18","0.01","0.19","0.017"
:::

## Figures

Click an image to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2024-07-02-NSW2.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2024-07-02-NSW2.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2024-07-02-NSW2.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    