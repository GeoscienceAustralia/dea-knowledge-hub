# 2018-06-23 LGR: Longreach, Landsat 8 and Sentinel-2B dual overpass

This is a report of the field data collected on 23 June 2018 at the location of Longreach
to validate the satellite data of the Landsat 8 and Sentinel-2B dual overpass.
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

"Instrument(s) used","ASD FR4 (16516/1)"
"Time of field site measurements (UTC)","2018-06-23 00:05:42 to 2018-06-23 00:42:53"
"Time of Landsat 8 overpass (UTC)", 2018-06-23 00:16:59
"Time of Sentinel-2B overpass (UTC)", 2018-06-23 00:27:06
"GPS quality","Bad"
"Reference position","144.31038333E, 23.52441667S (WGS84)"
"Matchup quality for Landsat 8","Excellent"
"Matchup quality for Sentinel-2B","Excellent"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2018-06-23-LGR.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.071","0.001","0.072","0.008"
"blue","0.091","0.002","0.089","0.011"
"green","0.141","0.003","0.137","0.017"
"red","0.188","0.006","0.18","0.023"
"NIR","0.256","0.009","0.245","0.03"
"SWIR1","0.323","0.006","0.323","0.036"
"SWIR2","0.255","0.004","0.268","0.031"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.077","0.001","0.072","0.008"
"blue","0.098","0.003","0.094","0.012"
"green","0.143","0.004","0.137","0.017"
"red","0.194","0.007","0.184","0.023"
"RE1","0.214","0.007","0.201","0.025"
"RE2","0.229","0.009","0.218","0.028"
"RE3","0.241","0.009","0.229","0.029"
"NIR1","0.247","0.01","0.24","0.03"
"NIR2","0.261","0.01","0.247","0.031"
"SWIR2","0.329","0.006","0.323","0.036"
"SWIR3","0.263","0.005","0.268","0.031"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2018-06-23-LGR.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2018-06-23-LGR.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2018-06-23-LGR.png

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
:::{figure} ./FCStats-2018-06-23-LGR.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2018-06-23-LGR.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    