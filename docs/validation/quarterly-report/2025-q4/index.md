# 2025 Q4: DEA Quarterly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::

## Executive Summary

This Quarterly report summarises validation for DEA surface reflectance products for Quarter 4 (October-December) of 2025
and presents aggregate validation results to the end of this quarter.

* During this quarter, a total of 5 measurements were taken across 5 field sites, to capture 9 overpasses.
* Validation of Landsat 8, 9 and Sentinel-2B all improved. Validation of Sentinel-2C worsened.
* On an averaged band-by-band basis, Landsat 8 is validated to 2.1%, Landsat 9 is validated to 8.2%, Sentinel-2B is validated to 2.3% and Sentinel-2C is validated to 21.1%.

## Introduction

This quarterly report presents a summary of results from Q4 2025 from the Earth Observation
Calibration/Validation team. The report is presented in the following sections:

* Background &mdash; this section outlines the context around this work, with particular attention paid ton historical work leading up to this quarter.
* Summary of Validation Work &mdash; this section provides an overall view of the field site measurements undertaken.
* Comments on Individual Sites of Interest &mdash; this section focuses on any sites where some aspect of the site or measurement was atypical.
* Summary of Band-by-Band Matching &mdash; this section presents comparison data for this quarter’s results, in the context of all previous results.
* Comments on How This Quarter’s Work Has Affected Combined Validation Results &mdash; this section discusses how the average results for each sensor have changed with the introduction of new validation data this quarter. All band data for each platform is combined to show averaged validation results.

## Background

The Digital Earth branch within Geoscience Australia offers a suite of Earth observation products, based on data from
both Landsat and Sentinel platforms. The core products are Landsat 8 and 9 and Sentinel-2B and -2C surface reflectance (SR).
To deliver these products with confidence, the EO Calibration/Validation team perform vicarious validation
by measuring field sites with hand-held equipment or an Unstaffed Aerial Vehicle (UAV; commonly known as drone) equipment
close to the time of an overpass. This work began with Phase 1, where measurements were performed by multiple groups
across continental Australia. Full details on the results and methodology can be found in the Phase 1 report.

Data for both SR products and from field site measurements are made freely available. For SR products, you can visualise
the data in [DEA Maps](https://maps.dea.ga.gov.au/), or for a more in-depth understanding and direct access to data, please visit the [DEA Knowledge Hub Data Products section](https://knowledge.dea.ga.gov.au/data/). Field measurement data are made available through the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).

As more field sites are measured and as newer measurements are made over the same field sites, the overall validation of
SR products becomes more accurate. The purpose of this report is to provide an up-to-date status of validation accuracy,
based on the most recent measurements.
 
## Summary of Validation Work

5 sites were measured, with 5 individual field site captures. The Table below summarises these captures.

:::{csv-table} Summary of field site captures
:header-rows: 1
"Site capture (Date, Field site, Overpasses)","Latitude, Longitude (WGS84)","Instrument","Comments"
"<a href='/validation/site-report/2025-12-03-NSW1/'>2025-12-03 NSW1: L8, S-2B</a>","-31.814046, 142.104200","Hand-held SR-3500","L8: Excellent matchup. S-2B: Good matchup"
"<a href='/validation/site-report/2025-12-03-NSW2/'>2025-12-03 NSW2: L8, S-2B</a>","-31.595985, 143.483040","Hand-held SR-3500","Both excellent matchup"
"<a href='/validation/site-report/2025-12-04-NSW3/'>2025-12-04 NSW3: L9</a>","-31.521335, 145.478526","Hand-held SR-3500","Excellent matchup"
"<a href='/validation/site-report/2025-12-05-NSW4/'>2025-12-05 NSW4: L8, S-2C</a>","-31.527130, 146.978367","Hand-held SR-3500","Both excellent matchup"
"<a href='/validation/site-report/2025-12-08-NSW6/'>2025-12-08 NSW6: L9, S-2C</a>","-30.786570, 150.024613","Hand-held ASD FR-4","Good for Landsat 9, mediocre for Sentinel-2C. Site shows significant (~15\degree) slope."
:::
 
:::{figure} ./2025Q4_Locations.png

The Figure shows the locations of the field sites measured in this quarter.
::: 

## Comments on Individual Sites of Interest

No sites of particular interest.
     
## Summary of Band-by-Band Matching

:::{figure} ./2025Q4-Matchup.png

The Figure shows comparison data for each platform. Black dots represent data that were collected prior to this quarter.
Coloured symbols represent data that were collected in this quarter. The diagonal line in each panel shows the
one-to-one correspondence between field and satellite data. Note that this diagonal line does NOT show the line of best
fit. It is plotted this way to highlight any trends where the data may be biased away from the line of one-to-one
correspondence. The statistics in the bottom-right corner of each panel provide details for the line of best fit
through all points up to and including this quarter’s data.
:::

The Table below lists overall validation results. These are based on the standard deviation of the scatter that we find
for each band of each sensor. This is when taking all the validation results together, up to and including this quarter’s
results. The band-by-band scatter is representative of the validation performance of each band. Rather than providing
values for each individual band, we characterise all results by looking at the mean and maximum scatter for each
platform.

:::{csv-table} Validation Results
:header-rows: 1

"Satellite platform","Mean band-by-band scatter","Maximum band-by-band scatter"
"Landsat 8","2.1%","2.7%"
"Landsat 9","8.3%","12.1%"
"Sentinel-2B","2.3%","3.7%"
"Sentinel-2C","21.1%","44.4%"
:::

For example, the Table shows that each Landsat 8 band is typically validated to 2.1%, with the worst performance
of a band being 2.7%. Note that there is much larger scatter for Landsat 9 and Sentinel-2C, indicating higher uncertainty in validation.
This is because there have been fewer field site measurements to coincide with the relatively new Landsat 9 and Sentinel-2C platforms.

## Effect on Cumulative Validation Results

This section discusses the effect that this quarter’s validation results have had on the total validation
results over all time.

For Landsat 8, this quarter has seen an overall improvement in validation results. There were 3 field site comparison measurements. Overall, the field data for Landsat 8 overpasses continues to improve the validation reliability.

For Landsat 9, this quarter has seen an overall improvement in validation results. There were 2 field site comparison measurements. Overall, the field data for Landsat 9 overpasses continue to improve the validation reliability.

For Sentinel-2B, this quarter has seen an overall improvement in validation results. There were 2 field site comparison measurements. Overall, the field data for Sentinel-2B overpasses continue to improve the validation reliability.

For Sentinel-2C, this quarter has seen an overall degradation in validation results. There were 2 field site comparison measurements. The degradation appears to be largely due to the NSW6 field site measurement and that, since
so few measurements have been made from the relatively new Sentinel-2C platform, a single measurement can have a large effect on overall results.
 
## Acknowledgments
 
The field validation data were collected by Geoscience Australia. 

