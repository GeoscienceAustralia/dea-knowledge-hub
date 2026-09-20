# 2026 Q2: DEA Quarterly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::

## Executive Summary

This Quarterly report summarises validation for DEA surface reflectance products for Quarter 2 (April-June) of 2026
and presents aggregate validation results to the end of this quarter.

* During this quarter, a total of 7 measurements were taken across 7 field sites, to capture 9 overpasses.
* IMPORTANT NOTE: Both Landsat and Sentinel products were affected by poor correction of the Aerosol Optical Thickness (AOT) for most locations and dates.
This appears to be a limitation on the input AOT data, rather than the model used to generate the products. This manifests as significantly darker
short wavelength bands (CA, blue, green, red) and slightly brighter in other bands. Results for these sites and days will not be included in future work.

## Introduction

This quarterly report presents a summary of results from Q2 2026 from the Earth Observation
Calibration/Validation team. The report is presented in the following sections:

* Background &mdash; this section outlines the context around this work, with particular attention paid to historical work leading up to this quarter.
* Summary of Validation Work &mdash; this section provides an overall view of the field site measurements undertaken.
* Comments on Individual Sites of Interest &mdash; this section focuses on any sites where some aspect of the site or measurement was atypical.
* Discussion of AOT correction &mdash; this section discusses the effects of poorly modelled atmospheric components that affect the poerformance of products, seen in comparison measurements for this quarter.
* Summary of Band-by-Band Matching &mdash; this section presents comparison data for this quarter’s results, in the context of all previous results.
* Comments on How This Quarter’s Work Has Affected Combined Validation Results &mdash; this section discusses how the average results for each sensor have changed with the introduction of new validation data this quarter. All band data for each platform is combined to show averaged validation results.

## Background

The Digital Earth branch within Geoscience Australia offers a suite of Earth observation products, based on data from
both Landsat and Sentinel platforms. The core products are Landsat 8 and 9 and Sentinel-2A, -2B and -2C surface reflectance (SR).
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

7 sites were measured, with 7 individual field site captures. The Table below summarises these captures.

:::{csv-table} Summary of field site captures
:header-rows: 1
"Site capture (Date, Field site, Overpasses)","Latitude, Longitude (WGS84)","Instrument","Comments"
"<a href='/validation/site-report/2026-06-07-VICCB/'>2026-06-07 VICCB: L8, S-2B</a>","-38.361201, 145.174188","Hand-held ASD FR-4 and UAV-borne SR-3500","All mediocre matchup"
"<a href='/validation/site-report/2026-06-08-VICPW01/'>2026-06-08 VICPW01: L8</a>","-38.690533, 146.387495","Hand-held ASD FR-4","Mediocre matchup"
"<a href='/validation/site-report/2026-06-08-VICPWL/'>2026-06-08 VICPWL: L8</a>","-38.699936, 146.45075","UAV-borne SR3500","Excellent* matchup"
"<a href='/validation/site-report/2026-06-08-VICPWS/'>2026-06-08 VICPWS: L8</a>","-38.699916, 146.450667","UAV-borne SR3500","Excellent* matchup"
"<a href='/validation/site-report/2026-06-11-VICSRV/'>2026-06-11 VICSRV: S-2A, S-2B</a>","-36.376772, 140.970136","Hand-held ASD FR-4","Excellent matchup for S-2A, good matchup for S-2B"
"<a href='/validation/site-report/2026-06-11-VICWAR1/'>2026-06-11 VICWAR1: L8</a>","-38.321963, 145.189983","UAV-borne SR3500","Good* matchup"
"<a href='/validation/site-report/2026-06-11-VICWAR2/'>2026-06-11 VICWAR2: L8</a>","-38.321976, 145.189983","UAV-borne SR3500","Good* matchup"
:::

* The quality of the matchups may appear to be artificially inflated because matchup quality is based on the number of bands where "error bars" overlap.
However, the error bars are also a representation of the variability in SR from the spectra within the site, so these error bars will naturally appear
large for inhomogeneous sites, increasing the chance of overlap with satellite measurements.
 
:::{figure} ./2026Q2_Locations.png

The Figure shows the locations of the field sites measured in this quarter.
::: 

## Comments on Individual Sites of Interest

**VICCB - Cerberus** This site is an open grass field. It was the first time that the SR3500 spectroradiometer was used to fully sample a field site, when
mounted on an UAV. This site was also walked with the ASD, although there is a slight mismatch between the two one-hectare sites, as shown below:

:::{figure} ./VICCB-Footprints.png

The Figure shows the locations of each spectrum for ASD (black circles) and SR3500 (blue circles). Note that the size of the circles represents the footprint,
or the area of ground that each spectrum is gathered from. Because the ASD spectra are gathered from such a small area (approximately 15cm in diameter), they
appear as black dots, compared to the much larger SR3500 circles (approximately 12m in diameter). This Figure shows that the orientation of the two sites are
not aligned, which means that a direct comparison between the two must be treated with caution. Nevertheless, a band-by-band comparison of ASD and SR3500
spectra is shown below:

:::{figure} ./VICCB-ASD-SR3500.png
     
**VICPW - Port Welshpool Long and Short** This site is an extended intertidal zone that was measured close to low tide, using the UAV-mounted SR3500.
Two flights were used to measure two adjacent areas. The first area - VICPW Long - was 1km long and consisted of two transects, separated by 12m. The
second area - VICPW Short - was 500m long and consisted of four transects, separated by 12m, as shown below:

:::{figure} ./VICPW-Map.png
     
In the figure, the blue lines show the location of VICPW Long and the yellow lines show the location of VICPW Short.

## Summary of Band-by-Band Matching

:::{figure} ./2026Q2-Matchup.png

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
"Landsat 8","2.4%","3.2%"
"Landsat 9","6.8%","10.9%"
"Sentinel-2B","3.5%","7.3%"
"Sentinel-2C","17.3%","34.7%"
:::

For example, the Table shows that each Landsat 8 band is typically validated to 2.4%, with the worst performance
of a band being 3.2%. Note that there is much larger scatter for Landsat 9 and Sentinel-2C, indicating higher uncertainty in validation.
This is because there have been fewer field site measurements to coincide with the relatively new Landsat 9 and Sentinel-2C platforms.

## Effect on Cumulative Validation Results

This section discusses the effect that this quarter’s validation results have had on the total validation
results over all time.

For Landsat 8, this quarter has seen an overall degradation in validation results. There was 1 field site comparison measurement. Overall, the field data for Landsat 8 overpasses has degraded the validation reliability.

For Landsat 9, this quarter has seen an overall improvement in validation results. There was 1 field site comparison measurement. Overall, the field data for Landsat 9 overpasses continue to improve the validation reliability.

For Sentinel-2B, this quarter has seen no change in validation results. There were no field site comparison measurements.

For Sentinel-2C, this quarter has seen an overall improvement in validation results. There was 1 field site comparison measurement. Overall, the field data for Sentinel-2C overpasses continue to improve the validation reliability.
 
## Fractional Cover Validation

::::{grid} 2

:::{grid-item}
:::{figure} ./FCSummary-L8.png
:width: 100%
:::
:::

:::{grid-item}
:::{figure} ./FCSummary-L9.png
:width: 100%
:::
:::

::::

The above Figures show a comparison of this Quarter's validation data (shown in blue) vs. previous data (black) for Landsat 8 and 9. The diagonal dashed lines show the one-to-one
correspondence and NOT the line of best fit between the points. The line of best fit is represented by the parameters shown in the bottom-right of each panel, including $R^2$ correlation
coefficient, slope, intercept and standard deviation. Blue points, which include data for this Quarter, also show uncertainty error bars. Black dots represent data that were collected
prior to this Quarter. For each Figure, panels show the four Fractional Cover (FC) parameters: Bare Soil (BS, top-left), Non-Photosynthetic Vegetation (NPV, top-right), Photosynthetic
Vegetation (PV, bottom-left) and Unmixing Error (UE, bottom-right).

Note that the Fractional Cover (FC) comparison does not compare results with a 'ground truth', but is a comparison of derived FC parameters based on satellite SR (vertical axis) and field
SR (horizontal axis).

## Acknowledgments
 
The field validation data were collected by Geoscience Australia. 

