# 2023-07-25-MUL: Mullion, Sentinel-2A overpass

This is a report of the field data collected on the 25th of July, 2023 at the location of Mullion
to validate the satellite data of the Sentinel-2A overpass.
The full collection of data is contained in the [National Spectral Database](https://www.dea.ga.gov.au/products/national-spectral-database).
Satellite data can be found on [DEA maps](https://maps.dea.ga.gov.au/).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

These variables and environmental factors were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-07-25 01:10:03 to 2023-07-25 01:58:33"
"Time of overpass (UTC)", 2023-07-26 00:16:32
"GPS quality","Good"
"Reference position","148.86261117E, 35.12279053S (WGS84)"
"Matchup quality","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2023-07-25-MUL.csv>`
```

:::{csv-table} Results of Field data versus Sentinel-2A Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.045","0.002","0.044","0.009"
"blue","0.057","0.005","0.059","0.013"
"green","0.088","0.006","0.092","0.019"
"red","0.105","0.01","0.104","0.026"
"RE1","0.161","0.009","0.152","0.032"
"RE2","0.259","0.014","0.245","0.051"
"RE3","0.278","0.016","0.278","0.058"
"NIR1","0.294","0.019","0.3","0.062"
"NIR2","0.315","0.018","0.314","0.065"
"SWIR2","0.252","0.012","0.292","0.059"
"SWIR3","0.14","0.008","0.166","0.036"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-07-25-MUL.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2023-07-25-MUL.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-07-25-MUL.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    