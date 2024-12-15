# 2024 Q3: DEA Quarterly Validation Report

:::{contents} In this report
:local:
:backlinks: none
:::


## Executive Summary

This Quarterly report summarises validation for DEA surface reflectance products for quarter 3 (July-September), 2024
and presents aggregate validation results to the end of this quarter.

<UL>
  <LI>During this quarter, 6 field sites were measured 9 times and can be matched to 11 overpasses.</LI>
  <LI>Validation of Landsat 8 and 9 and Sentinel-2A all improved in accuracy, taking into account the data from this
      quarter.</LI>
  <LI>Validation of Sentinel-2B degraded slightly, which is likely because the only site measurement matched to a
      Sentinel-2B overpass was over a challenging site with complex terrain and surface morphology.</LI>
  <LI>On an averaged band-by-band basis, Landsat 8 is validated to 2.4%, Landsat 9 is validated to 13.4%, Sentinel-2A
      is validated to 2.2% and Sentinel-2B is validated to 2.6%.</LI>
</UL>



## Introduction

This quarterly report presents a summary of results from Q3 2024 (July-September) from the Digital Earth
Calibration/Validation team. The report is presented in the following sections:

<UL>
  <LI>Background outlines the context around this work, with particular attention on historical work leading up to this
      quarter.</LI>
  <LI>Summary of Validation Work presents an overall picture of the field site measurements undertaken in a table and
      map.</LI>
  <LI>Comments on Individual Sites of Interest focuses on any sites where some aspect of the site or measurement was
      atypical.</LI>
  <LI>Summary of Band-by-Band Matching presents comparison data for this quarter’s results, in the context of all
      previous results.</LI>
  <LI>Comments on How This Quarter’s Work Has Affected Combined Validation Results discusses how the average results
      for each sensor have changed with the introduction of new validation data from this quarter. This section combines
      all band data for each platform to show averaged validation results.</LI>
</UL>

The Q3, 2024 validation report includes field site measurements that were captured as part of the winter transect work
across South Australia and New South Wales. Note that one field site measurement for SA1 is part of the Q2 2024
validation report and not shown here. No other field site measurements were conducted during this quarter.
 

## Background

The Digital Earth branch within Geoscience Australia offers a suite of Earth observation products, based on data from
both Landsat and Sentinel platforms. The core products are Landsat 8 and 9 and Sentinel-2A and -2B surface reflectance
(SR). To deliver these products with surety, the Calibration and Validation (Cal/Val) team perform vicarious validation
by measuring field sites with hand-held or Unstaffed Aerial Vehicle (UAV, commonly known as drones)-based equipment
close to the time of an overpass. This work began with Phase 1, where measurements were performed by multiple groups
across continental Australia. Full details on the results and methodology can be found in the Phase 1 report.

Data for both SR products and from field site measurements are made freely available. For SR products, you can visualise
the data at DEA Maps, or for a more in-depth understanding and direct access to data, please visit the DEA Data and
Products page. Field measurement data are made available through the National Spectral Database.

As more field sites are measured and as newer measurements are made over the same field sites, the overall validation of
SR products becomes more accurate. The purpose of this report is to provide an up-to-date status of validation accuracy,
based on the most recent measurements.
 
## Summary of Validation Work

6 sites were measured, with 9 individual field site captures. The table below summarises these captures:

:::{csv-table} Summary of field site captures
:header-rows: 1

"Date","Field Site","Overpass (Link to site report)","Longitude, Latitude (WGS84)","Instrument","Comments"
"2024-07-01","NSW1","L9, S-2B","142.10368, -31.81348","Hand-held ASD FR-4","Both satellites affected by cloud – validation data not used."
"2024-07-02","NSW2","L8","143.48095, -31.59525","Drone mounted SR-3500","Good matchup"
"2024-07-02","NSW3","L8","145.47855, -31.52124","Hand-held ASD FR-4","Good matchup"
"2024-07-03","NSW3","L9, S-2A","145.47862, -31.52124","Hand-held ASD FR-4","Good matchup"
"2024-07-04","NSW4","L8","146.97750, -31.52760","Drone mounted SR-3500","Good matchup"
"2024-07-04","NSW5","L8","148.21046, -32.20980","Hand-held ASD FR-4","Good matchup"
"2024-07-05","NSW5","L9","148.21043, -32.20982","Hand-held ASD FR-4","Good matchup"
"2024-07-05","NSW6","L9, S-2B","150.02628, -30.78773","Drone mounted SR-3500","Clouds nearby for S-2B overpass but both overpasses show a good matchup. Field site shows a significant slope and is partially over tree canopy."
"2024-07-06","NSW6","L8","150.02628, -30.78777","Drone mounted SR-3500","Good matchup. Field site shows a significant slope and is partially over tree canopy."
:::
 
:::
:::{figure} ./2024Q3_Locations.png

The Figure shows the locations of the field sites measured in this quarter.
::: 

## Comments on Individual Sites of Interest

<B>NSW6 field site</B>, also known as Boggabri, is situated on the slope of a hill, which rises about 200m over a length of
around 700m. The bottom of the hill is situated within a canola field, However, the field site is located along the
slope of the hill, which is covered with native vegetation, mainly comprising of trees. This site was specifically
selected to be more challenging than typical field sites due to the slope of the hill and the presence of the tree
canopy.

:::
:::{figure} ./2024Q3-Boggabri1.png

The Figure shows NSW6 field site (blue square), in the context of the surrounding area. The bottom panel of the Figure
shows the elevation profile of the hill, following along the white line drawn in the upper panel.
:::

:::
:::{figure} ./2024Q3-Boggabri2.jpg
{figure} ./2024Q3-Boggabri3.jpg
{figure} ./2024Q3-Boggabri4.jpg

The Figure shows three images taken by the drone during flight on 6 July 2024, showing the transition between cultivated
field and native area (left) and examples of tree canopy in the field site area (middle and right). This Figure
highlights the challenges of validating the site, where the surface reflectance properties vary strongly and individual
sight lines may land on tree canopy, shadow or somewhere in between.
:::
     
## Summary of Band-by-Band Matching

:::
:::{figure} ./2024Q3-Matchup.png

The Figure shows comparison data for each platform. Black dots represent data that were collected prior to this quarter.
Coloured symbols represent data that were collected in this quarter. The diagonal line in each panel shows the
one-to-one correspondence between field and satellite data. Note that this diagonal line does NOT show the line of best
fit. It is plotted this way to highlight any trends where the data may be biased away from the line of one-to-one
correspondence. Statistics, given in the bottom right-hand corner of each panel, show details for the line of best fit
through all points up to and including this quarter’s data.

The table below lists overall validation results. These are based on the standard deviation of the scatter that we find
for each band, for each sensor, when taking all the validation results together, up to, and including, this quarter’s
results. The band-by-band scatter is representative of the validation performance of each band. Rather than providing
values for each individual band, we characterise all results by looking at the mean and maximum scatter for each
platform.

:::{csv-table} Validation Results
:header-rows: 1

"Satellite Platform","Mean band-by-band scatter","Maximum band-by-band scatter"
"Landsat 8","2.4%","3.1%"
"Landsat 9","13.4%","35.9%"
"Sentinel-2A","2.2%","2.7%"
"Sentinel-2B","2.6%","4.4%"
:::

The Table indicates that, for example, each Landsat 8 band is validated to typically 2-3%, with the worst band
performance being 3.1%. Note that there is much larger scatter (ie. uncertainty in validation) for Landsat 9. This is
because there have been fewer field site measurements to coincide with the relatively new Landsat 9 platform.
 

## Effect on Cumulative Validation Results

This section discusses the effect that this quarter’s validation results have made on the total all-time validation
results.

For Landsat 8, this quarter has seen an overall improvement in validation results. There were 5 field site comparison
measurements. The NIR band for NSW6 on 6 July, 2024 stands out as below the line of equality. This is the Boggabri field
site, where there is a significant slope to the site, as well as strongly changing surface reflectance within the field
site. A BRDF correction to the slope has not yet been applied to the SR-3500 data (expected to be done in Q1, 2025),
which may also contribute to the discrepancy. Overall, the field data for Landsat 8 overpasses continue to improve the
validation reliability, where the statistics indicate that, with all bands taken together, Landsat 8 data can be relied
upon to around 1% of the surface reflectance. 

For Landsat 9, this quarter has seen an overall improvement in validation results. There were 4 field site comparison
measurements. Again, the NIR band for NSW6 on 5 July, 2024 stands out as below the line of equality. This is the
Boggabri field site, where there is a significant slope to the site, as well as strongly changing surface reflectance
within the field site. A BRDF correction to the slope has not yet been applied to the data, which may also contribute to
the discrepancy. Overall, the field data for Landsat 9 overpasses continue to improve the validation reliability, where
the statistics indicate that, with all bands taken together, Landsat 9 data can be relied upon to around 2% of the
surface reflectance. The larger uncertainty of Landsat 9, when compared to Landsat 8 above, is most likely due to few
overall field site comparisons with the newer Landsat 9 OLI2 sensor.

For Sentinel-2A, this quarter has seen an overall improvement in validation results. There was 1 field site comparison
measurement at NSW3 on 3 July, 2024. This measurement shows an excellent match. Overall, the field data for Sentinel-2A
overpasses continue to improve the validation reliability, where the statistics indicate that, with all bands taken
together, Sentinel-2A data are consistently within around 1% of the surface reflectance. 

For Sentinel-2B, this quarter has seen an overall degradation in validation results. There was 1 field site comparison
measurement at NSW6 on 5 July, 2024. This measurement is the Boggabri field site, where there is a significant slope to
the site, as well as strongly changing surface reflectance within the field site. A BRDF correction to the slope has not
yet been applied to the data, which may also contribute to the discrepancy. Overall, the field data for Sentinel-2B in
this quarter has slightly degraded validation performance, where the statistics indicate that, with all bands taken
together, Sentinel-2B data can be relied upon to around 1% of the surface reflectance. 

 
## Acknowledgments 
 
The field validation data were collected by Geoscience Australia. 


