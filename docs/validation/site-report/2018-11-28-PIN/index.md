# 2018-11-28 PIN: Pinnacles, Landsat 8 and Sentinel-2A dual overpass

This is a report of the field data collected on 28 November 2018 at the location of Pinnacles
to validate the satellite data of the Landsat 8 and Sentinel-2A dual overpass.
The full collection of data is contained in the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/). An explanation of how to read these reports can be found on the
[Daily Validation Summary Reports](https://knowledge.dea.ga.gov.au/guides/setup/validation/daily-summary-reports/) page.

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18296/4)"
"Time of field site measurements (UTC)","2018-11-28 02:43:27 to 2018-11-28 03:25:04"
"Time of Landsat 8 overpass (UTC)", 2018-11-28 02:11:10
"Time of Sentinel-2A overpass (UTC)", 2018-11-28 02:26:02
"GPS quality","Good"
"Reference position","115.15589433E, 30.58496833S (WGS84)"
"Matchup quality for Landsat 8","Mediocre"
"Matchup quality for Sentinel-2A","Mediocre"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2018-11-28-PIN.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.18","0.006","0.17","0.016"
"blue","0.222","0.008","0.208","0.017"
"green","0.384","0.008","0.364","0.014"
"red","0.485","0.009","0.456","0.015"
"NIR","0.594","0.01","0.561","0.019"
"SWIR1","0.643","0.01","0.604","0.019"
"SWIR2","0.47","0.008","0.445","0.019"
:::

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.184","0.004","0.167","0.015"
"blue","0.234","0.009","0.22","0.017"
"green","0.376","0.007","0.361","0.014"
"red","0.481","0.007","0.457","0.015"
"RE1","0.512","0.007","0.481","0.016"
"RE2","0.534","0.007","0.505","0.016"
"RE3","0.576","0.008","0.55","0.017"
"NIR1","0.582","0.009","0.557","0.018"
"NIR2","0.59","0.008","0.56","0.018"
"SWIR2","0.636","0.008","0.602","0.019"
"SWIR3","0.455","0.007","0.444","0.018"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2018-11-28-PIN.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2018-11-28-PIN.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2018-11-28-PIN.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

## Fractional Cover

A more detailed description of these results can be found at
[Daily Validation Summary Reports](https://knowledge.dea.ga.gov.au/guides/setup/validation/daily-summary-reports/).

[DEA Fractional Cover (FC)](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-fractional-cover)
is a derivative product, based on measured surface reflectance. Here, we apply
the same processing to the field measurements to compare the satellite- and
field-derived FC values. Please note, this is not validation of DEA Fractional Cover,
but rather quantifying the differences between field and satellite measurements an
their impact on derivative products. There is currently no FC product based on Sentinel
measurements, so we only validate Landsat-derived FC.
The following figures provide a comparison of FC
derived from Landsat and field data, where available. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 2
::::{grid-item}
:::{figure} ./FCStats-2018-11-28-PIN.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2018-11-28-PIN.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    