# 2020-03-20 MUL: Mullion, Sentinel-2A overpass

This is a report of the field data collected on 20 March 2020 at the location of Mullion
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

"Instrument(s) used","ASD FR4 (18179/2)"
"Time of field site measurements (UTC)","2020-03-20 00:21:25 to 2020-03-20 00:59:09"
"Time of overpass (UTC)", 2020-03-20 00:06:28
"GPS quality","Bad"
"Reference position","148.862692E, 35.123277S (WGS84)"
"Matchup quality","Excellent"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2020-03-20-MUL.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.034","0.001","0.035","0.006"
"blue","0.044","0.003","0.044","0.007"
"green","0.078","0.004","0.081","0.007"
"red","0.06","0.007","0.058","0.014"
"RE1","0.125","0.008","0.13","0.014"
"RE2","0.311","0.014","0.332","0.031"
"RE3","0.364","0.015","0.385","0.038"
"NIR1","0.373","0.018","0.4","0.038"
"NIR2","0.392","0.015","0.41","0.038"
"SWIR2","0.274","0.007","0.276","0.027"
"SWIR3","0.148","0.008","0.152","0.031"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2020-03-20-MUL.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2020-03-20-MUL.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2020-03-20-MUL.png

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
    