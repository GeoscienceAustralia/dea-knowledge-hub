# 2018-04-22 BLA: Blanchetown, Sentinel-2A overpass

This is a report of the field data collected on 22 April 2018 at the location of Blanchetown
to validate the satellite data of the Sentinel-2A overpass.
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

"Instrument(s) used","ASD FR4 (16356/2)"
"Time of field site measurements (UTC)","2018-04-22 00:51:38 to 2018-04-22 02:08:04"
"Time of overpass (UTC)", 2018-04-22 00:37:06
"GPS quality","Bad"
"Reference position","139.600725E, 34.385141S (WGS84)"
"Matchup quality","Excellent"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2018-04-22-BLA.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.072","0.001","0.059","0.017"
"blue","0.09","0.002","0.074","0.018"
"green","0.125","0.003","0.107","0.022"
"red","0.178","0.006","0.158","0.031"
"RE1","0.201","0.005","0.177","0.032"
"RE2","0.221","0.005","0.196","0.034"
"RE3","0.237","0.005","0.209","0.035"
"NIR1","0.251","0.007","0.225","0.036"
"NIR2","0.267","0.005","0.235","0.037"
"SWIR2","0.392","0.005","0.365","0.059"
"SWIR3","0.302","0.006","0.297","0.059"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2018-04-22-BLA.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2018-04-22-BLA.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2018-04-22-BLA.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
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
No Landsat overpasses were matched to this dataset.

% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    