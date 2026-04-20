# 2018-06-21 WIN: Winton, Landsat 8 and Sentinel-2A dual overpass

This is a report of the field data collected on 21 June 2018 at the location of Winton
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

"Instrument(s) used","ASD FR4 (16516/1)"
"Time of field site measurements (UTC)","2018-06-21 00:11:45 to 2018-06-21 00:46:52"
"Time of Landsat 8 overpass (UTC)", 2018-06-21 00:28:55
"Time of Sentinel-2A overpass (UTC)", 2018-06-21 00:37:04
"GPS quality","Bad"
"Reference position","142.93854167E, 22.52781389S (WGS84)"
"Matchup quality for Landsat 8","Mediocre"
"Matchup quality for Sentinel-2A","Good"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2018-06-21-WIN.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.144","0.013","0.184","0.012"
"blue","0.179","0.015","0.218","0.014"
"green","0.291","0.023","0.331","0.017"
"red","0.412","0.036","0.466","0.02"
"NIR","0.475","0.031","0.517","0.023"
"SWIR1","0.604","0.043","0.664","0.021"
"SWIR2","0.537","0.046","0.59","0.017"
:::

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.056","0.001","0.055","0.006"
"blue","0.073","0.004","0.074","0.008"
"green","0.135","0.008","0.137","0.015"
"red","0.255","0.015","0.252","0.028"
"RE1","0.281","0.015","0.273","0.03"
"RE2","0.296","0.016","0.291","0.031"
"RE3","0.308","0.016","0.301","0.031"
"NIR1","0.307","0.018","0.307","0.03"
"NIR2","0.318","0.015","0.31","0.03"
"SWIR2","0.443","0.019","0.439","0.035"
"SWIR3","0.354","0.015","0.366","0.033"
"CA","0.16","0.007","0.184","0.012"
"blue","0.199","0.013","0.227","0.014"
"green","0.3","0.017","0.327","0.016"
"red","0.439","0.029","0.473","0.019"
"RE1","0.482","0.029","0.506","0.021"
"RE2","0.497","0.028","0.527","0.022"
"RE3","0.493","0.026","0.52","0.022"
"NIR1","0.497","0.026","0.517","0.022"
"NIR2","0.492","0.023","0.516","0.023"
"SWIR2","0.639","0.035","0.665","0.021"
"SWIR3","0.554","0.036","0.589","0.017"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2018-06-21-WIN.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2018-06-21-WIN.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2018-06-21-WIN.png

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
:::{figure} ./FCStats-2018-06-21-WIN.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2018-06-21-WIN.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    