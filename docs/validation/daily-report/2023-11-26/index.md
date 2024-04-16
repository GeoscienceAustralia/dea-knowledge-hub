
# 2023-11-26: Transect South Australia Site 1, Landsat 8 overpass

A Daily Validation Summary Report of the surface reflectance data collected on the date of 2023-11-26 by Geoscience&nbsp;Australia. 
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

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-11-26 00:05:36 to 2023-11-26 00:53:24"
"Time of overpass (UTC)", 2023-11-26 00:33:00
"GPS quality","Good"
"Reference position","140.64201522E, 32.17492712S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands. 
This allows the data to be used to validate Geoscience Australia's other datasets which use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./DailyValidationResults-2023-11-26.csv>`
```

:::{csv-table}
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.0557","0.000895","0.0508","0.00527"
"blue","0.0681","0.00127","0.0646","0.00751"
"green","0.118","0.00385","0.119","0.0244"
"red","0.21","0.00766","0.21","0.0569"
"NIR","0.281","0.00876","0.279","0.0584"
"SWIR1","0.371","0.00847","0.378","0.0606"
"SWIR2","0.303","0.0075","0.318","0.0651"
:::

## Figures

Click an image to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-11-26.png

A satellite imagery tile of true colour (RGB) surface reflectance. 
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km. 
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./DayComparison-2023-11-26.png

A band-by-band plot of surface reflectance for satellite and field data. 
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site. 
Field uncertainty error bars are the standard deviation of values after 
averaging all spectra within the same satellite pixels. 

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-11-26.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date. 
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::
