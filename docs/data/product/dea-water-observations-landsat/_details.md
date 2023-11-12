## Background

It is important to know where water is normally present in a landscape, where water is rarely observed, and where inundation has occasionally occurred.

These observations tell us where flooding has occurred in the past, and allows us to understand wetlands, water connectivity and surface-groundwater relationships. This can lead to more effective emergency management and risk assessment.

This is the principal Digital Earth Australia (DEA) Water product (previously known as Water Observations from Space (WOfS)), providing the individual water observations per satellite image that are subsequently used in the following DEA Water suite and related water bodies products: DEA Waterbodies (Landsat), DEA Water Observations Statistics (Landsat), DEA Water Observations Filtered Statistics (Landsat).

This product shows where surface water was observed by the Landsat satellites on any particular day since mid 1986. These daily data layers are termed Water Observations (WOs).

## What this product offers

DEA Water Observations provides surface water observations derived from Landsat satellite imagery for all of Australia from 1986 to present.

The Water Observations show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows or where sensor problems cause parts of a scene to not be observable.

% ## Data description

## Applications

The DEA Water Observations (WOs) are used to determine the area of surface water present in the corresponding satellite scene, and can be used for several water monitoring applications. Uses of the individual WOs include:

* flood extent
* amount of water in water bodies, major rivers and the coastal zone.

As the WOs are separated from the derived statistics of the associated DEA Water statistical products, the WOs are most useful for performing analyses requiring the investigation of surface water extent for particular times rather than over long term time series.

## Technical information

Digital Earth Australia (DEA) Water Observations (WOs) is a gridded dataset indicating areas where surface water has been observed using the Geoscience Australia (GA) Earth observation satellite data holdings. The current product (Version 3.1.6) includes observations taken between 1986 and the present (inclusive) from the Landsat 5, 7 and 8 satellites. WOs cover all of mainland Australia and Tasmania but exclude off-shore Territories. The dataset is updated automatically as each new Landsat scene is acquired and processed to Analysis Ready Data (ARD) state. 

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The meaning of each bit in the WOFLs is given in the table below. Prior to version 2.1.5, only one bit could be set per pixel, therefore the value of a pixel in an Observation could be X OR Y OR Z. Hence in previous versions the WOs values could only be 0 or 1 or 2 or 4 or ... or 128. From version 2.1.5 onward the data type has been changed to a bit field, where multiple bits can be set simultaneously. Hence the value of a pixel in an Observation can be X AND Y AND Z, etc, hence values can range from 0 to 255.

This version (3.1.6) has been further updated with changes to the way different factors impeding water detection are dealt with. These changes result in improved detection rates and allow discrimination of different factors impeding water observations. Masking of the ocean with a pre-defined mask has been removed, and the extent of the ocean is now defined by the algorithm. Masking for terrain and solar incident angle have been de-coupled in order to provide better visibility about the reason for masking. The solar incident angle threshold used to remove poor quality observations collected when the sun is at a very low angle has been reduced from 30 degrees to 10 degrees. This change increases the number of observations included in the dataset during winter months while still removing those that are most badly impacted by shadowing caused by low solar incident angle. 

The table below describes the meaning of each bit set per pixel in each WOFL. Where multiple factors impeding a clear observation are detected all the respective bits will be set. For example a value of 136 indicates water (128) AND terrain shadow (8) were observed for the pixel.

![Bit assignment for DEA_WO_3.1.6](/_files/cmi/DEA_WO_3_BitFieldTable_resized.png)

Full details of the original algorithms and features of DEA Water Observations can be found in the Water Observations from Space paper by Mueller et al. (2015).

## Lineage

Digital Earth Australia (DEA) Water Observations is derived from Landsat 5, 7 and 8 imagery. Imagery is initially corrected to Analysis Ready Data (ARD) standard, and masked for cloud, cloud-shadow, data contiguity, steep slope, solar incidence angle, and terrain shadow. Water classification is achieved using a decision tree based on the individual spectral bands of the Landsat satellites and derived normalised difference indicies associated with water and vegetation. The output is then stored as an 8-bit, bit-field with values from 0 - 255 indicating the presence or absence of each mask type and the presence or absence of water.

## Processing steps

1. Water Observations from Space Detection Algorithm

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

