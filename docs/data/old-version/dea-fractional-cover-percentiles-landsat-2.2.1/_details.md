## Background

The Fractional Cover 2 (Landsat) product, developed by the Joint Remote Sensing Research Program, provides information about the the proportions of:

* Green vegetation
* Non-green vegetation (including deciduous trees during autumn and dry grass)
* Bare areas for every 25m x 25m ground footprint

It provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.

It is important to be able to analyse and interpret fractional cover. For example, the 90th percentile of bare soil for a particular year will identify areas that have experienced a high portion of bare soil during that year.

## What this product offers

This product is designed to make it easier to analyse and interpret fractional cover. It uses the Fractional Cover 2 (Landsat) product and calculates the statistical summaries (10th, 50th and 90th percentile) of fractional cover per epoch (whole-of-archive-summary, annual, seasonal).

This product is available in the following forms:

:::{list-table}

* - **FC-PERCENTILE-SUMMARY**
  - This contains a (10th, 50th and 90th percentile) of bare, green and non-green vegetation of all observations contained within the DEA (from 1987 to the most up to date imagery available).
* - **FC-PERCENTILE-ANNUAL-SUMMARY**
  - This contains a (10th, 50th and 90th percentile) of bare, green and non-green vegetation of observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
* - **FC-PERCENTILE-SEASONAL-SUMMARY**
  - This contains a (10th, 50th and 90th percentile) of bare, green and non-green vegetation of observations acquired within each calendar season (DJF, MAM, JJA, SON).  This product is available for the most recent 8 seasons.
:::

% ## Data description

## Applications

This product provides valuable information for a range of environmental and agricultural applications, including:
* Soil erosion monitoring
* Land surface process modelling
* Land management practices (e.g. crop rotation, stubble management, rangeland management)
* Vegetation studies
* Fuel load estimation
* Ecosystem modelling

## Technical information

This product provides continental composites for each cover fraction.

The percentile ranges for each compositing period can be used to identify the 'greenest' observation i.e. 90th percentile of green cover and 'barest' observation i.e. 90th percentile of bare soil that occurred within the compositing period.

The 10th and 90th percentile are used in preference to the minimum and maximum values because they are less prone to residual noise associated with undetected cloud/cloud shadow. The 50th percentile (median) are used in preference to the mean as the median is less prone to being skewed by extreme values. It is worth noting that some undetected cloud and cloud shadow artefacts may still be present in the 10th and 90th percentiles, especially in areas with frequent cloud cover such as the wet tropics and Tasmania.

To account for satellite availability and status the statistics are calculated using the following satellites for the following periods of time:

:::{list-table}

* - **1987&ndash;1998**
  - Landsat 5
* - **1999**
  - Landsat 5 and Landsat 7
* - **2000&ndash;2002**
  - Landsat 7
* - **2003**
  - Landsat 5 and Landsat 7
* - **2004&ndash;2010**
  - Landsat 5
* - **2011&ndash;2012**
  - Landsat 7
* - **2013 onward**
  - Landsat 8

:::

The values for this product are scaled as follows:  
For the fractional cover bands (PV, NPV, BS)  
0-100 = fractional cover values that range between 0 and 100%

Due to model uncertainties and the limitations of the training data, some areas may show cover values in excess of 100%. These areas can either be excluded or treated as equivalent to 100%

For the unmixing error (UE) band, the values are scaled between 0 and 127  High unmixing error values represent areas of high model uncertainty (areas of water, cloud, cloud shadow or soil types/colours that were not included in the model training data).

## Lineage

Nationally consistent information about fractional cover dynamics is essential to addressing a range of natural resource challenges. These include land management practices, air quality, soil erosion, rangeland condition and soil carbon dynamics.

The fractional cover algorithm was developed by the Joint Remote Sensing Research Program (JRSRP) and is described in Scarth et al. (2010). While originally calibrated in Queensland, a large collaborative effort between The Department of Agriculture - ABARES and State and Territory governments to collect additional calibration data has enabled the calibration to extend to the entire Australian continent.

FC was made possible by new scientific and technical capabilities, the collaborative framework established by the Terrestrial Ecosystem Research Network (TERN) through the National Collaborative Research Infrastructure Strategy (NCRIS), and collaborative effort between state and Commonwealth governments.

The long term acquisition plan supported by the Landsat program, in combination with Geoscience Australia's longstanding investment in the on-ground infrastructure required to capture Landsat imagery has made this product possible. Geoscience Australia's partnership with the National Computing Infrastructure facilities in conjunction with the development of the Australian Geoscience Data Cube - a high performance data framework - makes it possible to analyse the continental archive of fractional cover data.

FC-PERCENTILE provides a consistent summary of fractional cover which will be an important foundation for land cover mapping and monitoring across Australia. It is a resource for natural resource managers, land surface process modellers, carbon modellers, rangeland managers, ecosystem scientists and policy makers.

## Processing steps

Fractional Cover (FC) provides a representation of the proportions of living vegetation, dry and dying vegetation (including deciduous trees during autumn, dying grass, etc.), and bare soils across the Australian continent for any point in time in the Landsat archive since 1987. FC can potentially provide insight into areas of dry/dying vegetation and/or bare soil as well as allowing the mapping of living vegetation extent.

Fractional cover data can be used to identify large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land management practices and rangeland condition. This information could enable policy agencies, natural and agricultural land resource managers, and scientists to monitor land conditions over large areas over long time frames.

The Fractional Cover (FC) algorithm was developed by the Joint Remote Sensing Research Program and is described in described in Scarth et al. (2010). It has been implemented by Geoscience Australia for every observation from Landsat Thematic Mapper (Landsat 5), Enhanced Thematic Mapper (Landsat 7) and Operational Land Imager (Landsat 8) acquired since 1987. It is calculated from surface reflectance data.

FC provides a fractional cover representation of the proportions of green or photosynthetic vegetation, non-photosynthetic vegetation, and bare surface cover across the Australian continent. The fractions are retrieved by inverting multiple linear regression estimates and using synthetic endmembers in a constrained non-negative least squares unmixing model.

% ## Software

## References

Flood, N. (2014). Continuity of reflectance data between Landsat-7 ETM+ and Landsat-8 OLI, for both top-of-atmosphere and surface reflectance: A study in the Australian landscape. *Remote Sensing*, *6*(9), 7952–7970. [https://doi.org/10.3390/rs6097952](https://doi.org/10.3390/rs6097952)

Muir, J., Schmidt, M., Tindall, D., Trevithick, R., Scarth, P. and Stewart, J.B. (2011). Guidelines for field measurement of fractional ground cover: a technical handbook supporting the Australian Collaborative Land Use and Management Program. *Queensland* *Department of Environment and Resource Management for the Australian Bureau of* *Agricultural and Resource Economics and Sciences*. 

Scarth, P., Roder, A. and Schmidt, M. (2010). Tracking grazing pressure and climate interaction - the role of Landsat fractional cover in time series analysis. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*

Schmidt, M., Denham, R. and Scarth, P. (2010), Fractional ground cover monitoring of pastures and agricultural areas in Queensland. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*
