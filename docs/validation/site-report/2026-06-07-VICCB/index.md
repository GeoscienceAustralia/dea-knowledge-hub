# 2026-06-07 VICCB: Vic Cerberus, Sentinel-2B and Landsat 8 dual overpass

IMPORTANT NOTE: Both Landsat and Sentinel products are affected by poor correction of the Aerosol Optical Thickness (AOT) for this location and date.
This appears to be a limitation on the input AOT data, rather than the model used to generate the products. This manifests as significantly darker
short wavelength bands (CA, blue, green, red) and slightly brighter in other bands. Results for this site and day will not be included in future work.

This is a report of the field data collected on 7 June 2026 at the location of Vic Cerberus
to validate the satellite data of the Sentinel-2B and Landsat 8 dual overpass.
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

"Instrument(s) used","SR-3500_20680T1" and "ASD FR4 (18179/3)"
"Time of SR-3500 field site measurements (UTC)","2026-06-06 23:52:50 to 2026-06-07 00:28:32"
"Time of ASD field site measurements (UTC)","2026-06-07 00:31:14 to 2026-06-07 01:19:18"
"Time of Sentinel-2B overpass (UTC)", 2026-06-08 00:27:29
"Time of Landsat 8 overpass (UTC)", 2026-06-08 00:02:56
"GPS quality","Good for both"
"Reference position (SR3500)","145.1765E, 38.36313333S (WGS84)"
"Reference position (ASD)","145.174188E 38.361201S (WGS84)"
"Matchup quality","All Mediocre"
:::

## Surface Reflectance Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2026-06-07-VICCB.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2B Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean (SR3500)","Field rms (SR3500)","Field mean (ASD)","Field rms (ASD)"
"CA","0.0","0.0","0.029","0.002","0.029","0.004"
"blue","0.0","0.0","0.036","0.002","0.037","0.005"
"green","0.01","0.002","0.056","0.002","0.059","0.006"
"red","0.02","0.003","0.054","0.003","0.057","0.008"
"RE1","0.073","0.006","0.098","0.004","0.102","0.01"
"RE2","0.184","0.012","0.192","0.01","0.199","0.019"
"RE3","0.203","0.013","0.202","0.009""0.215","0.021"
"NIR1","0.224","0.017","0.221","0.009","0.236","0.022"
"NIR2","0.24","0.015","0.231","0.01","0.247","0.023"
"SWIR2","0.245","0.016","0.23","0.01","0.264","0.027"
"SWIR3","0.131","0.01","0.122","0.008","0.15","0.021"
:::

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean (SR3500)","Field rms (SR3500)","Field mean (ASD)","Field rms (ASD)"
"CA","0.0","0.0","0.029","0.002","0.029","0.004"
"blue","0.004","0.001","0.033","0.002""0.034","0.004"
"green","0.034","0.005","0.054","0.002","0.057","0.006"
"red","0.037","0.005","0.054","0.003","0.057","0.008"
"NIR","0.248","0.018","0.23","0.01","0.246","0.022"
"SWIR1","0.237","0.025","0.227","0.01","0.261","0.027"
"SWIR2","0.125","0.014","0.121","0.008","0.149","0.021"
:::

## Figures

The following figures provide visual representations of the surface reflectance data.
Note that comparison figures are only shown for SR3500 data. ASD data are very close to the SR3500
data. Also note that there is a small mismatch between the location of the SR3500 and ASD areas, as shown by the lower figure.
(Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2026-06-07-VICCB.png

Satellite imagery tiles of true colour (RGB) surface reflectance.
They each cover an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2026-06-07-VICCB.png

Band-by-band plots of surface reflectance for field data versus each satellite.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2026-06-07-VICCB.png

Plots of Satellite Surface Reflectance for each satellite versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./VICCB-SR3500-ASD-Locations.png

Comparison of the locations of individual SR3500 (blue) and ASD (black) spectra. Two significant differences
are shown between the datasets: First, the areas traced out by the spectra are not aligned. Second, the footprints
of each spectra, as shown by the size of the circles, are strongly different, meaning that individual spectra are
sampling different parts of the ground. The footprint sizes are 12m for SR3500 and 15cm for ASD.

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
:::{figure} ./FCStats-2026-06-07-VICCB.png
Rows show results for Bare Soil (BS), Non-Photosynthetic Vegetation (NPV), Photosynthetic
Vegetation (PV) and Unmixing Error (UE), respectively. The left column shows the range of FC
values, on a pixel-by-pixel basis, using the satellite data. The middle panels show the 
difference between satellite- and field-derived FC values. The right panels show a histogram
of differences, together with summary statistics for the field site.

:::
::::
::::{grid-item}
:::{figure} ./FC-2026-06-07-VICCB.png

The four panels show FC values for today (blue) and previous (black) field site measurements.
The solid line represents that one-to-one equality between field and satellite measurements.
Error bars are shown with today's data, which represent the variation in the pixel values over
the field site.

:::
::::
:::::
    


% :::{tags} validation, site_validation, landsat_8_validation, sentinel_2_validation
% :::
    
