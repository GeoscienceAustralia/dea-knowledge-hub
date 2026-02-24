# 2025: DEA Yearly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::

## Executive Summary

This Yearly report summarises validation for DEA surface reflectance products for 2025
and presents aggregate validation results to the end of this year.

* During this year, a total of 21 measurements were taken across 9 field sites, to capture 33 overpasses.
* Validation of all platforms improved in accuracy, taking into account the data from this year. This year also saw the first validation measurement for Sentinel-2C.
* On an averaged band-by-band basis, Landsat 8 is validated to 2.1%, Landsat 9 is validated to 8.2%, Sentinel-2B is validated to 2.3% and Sentinel-2C is validated to 21.1%.

## Introduction

This yearly report presents a summary of results from 2025 from the Digital Earth
Calibration/Validation team. The report is presented in the following sections:

* Background &mdash; this section outlines the context around this work, with particular attention paid ton historical work leading up to this year.
* Summary of Validation Work &mdash; this section provides an overall view of the field site measurements undertaken.
* Comments on Individual Sites of Interest &mdash; this section focuses on any sites where some aspect of the site or measurement was atypical.
* Summary of Band-by-Band Matching &mdash; this section presents comparison data for this year’s results, in the context of all previous results.
* Comments on How This Year’s Work Has Affected Combined Validation Results &mdash; this section discusses how the average results for each sensor have changed with the introduction of new validation data this year. All band data for each platform is combined to show averaged validation results.

## Background

The Digital Earth branch within Geoscience Australia offers a suite of Earth observation products, based on data from
both Landsat and Sentinel platforms. The core products are Landsat 8 and 9 and Sentinel-2A, -2B and -2C surface reflectance (SR).
To deliver these products with confidence, the Calibration/Validation team perform vicarious validation
by measuring field sites with hand-held equipment or an Unstaffed Aerial Vehicle (UAV; commonly known as drone) equipment
close to the time of an overpass. This work began with Phase 1, where measurements were performed by multiple groups
across continental Australia. Full details on the results and methodology can be found in the Phase 1 report.

Data for both SR products and from field site measurements are made freely available. For SR products, you can visualise
the data in [DEA Maps](https://maps.dea.ga.gov.au/), or for a more in-depth understanding and direct access to data, please
visit the [DEA Knowledge Hub Data Products section](https://knowledge.dea.ga.gov.au/data/). Field measurement data are made
available through the
[National Spectral Database](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/national-spectral-database).
An explanation of how to read these reports can be found on the
[Daily Validation Summary Reports](https://knowledge.dea.ga.gov.au/guides/setup/validation/daily-summary-reports/) page.

As more field sites are measured and as newer measurements are made over the same field sites, the overall validation of
SR products becomes more accurate. The purpose of this report is to provide an up-to-date status of validation accuracy,
based on the most recent measurements.
 
## Summary of Validation Work

9 sites were measured, with 21 individual field site captures. The Table below summarises these captures.

:::{csv-table} Summary of field site captures
:header-rows: 1

"Site capture (Date, Field site, Overpasses)","Latitude, Longitude (WGS84)","Instrument","Comments"
"<a href='/validation/site-report/2025-02-07-MUL/'>2025-02-07 MUL: L9, S-2B</a>","-35.122787, 148.86258","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-02-27-MUL/'>2025-02-27 MUL: S-2B</a>","-35.122769, 148.862567","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-03-02-MUL/'>2025-03-02 MUL: L9, S-2B</a>","-35.122697, 148.862573","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-04-03-MUL/'>2025-04-03 MUL: L9, S-2C</a>","-35.122747, 148.862612","Hand-held ASD FR-4","Both Excellent matchup"
"<a href='/validation/site-report/2025-06-16-SA1/'>2025-06-16 SA1: L9</a>","-32.175474, 140.642875","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-06-18-NSW1/'>2025-06-18 NSW1: L9, S-2B</a>","-31.814046, 142.104200","Hand-held ASD FR-4","L9: Good matchup. S-2B: Excellent matchup"
"<a href='/validation/site-report/2025-06-18-NSW2/'>2025-06-18 NSW2: L9</a>","-31.595985, 143.483040","Hand-held SR-3500","Excellent matchup"
"<a href='/validation/site-report/2025-06-19-NSW2/'>2025-06-19 NSW2: L8</a>","-31.596118, 143.483167","Hand-held SR-3500","Excellent matchup"
"<a href='/validation/site-report/2025-06-19-NSW3/'>2025-06-19 NSW3: S-2C</a>","-31.521335, 145.478526","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-06-20-NSW3/'>2025-06-20 NSW3: L8</a>","-31.521348, 145.478564","Hand-held ASD FR-4","Good matchup"
"<a href='/validation/site-report/2025-06-21-NSW4/'>2025-06-21 NSW4: L8</a>","-31.527130, 146.978367","Hand-held SR-3500","Good matchup"
"<a href='/validation/site-report/2025-06-21-NSW5/'>2025-06-21 NSW5: L8</a>","-32.209699, 148.210396","Hand-held ASD FR-4","Excellent matchup"
"<a href='/validation/site-report/2025-06-22-NSW5/'>2025-06-22 NSW5: L9</a>","-32.209718, 148.210447","Hand-held ASD FR-4","Excellent matchup"
"<a href='/validation/site-report/2025-06-22-NSW6/'>2025-06-22 NSW6: L9, S-2C</a>","-30.786570, 150.024613","Hand-held SR-3500","Both excellent matchup. Site shows significant (~15\degree) slope."
"<a href='/validation/site-report/2025-06-23-NSW7/'>2025-06-23 NSW7: S-2C</a>","-30.985918, 151.483177","Hand-held ASD FR-4","Mediocre matchup"
"<a href='/validation/site-report/2025-06-24-NSW8/'>2025-06-24 NSW8: L9, S-2B</a>","-31.083548, 153.037374","Hand-held ASD FR-4 and SR-3500","Site shows significant terrain, being sand dunes. Results not used."
"<a href='/validation/site-report/2025-12-03-NSW1/'>2025-12-03 NSW1: L8, S-2B</a>","-31.814046, 142.104200","Hand-held SR-3500","L8: Excellent matchup. S-2B: Good matchup"
"<a href='/validation/site-report/2025-12-03-NSW2/'>2025-12-03 NSW2: L8, S-2B</a>","-31.595985, 143.483040","Hand-held SR-3500","Both excellent matchup"
"<a href='/validation/site-report/2025-12-04-NSW3/'>2025-12-04 NSW3: L9</a>","-31.521335, 145.478526","Hand-held SR-3500","Excellent matchup"
"<a href='/validation/site-report/2025-12-05-NSW4/'>2025-12-05 NSW4: L8, S-2C</a>","-31.527130, 146.978367","Hand-held SR-3500","Both excellent matchup"
"<a href='/validation/site-report/2025-12-08-NSW6/'>2025-12-08 NSW6: L9, S-2C</a>","-30.786570, 150.024613","Hand-held ASD FR-4","Good for Landsat 9, mediocre for Sentinel-2C. Site shows significant (~15\degree) slope."
:::
 
:::{figure} ./2025_Locations.png

The Figure shows the locations of the field sites measured during this year.
::: 

## Comments on Individual Sites of Interest

No sites of particular interest.
     
## Summary of Band-by-Band Matching

:::{figure} ./2025-Matchup.png

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
"Landsat 8","2.1%","2.7%"
"Landsat 9","8.3%","12.1%"
"Sentinel-2B","2.3%","3.7%"
"Sentinel-2C","21.1%","44.4%"
:::

For example, the Table shows that each Landsat 8 band is typically validated to 2.1%, with the worst performance
of a band being 2.7%. Note that there is much larger scatter for Landsat 9 and Sentinel-2C, indicating higher uncertainty in validation.
This is because there have been fewer field site measurements to coincide with the relatively new Landsat 9 and Sentinel-2C platforms.

## Effect on Cumulative Validation Results

This section discusses the effect that this year’s validation results have had on the total validation
results over all time.

For Landsat 8, this year has seen an overall improvement in validation results. There were 8 field site comparison measurements. Overall, the field data for Landsat 8 overpasses continues to improve the validation reliability.

For Landsat 9, this year has seen an overall improvement in validation results. There were 11 field site comparison measurements. Overall, the field data for Landsat 9 overpasses continue to improve the validation reliability.

For Sentinel-2B, this year has seen an overall improvement in validation results. There were 8 field site comparison measurements. Overall, the field data for Sentinel-2B overpasses continue to improve the validation reliability.

For Sentinel-2C, this year has seen the first validation results, as this platform replaced Sentinel-2A. There were 6 field site comparison measurements.

## Acknowledgments
 
The field validation data were collected by Geoscience Australia. 

