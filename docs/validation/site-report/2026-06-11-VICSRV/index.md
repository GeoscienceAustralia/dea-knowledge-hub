# 2026-06-11 VICSRV: VIC Serviceton, Sentinel-2A and Sentinel-2B dual overpass

This is a report of the field data collected on 11 June 2026 at the location of VIC Serviceton
to validate the satellite data of the Sentinel-2A and Sentinel-2B dual overpass.
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
"Time of field site measurements (UTC)","2026-06-11 00:06:59 to 2026-06-11 00:41:01"
"Time of overpass (UTC)", "2026-06-11 00:47:26 for Sentinel-2A, 2026-06-11 00:37:13 for Sentinel-2B"
"GPS quality","Good"
"Reference position","140.97013627E, 36.37677168S (WGS84)"
"Matchup quality","Excellent for Sentinel-2A, Good for Sentinel-2B"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2026-06-11-VICSRV.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.058","0.001","0.063","0.007"
"blue","0.072","0.004","0.074","0.008"
"green","0.091","0.005","0.092","0.009"
"red","0.113","0.006","0.111","0.013"
"RE1","0.143","0.006","0.138","0.014"
"RE2","0.18","0.007","0.178","0.02"
"RE3","0.19","0.007","0.185","0.021"
"NIR1","0.199","0.01","0.201","0.022"
"NIR2","0.214","0.008","0.21","0.022"
"SWIR2","0.293","0.011","0.29","0.029"
"SWIR3","0.211","0.008","0.21","0.025"
:::

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.053","0.001","0.063","0.007"
"blue","0.067","0.003","0.073","0.008"
"green","0.085","0.004","0.092","0.009"
"red","0.104","0.006","0.111","0.013"
"RE1","0.13","0.005","0.138","0.014"
"RE2","0.17","0.007","0.178","0.02"
"RE3","0.176","0.006","0.185","0.02"
"NIR1","0.189","0.009","0.201","0.022"
"NIR2","0.2","0.007","0.21","0.022"
"SWIR2","0.279","0.01","0.289","0.029"
"SWIR3","0.195","0.008","0.212","0.025"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2026-06-11-VICSRV.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2026-06-11-VICSRV.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2026-06-11-VICSRV.png

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
No Landsat overpasses were matched to this dataset.

% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    
