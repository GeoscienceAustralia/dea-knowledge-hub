## Background

Understanding the amount of surface water in the landscape is important for many applications including water management, wetlands, water connectivity, surface-groundwater relationships and flood mapping. This can lead to more effective emergency management and risk assessment.

This product is the implementation of the DEA Water Observations (DEA WO) product (previously known as Water Observations from Space, or WOfS) on the Geoscience Australia Sentinel-2 Near Real Time surface reflectance product.

The Provisional Digital Earth Australia Water Observations (Sentinel-2) product shows where surface water was observed by the Sentinel-2A and Sentinel-2B satellites on any particular day over the most recent 3 months. The surface water observations are derived from Geoscience Australia Sentinel-2 Near Real Time surface reflectance imagery for all of Australia. The provisional, Near Real Time product is available for a rolling window of the most recent three months of data, and is produced within 24 hours of the satellite passing over an area.

## What this product offers

The Provisional Digital Earth Australia Water Observations product shows the extent of surface water in a corresponding Sentinel-2 scene, along with the degree to which the scene was obscured by data quality issues including; cloud, cloud shadows, and where sensor problems cause parts of a scene to not be observable. The Water observations are based on the WOfS algorithm which underpins all of the Digital Earth Australia surface reflectance water products. 

This is a rapid, provisional, product. It has not been validated and is of unknown accuracy, however it may provide useful information about the general extents of surface water soon after an image is acquired.

% ## Data description

## Applications

The Digital Earth Australia Near Real Time Water Observation product is provided as a provisional (not validated, with unknown accuracy) source of information on water in the landscape to help inform emergency management and decision makers on recent and evolving emergency situations. The product can be used to estimate the area of surface water present in the corresponding satellite scene, and can be used for several water monitoring applications. Uses of the individual Water Observations (WOs) includes:

* flood extent
* amount of water in water bodies, major rivers and the coastal zone.

As the WOs are separated from the derived statistics of the associated DEA Water statistical products, the WOs are most useful for performing analyses requiring the investigation of surface water extent for particular times rather than over long term time series.

## Technical information

Digital Earth Australia (DEA) Water Observations (Sentinel-2) Provisional is a dataset indicating areas where surface water has been observed using the Geoscience Australia Sentinel-2 surface reflectance imagery catalogue. The Near Real Time version of this product includes observations from the most recent three months of data collected by the Sentinel-2 satellites. Near Real Time products are created with predicted corrections for atmospheric conditions and ground reflectivity. It covers all of mainland Australia and Tasmania but excludes off-shore Territories. The dataset is updated automatically as each new Sentinel-2 scene is acquired and processed to Near Real Time Analysis Ready Data (ARD) state. 

The Water Observations from Space (WOfS) Water detection algorithm is used to generate a pixel wise classification of Sentinel-2A and Sentinel-2B scenes. The output of this algorithm is a classification with the bit meanings described in Table 1. Because of the way the current version (Version 3.1.6) of the WOfS algorithm operates multiple bits can be set simultaneously for each pixel. Hence the value of a pixel in an observation can be X AND Y AND Z, etc, hence values can range from 0 to 255.

**Table 1:** The table below describes the meaning of each bit set per pixel. Where multiple factors impeding a clear observation are detected all the respective bits will be set. For example a value of 136 indicates water (128) AND terrain shadow (8) were observed for the pixel.

![Bit assignment for DEA_WO_3.1.6](https://cmi.ga.gov.au/_files/cmi/DEA_WO_3_BitFieldTable_resized.png)

Full details of the original algorithms and features of DEA Water Observations can be found in the Water Observations from Space paper by Mueller et al. (2016). [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

## Lineage

The DEA Water Observations dataset is generated using the following steps:

Imagery of the earth’s surface is collected by the Sentinel-2A and Sentinel-2B satellites as a raster based product. Digital Earth Australia receive this data and conduct atmospheric and Bidirectional Reflectance Distribution Function corrections to produce Geoscience Australia Sentinel-2 Analysis Ready Data to predicted (NRT) standard.

Once the input data has been processed to ARD the Water Observations from Space (WOfS) algorithm is applied, including cloud and shadow masking, on a per-granule basis and indexed into the Data Cube for further processing.

## Processing steps

1. Surface Reflectance Calculation (NBAR + Terrain Illumination Correction)

1. Water Observations from Space Detection Algorithm

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

