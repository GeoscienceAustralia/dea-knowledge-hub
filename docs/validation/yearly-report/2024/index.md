# 2024: DEA Yearly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::

## Executive Summary

This Yearly report summarises validation for DEA surface reflectance products for 2024
and presents aggregate validation results to the end of this year.

* During this year, a total of 9 measurements were taken across 6 field sites, to capture 10 overpasses.
* Validation of all platforms improved in accuracy, taking into account the data from this year.
* On an averaged band-by-band basis, Landsat 8 is validated to 2.3%, Landsat 9 is validated to 11.5%, Sentinel-2A is validated to 2.1% and Sentinel-2B is validated to 2.5%.

## Introduction

This yearly report presents a summary of results from 2024 from the Digital Earth
Calibration/Validation team. The report is presented in the following sections:

* Background &mdash; this section outlines the context around this work, with particular attention paid ton historical work leading up to this year.
* Summary of Validation Work &mdash; this section provides an overall view of the field site measurements undertaken.
* Comments on Individual Sites of Interest &mdash; this section focuses on any sites where some aspect of the site or measurement was atypical.
* Summary of Band-by-Band Matching &mdash; this section presents comparison data for this year’s results, in the context of all previous results.
* Comments on How This Year’s Work Has Affected Combined Validation Results &mdash; this section discusses how the average results for each sensor have changed with the introduction of new validation data this year. All band data for each platform is combined to show averaged validation results.

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

6 sites were measured, with 9 individual field site captures. The Table below summarises these captures.

:::{csv-table} Summary of field site captures
:header-rows: 1

"Site capture (Date, Field site, Overpasses)","Latitude, Longitude (WGS84)","Instrument","Comments"
"<a href='/validation/site-report/2024-04-16-MUL/'>2024-04-16 MUL: S-2B</a>","-35.122799, 148.862583","Hand-held ASD FR-4","Excellent matchup"
"<a href='/validation/site-report/2024-05-21-MUL/'>2024-05-21 MUL: S-2A</a>","-35.123887, 148.862833","Hand-held ASD FR-4","Poor matchup"
"<a href='/validation/site-report/2024-06-30-SA1/'>2024-06-30 SA1: L8</a>","-32.175007, 140.640833","Hand-held SR-3500","Excellent matchup"
"<a href='/validation/site-report/2024-07-02-NSW2/'>2024-07-02 NSW2: L8</a>","-31.595245, 143.480953","Hand-held SR-3500","Good matchup"
"<a href='/validation/site-report/2024-07-02-NSW3/'>2024-07-02 NSW3: L8</a>","-31.521237, 145.478554","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2024-07-03-NSW3/'>2024-07-03 NSW3: L9/S-2A</a>","-31.521239, 145.478625","Hand-held ASD FR-4","Both excellent matchups"
"<a href='/validation/site-report/2024-07-04-NSW4/'>2024-07-04 NSW4: L8</a>","-31.527603, 146.977497","Hand-held SR-3500","Good matchup"
"<a href='/validation/site-report/2024-07-04-NSW5/'>2024-07-04 NSW5: L8</a>","-32.209803, 148.210464","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2024-07-05-NSW5/'>2024-07-05 NSW5: L9</a>","-32.209824, 148.210429","Hand-held ASD FR-4","Excellent matchup"
:::
 
:::{figure} ./2024_Locations.png

The Figure shows the locations of the field sites measured during this year.
::: 

## Comments on Individual Sites of Interest

No sites of particular interest.
     
## Summary of Band-by-Band Matching

:::{figure} ./2024-Matchup.png

The Figure shows comparison data for each platform. Black dots represent data that were collected prior to this year.
Coloured symbols represent data that were collected during this year. The diagonal line in each panel shows the
one-to-one correspondence between field and satellite data. Note that this diagonal line does NOT show the line of best
fit. It is plotted this way to highlight any trends where the data may be biased away from the line of one-to-one
correspondence. The statistics in the bottom-right corner of each panel provide details for the line of best fit
through all points up to and including this year’s data.
:::

The Table below lists overall validation results. These are based on the standard deviation of the scatter that we find
for each band of each sensor. This is when taking all the validation results together, up to and including this year’s
results. The band-by-band scatter is representative of the validation performance of each band. Rather than providing
values for each individual band, we characterise all results by looking at the mean and maximum scatter for each
platform.

:::{csv-table} Validation Results
:header-rows: 1

"Satellite platform","Mean band-by-band scatter","Maximum band-by-band scatter"
"Landsat 8","2.3%","2.9%"
"Landsat 9","11.5%","16.9%"
"Sentinel-2A","2.2%","2.7%"
"Sentinel-2B","2.5%","4.5%"
:::

For example, the Table shows that each Landsat 8 band is typically validated to 2.3%, with the worst performance
of a band being 2.9%. Note that there is much larger scatter for Landsat 9, indicating higher uncertainty in validation.
This is because Landsat 9 is a newer platform, with fewer validation matchups.

## Effect on Cumulative Validation Results

This section discusses the effect that this year’s validation results have had on the total validation
results over all time.

For Landsat 8, this year has seen an overall improvement in validation results. There were 5 field site comparison
measurements.

For Landsat 9, this year has seen an overall improvement in validation results. There were 2 field site comparison
measurements.

For Sentinel-2A, this year has seen an overall improvement in validation results. There were 2 field site comparison
measurements.

For Sentinel-2B, this year has seen an overall improvement in validation results. There was 1 field site comparison
measurement.

## Acknowledgments
 
The field validation data were collected by Geoscience Australia. 

