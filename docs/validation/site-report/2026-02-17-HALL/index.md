# 2026-02-17 HALL: CSIRO Hall, Landsat 9 and Sentinel-2C dual overpass

This is a report of the field data collected on 17 February 2026 at the location of CSIRO Hall
to validate the satellite data of the Landsat 9 and Sentinel-2C dual overpass.
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

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2026-02-17 00:02:14 to 2026-02-17 01:01:10"
"Time of Landsat 9 overpass (UTC)", 2026-02-16 23:56:38
"Time of Sentinel-2C overpass (UTC)", 2026-02-17 00:06:33
"GPS quality","Good"
"Reference position","149.06603913E, 35.18217217S (WGS84)"
"Matchup quality for Landsat 9","Good"
"Matchup quality for Sentinel-2C","Excellent"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2026-02-17-HALL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.051","0.003","0.067","0.007"
"blue","0.068","0.004","0.081","0.008"
"green","0.1","0.005","0.11","0.01"
"red","0.131","0.008","0.139","0.013"
"NIR","0.238","0.009","0.233","0.02"
"SWIR1","0.389","0.02","0.4","0.029"
"SWIR2","0.269","0.017","0.283","0.027"
:::

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.063","0.002","0.067","0.007"
"blue","0.08","0.005","0.084","0.008"
"green","0.107","0.006","0.11","0.01"
"red","0.143","0.009","0.141","0.013"
"RE1","0.169","0.006","0.159","0.013"
"RE2","0.198","0.007","0.183","0.015"
"RE3","0.215","0.007","0.205","0.017"
"NIR1","0.233","0.011","0.223","0.019"
"NIR2","0.245","0.008","0.234","0.02"
"SWIR2","0.404","0.015","0.403","0.029"
"SWIR3","0.271","0.014","0.284","0.027"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2026-02-17-HALL.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2026-02-17-HALL.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2026-02-17-HALL.png

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
:::{figure} ./FCStats-2026-02-17-HALL.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2026-02-17-HALL.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::

% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    