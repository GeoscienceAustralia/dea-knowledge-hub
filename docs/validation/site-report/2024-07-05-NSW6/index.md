# 2024-07-05-NSW6: Transect NSW Site 6, Landsat 9 and Sentinel-2B dual overpass

A Site Validation Summary Report of the surface reflectance data collected on the date of 2024-07-05-NSW6 by Geoscience&nbsp;Australia.
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
"Time of field site measurements (UTC)","2024-07-04 23:41:39 to 2024-07-05 00:38:22"
"Time of Landsat 9 overpass (UTC)", 2024-07-04 23:54:33
"Time of Sentinel-2B overpass (UTC)", 2024-07-15 00:15:28
"GPS quality","Good"
"Reference position","150.02628167E, 30.78772667S (WGS84)"
"Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./SiteValidationResults-2024-07-05-NSW6.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.019","0.004","0.033","0.007"
"blue","0.022","0.004","0.037","0.009"
"green","0.046","0.01","0.068","0.016"
"red","0.039","0.01","0.054","0.025"
"NIR","0.304","0.137","0.42","0.191"
"SWIR1","0.14","0.021","0.189","0.053"
"SWIR2","0.073","0.018","0.098","0.05"
:::

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./SiteValidationResults-2024-07-05-NSW6.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.036","0.004","0.029","0.007"
"blue","0.036","0.005","0.035","0.008"
"green","0.057","0.01","0.064","0.016"
"red","0.044","0.014","0.048","0.024"
"RE1","0.09","0.014","0.107","0.027"
"RE2","0.295","0.138","0.337","0.158"
"RE3","0.339","0.164","0.393","0.189"
"NIR1","0.348","0.169","0.403","0.188"
"NIR2","0.362","0.165","0.409","0.186"
"SWIR2","0.152","0.02","0.183","0.051"
"SWIR3","0.076","0.021","0.093","0.047"
:::

## Figures

Click an image to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2024-07-05-NSW6.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2024-07-05-NSW6.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2024-07-05-NSW6.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    