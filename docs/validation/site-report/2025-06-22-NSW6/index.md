# 2025-06-22 NSW6: Transect NSW Site 6, Landsat 9 and Sentinel-2C dual overpass

This is a report of the field data collected on 22 June 2025 at the location of Transect NSW Site 6
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

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2025-06-22 00:18:56 to 2025-06-22 00:49:33"
"Time of Landsat 9 overpass (UTC)", 2025-06-21 23:54:56
"Time of Sentinel-2C overpass (UTC)", 2025-06-22 00:05:32
"GPS quality","Good"
"Reference position","150.0245E, 30.78657S (WGS84)"
"Matchup quality for Landsat 9","Excellent"
"Matchup quality for Sentinel-2C","Excellent"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-22-NSW6.csv>`
```

:::{csv-table} Results of Field data versus Landsat 9 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.031","0.001","0.042","0.013"
"blue","0.041","0.001","0.049","0.015"
"green","0.067","0.003","0.073","0.015"
"red","0.104","0.007","0.111","0.02"
"NIR","0.151","0.016","0.167","0.039"
"SWIR1","0.218","0.021","0.243","0.063"
"SWIR2","0.186","0.02","0.202","0.039"
:::

:::{csv-table} Results of Field data versus Sentinel-2C Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.045","0.001","0.041","0.012"
"blue","0.05","0.002","0.05","0.015"
"green","0.072","0.003","0.07","0.014"
"red","0.114","0.007","0.113","0.021"
"RE1","0.129","0.008","0.124","0.024"
"RE2","0.142","0.009","0.134","0.026"
"RE3","0.145","0.009","0.152","0.031"
"NIR1","0.149","0.01","0.16","0.036"
"NIR2","0.157","0.01","0.166","0.039"
"SWIR2","0.226","0.017","0.243","0.063"
"SWIR3","0.186","0.016","0.203","0.039"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-22-NSW6.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-22-NSW6.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-22-NSW6.png

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
:::{figure} ./FCStats-2025-06-22-NSW6.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2025-06-22-NSW6.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    