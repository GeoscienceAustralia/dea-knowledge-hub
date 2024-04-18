
# 2023-07-25: Mullion, Sentinel-2A overpass

A Daily Validation Summary Report of the surface reflectance data collected on the date of 2023-07-25 by Geoscience&nbsp;Australia. 
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
"Time of field site measurements (UTC)","2023-07-25 01:10:03 to 2023-07-25 01:58:33"
"Time of overpass (UTC)", 2023-07-26 00:16:32
"GPS quality","Good"
"Reference position","148.86261117E, 35.12279053S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands. 
This allows the data to be used to validate Geoscience Australia's other datasets which use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./DailyValidationResults-2023-07-25.csv>`
```

:::{csv-table}
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.04488","0.0015481763465445403","0.044273600098971314","0.009315204470739687"
"blue","0.056975416666666674","0.0050493914477940365","0.05905323038979645","0.013042829484586125"
"green","0.08841125","0.006047444234619558","0.0920048750114346","0.019229790944200322"
"red","0.10452375","0.010346282469442828","0.10395621449979836","0.025602144655099024"
"RE1","0.161215","0.008553787172942756","0.15161078619481552","0.03165035203213386"
"RE2","0.2590554166666667","0.013828535255998333","0.24517303092889134","0.050812040847717795"
"RE3","0.27764416666666664","0.015650198592101705","0.278259346209061","0.058193868212933236"
"NIR1","0.29371833333333336","0.019263702842969268","0.30029337863157296","0.06222828528150687"
"NIR2","0.3149625","0.017533575232013196","0.31371483943929407","0.06460552364610218"
"SWIR2","0.2522054166666667","0.012158471490818881","0.292426929963538","0.059064406134577606"
"SWIR3","0.13983958333333332","0.007713222942436074","0.16631646381320947","0.03637967739714359"
:::

## Figures

Click an image to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-07-25.png

A satellite imagery tile of true colour (RGB) surface reflectance. 
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km. 
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./DayComparison-2023-07-25.png

A band-by-band plot of surface reflectance for satellite and field data. 
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site. 
Field uncertainty error bars are the standard deviation of values after 
averaging all spectra within the same satellite pixels. 

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-07-25.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date. 
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::
