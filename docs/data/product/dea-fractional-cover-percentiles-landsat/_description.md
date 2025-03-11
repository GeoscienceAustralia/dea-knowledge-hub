## Background

The Fractional Cover (Landsat) product, developed by the Joint Remote Sensing Research Program, provides information about the the proportions of:

* Green vegetation
* Non-green vegetation (including deciduous trees during autumn and dry grass)
* Bare areas for every 30m x 30m ground footprint. It provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.

Fractional Cover Percentiles (Landsat) estimate the 10th, 50th, and 90th percentiles independently for the green vegetation, non-green vegetation, and bare soil fractions observed in each calendar year.

Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. Because the percentiles are estimated independently for the three cover types, the 10th percentiles represent the low end of the measurements for the three covers, which may have been observed at different times of a year. Similarly, the 90th percentiles represent the high end of the measurements for the three covers, which may have occurred at different times.

The 10th, 50th, and 90th percentiles represent low, median and high values in a distribution that are robust against outliers. These values can be used separately or combined to understand the land cover dynamics. For example, the three percentiles for the green cover fraction can serve as proxies for the minimum, typical and maximum green cover for a given year. Difference between the 10th and 90th percentiles provides an estimate of the magnitude of change within a year. A large range of values may be observed in the agricultural land for all cover types while high green cover and a small difference between 10th and 90th percentiles are expected for forest cover.

A representative view of the landscape in a year can be obtained by combining the 50th percentiles, or the median values, for the three cover types.

## What this product offers

This product is designed to make it easier to analyse and interpret fractional cover. It uses the Fractional Cover (Landsat) product and calculates the statistical summaries (10th, 50th and 90th percentile) of fractional cover per epoch (annual).

It includes cloud and cloud shadow buffering with a size of 6 pixels. This buffering is applied to Landsat 5, Landsat 7, Landsat 8, and Landsat 9 data.

% ## Data description

## Applications

This product provides valuable information for a range of environmental and agricultural applications, including:
* soil erosion monitoring
* land surface process modelling
* land management practices (e.g. crop rotation, stubble management, rangeland management)
* vegetation studies
* fuel load estimation
* ecosystem modelling

## Technical information

### FC-PERCENTILE-ANNUAL-SUMMARY

This contains a (10th, 50th and 90th percentile) of bare, green and non-green vegetation of observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

This product provides continental composites for each cover fraction.

The percentile ranges for each compositing period can be used to identify the 'greenest' observation i.e. 90th percentile of green cover and 'barest' observation i.e. 90th percentile of bare soil that occurred within the compositing period.

The 10th and 90th percentile are used in preference to the minimum and maximum values because they are less prone to residual noise associated with undetected cloud/cloud shadow. The 50th percentile (median) are used in preference to the mean as the median is less prone to being skewed by extreme values. It is worth noting that some undetected cloud and cloud shadow artefacts may still be present in the 10th and 90th percentiles, especially in areas with frequent cloud cover such as the wet tropics and Tasmania.

To account for satellite availability and status the statistics are calculated using the following satellites for the following periods of time:
* 1987-1998 : Landsat 5 only
* 1999 : Landsat 5 and Landsat 7
* 2000-2002 : Landsat 7 only
* 2003 : Landsat 5 and Landsat 7
* 2004-2010 : Landsat 5 only
* 2011-2012 : Landsat 7 only
* 2013-2021 : Landsat 8 only
* 2022 onwards: Landsat 8 and Landsat 9

The values for this product are as follows:

* For the fractional cover bands (PV, NPV, BS)
* 0-100 = fractional cover values that range between 0 and 100%

### Quality Assurance:

This layer provides a breakdown of each FCP pixel between,

* sufficient observations
* insufficient observations dry
* insufficient observations wet

For insufficient observations, these are pixels that have been masked out of the percentiles results e.g. NODATA, and provides an explanation as to why they have been masked out.

### Each product’s datasets will:

* be divided into tiles of 3200 x 3200 pixels, with a pixel size of 30m^2
* be presented in EPSG:3577

### Fractional Cover Masking

DEA Water Observations are used to identify clear pixels from DEA Fractional Cover to be included in percentile calculation. A Fractional Cover observation is included if:
* It has corresponding DEA Water Observation information. If an observation within DEA Fractional Cover has no corresponding Water Observation, it is discarded. This can happen for ARD scenes that have a geometric quality assessment of greater than one, which occurs when there is poor geometric quality.
* The DEA Water Observation has the following characteristics:
  * It is contiguous (data for all bands is present and valid)
  * It is not saturated
  * It is not cloud
  * It is not cloud shadow
  * It is not terrain shadow
  * It is not low solar angle
  * It can be high slope
  * It is not wet
  * There are at least 3 clear and dry observations for the time period.
* Please note, no land/sea masking is applied
* Observation dates for given percentiles are not captured

### Temporal period

Will be calculated from the 1st of January to the 31st of December (inclusive) for every available year of DEA Landsat Collection 3 Water Observations and DEA Landsat Collection 3 Fractional Cover observations.

### It will have a directory structure of form:

`/ga_ls_fc_pc_cyear_3/4-0-0/x25/y41/1999--P1Y/ga_ls_fc_pc_cyear_3_x25y41_1999--P1Y_final_bs_pc_10.tif`

## Lineage

10th, 50th and 90th percentiles are calculated per Fractional Cover measurement - Bare Soil, Photosynthetic Vegetation, Non-Photosynthetic Vegetation. DEA Fractional Cover C3 and DEA Water Observations C3 are used as the input to these products.

## Processing steps

The Fractional Cover Percentile odc-statistician plugin can be found in [Fractional Cover Percentiles Code Repository](https://github.com/opendatacube/odc-stats/blob/develop/odc/stats/plugins/fc_percentiles.py).

The processing steps are:

<div id="processing-steps"></div>

1. Fractional Cover and Water Observations Daily scenes are loaded for the calender year
1. Pixels for each time step are masked out that are not clear and dry or are wet, and a cloud and cloud shadow dilation of 6 pixels is applied 
1. Fractional cover percentiles are calculated - noting results are not filtered by an unmixing error threshold

% ## Software

## References

Flood, N. (2014). Continuity of reflectance data between Landsat-7 ETM+ and Landsat-8 OLI, for both top-of-atmosphere and surface reflectance: A study in the Australian landscape. *Remote Sensing*, *6*(9), 7952–7970. [https://doi.org/10.3390/rs6097952](https://doi.org/10.3390/rs6097952)

Muir, J., Schmidt, M., Tindall, D., Trevithick, R., Scarth, P. and Stewart, J.B. (2011). Guidelines for field measurement of fractional ground cover: a technical handbook supporting the Australian Collaborative Land Use and Management Program. *Queensland* *Department of Environment and Resource Management for the Australian Bureau of* *Agricultural and Resource Economics and Sciences*.

Scarth, P., Roder, A. and Schmidt, M. (2010). Tracking grazing pressure and climate interaction - the role of Landsat fractional cover in time series analysis. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*

Schmidt, M., Denham, R. and Scarth, P. (2010), Fractional ground cover monitoring of pastures and agricultural areas in Queensland. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*

