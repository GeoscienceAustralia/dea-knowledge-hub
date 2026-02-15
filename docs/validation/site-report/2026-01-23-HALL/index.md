# 2026-01-23 HALL: CSIRO Hall, Landsat 8 overpass

This is a report of the field data collected on 23 January 2026 at the location of CSIRO Hall
to validate the satellite data of the Landsat 8 overpass.
The full collection of data is contained in the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/#share=s-i2o7JwB5gvXOQefhMmTLJaA14b0).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2026-01-23 01:28:28 to 2026-01-23 01:58:23"
"Time of overpass (UTC)", 2026-01-23 23:56:35
"GPS quality","Good"
"Reference position","149.06602167E, 35.18213333S (WGS84)"
"Matchup quality","Mediocre"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2026-01-23-HALL.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.059","0.003","0.082","0.008"
"blue","0.08","0.005","0.103","0.01"
"green","0.12","0.007","0.142","0.013"
"red","0.165","0.011","0.187","0.017"
"NIR","0.277","0.009","0.291","0.023"
"SWIR1","0.421","0.018","0.444","0.037"
"SWIR2","0.282","0.015","0.311","0.033"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2026-01-23-HALL.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2026-01-23-HALL.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2026-01-23-HALL.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

## Fractional Cover

The following figures provide a comparison of Fractional Cover derived from Landsat and
field data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 2
::::{grid-item}
:::{figure} ./FCStats-2026-01-23-HALL.png

Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statstics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2026-01-23-HALL.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    
