# 2025-06-21 NSW4: Transect NSW Site 4, Landsat 8 overpass

This is a report of the field data collected on 21 June 2025 at the location of Transect NSW Site 4
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
"Time of field site measurements (UTC)","2025-06-21 00:12:39 to 2025-06-21 00:46:03"
"Time of overpass (UTC)", 2025-06-21 00:01:33
"GPS quality","Good"
"Reference position","146.97836667E, 31.52713S (WGS84)"
"Matchup quality","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets that use the same standardised bands.

```{eval-rst}
.. container:: 

   :download:`Download results as CSV <./SiteValidationResults-2025-06-21-NSW4.csv>`
```

:::{csv-table} Results of Field data versus Landsat 8 Satellite
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.034","0.004","0.045","0.008"
"blue","0.044","0.005","0.053","0.011"
"green","0.077","0.007","0.083","0.014"
"red","0.095","0.011","0.1","0.021"
"NIR","0.284","0.012","0.275","0.027"
"SWIR1","0.248","0.017","0.273","0.032"
"SWIR2","0.16","0.016","0.178","0.03"
"CA","0.034","0.003","0.042","0.003"
"blue","0.045","0.004","0.052","0.004"
"green","0.09","0.009","0.101","0.009"
"red","0.172","0.018","0.183","0.028"
"NIR","0.277","0.017","0.284","0.021"
"SWIR1","0.411","0.044","0.442","0.043"
"SWIR2","0.359","0.041","0.389","0.052"
:::

## Figures

The following figures provide visual representations of the data. (Click a figure to view it at full size.)

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2025-06-21-NSW4.png

A satellite imagery tile of true colour (RGB) surface reflectance.
It covers an area of approximately 2&nbsp;km &times; 2&nbsp;km.
The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./SiteComparison-2025-06-21-NSW4.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation
of pixel values over and surrounding the field site.
Field uncertainty error bars are the standard deviation of values after
averaging all spectra within the same satellite pixels.

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2025-06-21-NSW4.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date.
The line of best fit is not shown, but its parameters are given in the bottom-right corner.

:::
::::
:::::

% :::{tags} validation, site_validation, mullion_validation, landsat_8_validation
% :::
    