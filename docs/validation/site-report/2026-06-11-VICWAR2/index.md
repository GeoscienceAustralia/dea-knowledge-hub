# 2026-06-11 VICWAR2: Vic Warrangine Park 2, Landsat 8 overpass

IMPORTANT NOTE: Both Landsat and Sentinel products are affected by poor correction of the Aerosol Optical Thickness (AOT) for this location and date.
This appears to be a limitation on the input AOT data, rather than the model used to generate the products. This manifests as significantly darker
short wavelength bands (CA, blue, green, red) and slightly brighter in other bands. Results for this site and day will not be included in future work.
Also note that the overpass occurred approximately 3 days before the field site measurements, which is outside of normal procedure to measure the
site within 24 hours of an overpass.

This is a report of the field data collected on 11 June 2026 at the location of Vic Warrangine Park 2
to validate the satellite data of the Landsat 8 overpass.
The full collection of data is contained in the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/). An explanation of how to read these reports can be found on the
[Daily Validation Summary Reports](https://knowledge.dea.ga.gov.au/guides/setup/validation/daily-summary-reports/) page.

"SWIR2","0.02","0.018","0.012","0.013"
IMPORTANT NOTE: Both Landsat and Sentinel products are affected by poor correction of the Aerosol Optical Thickness (AOT) for this location and date.
This appears to be a limitation on the input AOT data, rather than the model used to generate the products. This manifests as significantly darker
short wavelength bands (CA, blue, green, red) and slightly brighter in other bands. Results for this site and day will not be included in future work.
Also note that the overpass occurred approximately 3 days before the field site measurements, which is outside of normal procedure to measure the
site within 24 hours of an overpass.

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","SR-3500_20680T1"
"Time of field site measurements (UTC)","2026-06-11 02:50:12 to 2026-06-11 03:20:45"
"Time of overpass (UTC)", 2026-06-08 00:02:56
"GPS quality","Good"
"Reference position","145.18998333E, 38.321976S (WGS84)"
"Matchup quality","Good"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2026-06-11-VICWAR2.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.003","0.004","0.027","0.011"
"blue","0.011","0.01","0.03","0.014"
"green","0.032","0.022","0.043","0.019"
"red","0.041","0.029","0.041","0.024"
"NIR","0.066","0.044","0.044","0.044"
"SWIR1","0.031","0.026","0.02","0.026"
"SWIR2","0.016","0.013","0.011","0.012"
:::

## Figures

The following figures provide visual representations of the surface reflectance data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2026-06-11-VICWAR2.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the approximate location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2026-06-11-VICWAR2.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2026-06-11-VICWAR2.png

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
The following figures provide a comparison of FC
derived from Landsat and field data, where available. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 2
::::{grid-item}
:::{figure} ./FCStats-2026-06-11-VICWAR2.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2026-06-11-VICWAR2.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    
