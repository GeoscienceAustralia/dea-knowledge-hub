# 2023 Q4: DEA Quarterly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::

## Executive Summary

This Quarterly report summarises validation for DEA surface reflectance products for Quarter 4 (October-December) of 2023
and presents aggregate validation results to the end of this quarter.

* During this quarter, a total of 2 measurements were taken across 2 field sites, to capture 3 overpasses.
* Validation of Landsat 8 and 9 and Sentinel-2B all improved in accuracy, taking into account the data from this quarter.
* On an averaged band-by-band basis, Landsat 8 is validated to 2.6%, Landsat 9 is validated to 9.9%, Sentinel-2A is validated to 2.4% and Sentinel-2B is validated to 2.5%.

## Introduction

This quarterly report presents a summary of results from Q4 2023 from the Digital Earth
Calibration/Validation team. The report is presented in the following sections:

* Background &mdash; this section outlines the context around this work, with particular attention paid ton historical work leading up to this quarter.
* Summary of Validation Work &mdash; this section provides an overall view of the field site measurements undertaken.
* Comments on Individual Sites of Interest &mdash; this section focuses on any sites where some aspect of the site or measurement was atypical.
* Summary of Band-by-Band Matching &mdash; this section presents comparison data for this quarter’s results, in the context of all previous results.
* Comments on How This Quarter’s Work Has Affected Combined Validation Results &mdash; this section discusses how the average results for each sensor have changed with the introduction of new validation data this quarter. All band data for each platform is combined to show averaged validation results.

The Q4 2023 validation report includes field site measurements that were captured as part of the first transect work
across South Australia and New South Wales. No other field site measurements were conducted during this quarter.
 
## Background

The Digital Earth branch within Geoscience Australia offers a suite of Earth observation products, based on data from
both Landsat and Sentinel platforms. The core products are Landsat 8 and 9 and Sentinel-2A and -2B surface reflectance (SR).
To deliver these products with confidence, the Calibration/Validation team perform vicarious validation
by measuring field sites with hand-held equipment or an Unstaffed Aerial Vehicle (UAV; commonly known as drone) equipment
close to the time of an overpass. This work began with Phase 1, where measurements were performed by multiple groups
across continental Australia. Full details on the results and methodology can be found in the Phase 1 report.

Data for both SR products and from field site measurements are made freely available. For SR products, you can visualise
the data in [DEA Maps](https://maps.dea.ga.gov.au/), or for a more in-depth understanding and direct access to data, please visit the [DEA Knowledge Hub Data Products section](https://knowledge.dea.ga.gov.au/data/). Field measurement data are made available through the [National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).

As more field sites are measured and as newer measurements are made over the same field sites, the overall validation of
SR products becomes more accurate. The purpose of this report is to provide an up-to-date status of validation accuracy,
based on the most recent measurements.
 
## Summary of Validation Work

2 sites were measured, with 2 individual field site captures. The Table below summarises these captures.

:::{csv-table} Summary of field site captures
:header-rows: 1

"Site capture (Date, Field site, Overpasses)","Latitude, Longitude (WGS84)","Instrument","Comments"
"<a href='/validation/site-report/2023-11-26-SA1/'>2023-11-26-SA1: L8</a>","-32.17493, 140.64202","Hand-held ASD FR-4","Excellent matchup"
"<a href='/validation/site-report/2023-11-27-NSW1/'>2023-11-27-NSW1: L9, S-2B</a>","-31.81354, 142.10370","Hand-held ASD FR-4","Good matchup. Some cloud nearby."
:::
 
:::{figure} ./2023Q4_Locations.png

The Figure shows the locations of the field sites measured in this quarter.
::: 

## Comments on Individual Sites of Interest

No sites of particular interest.
     
## Summary of Band-by-Band Matching

:::{figure} ./2024Q3-Matchup.png

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
"Landsat 8","2.6%","3.3%"
"Landsat 9","9.9%","27%"
"Sentinel-2A","2.4%","2.9%"
"Sentinel-2B","2.5%","4.6%"
:::

For example, the Table shows that each Landsat 8 band is typically validated to 2-3%, with the worst performance
of a band being 3.3%. Note that there is much larger scatter for Landsat 9, indicating higher uncertainty in validation.
This is because there have been fewer field site measurements to coincide with the relatively new Landsat 9 platform.

## Effect on Cumulative Validation Results

This section discusses the effect that this quarter’s validation results have had on the total validation
results over all time.

For Landsat 8, this quarter has seen an overall improvement in validation results. There was 1 field site comparison
measurement.

For Landsat 9, this quarter has seen an overall improvement in validation results. There were 1 field site comparison
measurement.

For Sentinel-2A, this quarter has seen no change in validation results. There were no field site comparison
measurements during this quarter.

For Sentinel-2B, this quarter has seen an overall improvement in validation results. There was 1 field site comparison
measurement.
 
## Acknowledgments
 
The field validation data were collected by Geoscience Australia. 

