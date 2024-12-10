## Background

It is important to know where water is normally present in a landscape, where water is rarely observed, and where inundation has occasionally occurred.

These observations tell us where flooding has occurred in the past, and allows us to understand wetlands, water connectivity and surface-groundwater relationships. This can lead to more effective emergency management and risk assessment.

This is one of the Water Observations from Space suite of products, showing where surface water was observed by the Landsat satellites on any particular day since mid 1986. These daily data layers are termed Water Observation Feature Layers (WOFLs).

## What this product offers

Water Observations from Space (WOfS) provides surface water observations derived from Landsat satellite imagery for all of Australia from 1986 to present.

WOfS shows how often water was seen across Australia as a percentage of how often the Landsat satellites were able to see the Earth at each point clearly. It displays the detected surface water from cloud-free observations for the whole of Australia.

% ## Data description

## Applications

* To understand where flooding may have occurred in the past
* To indicate the permanence of surface water in the Australian landscape by comparing where water is rarely observed with where it is often observed
* To analyse wetlands
* To understand water connectivity and surface-groundwater relationships

## Technical information

Water Observations from Space (WOfS) is a gridded dataset indicating areas where surface water has been observed using the Geoscience Australia (GA) Earth observation satellite data holdings. The current product (Version 2.1.5) includes observations taken between 1986 and 2017 (inclusive) from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

WOfS shows water observed for every Landsat-5, Landsat-7 and Landsat-8 image across Australia (excluding External Territories) for the period of 1986 to 2017. The dataset is updated on as as-needs basis and is expected to increase in update frequency in the future so that as a satellite acquires data, it will automatically be analysed for the presence of water and added to the WOfS product in near real time.  
Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water.

A change in version 2.1.5 from earlier versions is that previously only one bit could be set per pixel. Hence the value of a pixel in a WOFL could be X or Y or Z. Hence in previous versions the WOFL values could only be 0 or 1 or 2 or 4 or ... or 128. With version 2.1.5 the data type has been changed to a bit field, where multiple bits can be set simultaneously. Hence the value of a pixel in a WOFL can be X AND Y AND Z, etc, hence values can range from 0 to 255 in WO\_25\_2.1.5.

The meaning of each bit in the WOFLs is given in the table below.

| Bit | Flagging       | Decimal Value | Description                                                            |
|-----|----------------|---------------|------------------------------------------------------------------------|
| 0   | no data        | 1             | Pixel masked out due to NO_DATA in NBAR source, 0 = valid data in NBAR |
| 1   | contiguity     | 2             | Pixel masked out due to lack of data contiguity                        |
| 2   | sea            | 4             | Pixel masked out due to being over sea                                 |
| 3   | terrain shadow | 8             | Pixel masked out due to terrain shadow                                 |
| 4   | high slope     | 16            | Pixel masked out due to high slop                                      |
| 5   | cloud shadow   | 32            | Pixel masked out due to cloud shadow                                   |
| 6   | cloud          | 64            | Pixel masked out due to cloud                                          |
| 7   | water observed | 128           | Water present                                                          |

For example a value of 136 indicates water (128) AND terrain shadow (8) were observed for the pixel.

In the future, WOfS will be updated as new data are added. This is potentially possible because the dataset is produced using Digital Earth Australia, containing GA's entire Australian Landsat archive in a high performance computing environment at the National Computational Infrastructure at the Australian National University.

The primary purpose of the WOfS product is to help understand where flooding may have occurred in the past. This has application in emergency management and risk assessment.  
The product has many secondary uses. For example the WOfS product provides an indication on the permanence of surface water in the Australian landscape by showing where water is observed rarely in comparison to where it is often observed. This has application in water management and mapping. WOfS has also been used for wetland analyses, water connectivity and surface-ground water relationships.

As the WOFLs have been separated from the derived statistics in this version, WOfS is most useful for performing analyses requiring the investigation of surface water extent for particular times rather than over long term time series.

Full details of the algorithms and features of WOfS can be found in the paper by Mueller et al. (2015).

## Lineage

The Water Observations from Space product (WOfS) is a key component of the National Flood Risk Information Portal (NFRIP), developed by Geoscience Australia (GA). The objective of Water Observations from Space is to analyse GA's historic archive of satellite imagery to derive water observations, to help understand where flooding may have occurred in the past, and hence help inform on areas underÂ threat of flooding in future.

WOfS is being developed in parallel with the National Flood Studies Database system which will provide Flood Study documentation and reports to a wide range of users. Both systems will be delivered via the internet through the NFRIP portal.

Satellite imagery has been used to map floods around the world for several years. Organisations such as the Colorado Flood Observatory in the USA and several state-based agencies in Australia regularly provide satellite-based flood extents for major flood events. GA developed a flood mapping methodology in 2008-2009 that was extensively used for the major Australian flood events since 2010, providing emergency service agencies with regional flood extent information.

The Phase 1 outputs from the NFRIP were delivered to the public in November 2012, including a proof of concept of WOfS. This displayed surface water extents for three study areas, including the original derived extents and the cumulative summary product. Subsequent stakeholder feedback has shown that the most desirable information is the summary product, providing and understanding of the long term dynamics of surface water.

The Phase 2 outputs from the NFRIP (release in April 2014), includedÂ the release of WOfS v1.0, which is accessible to the public as a web service from the NFRIP and from http://eos.ga.gov.au.

The current version of WOfS has separated the individual time slices from the derived summary statistics. The time slices, termed Water Observation Feature Layers (WOFLs) are contained in Water Observations 2 (Landsat), while the summary statistics are contained in Water Observations Statistics 2 (Landsat).

## Processing steps

The water detection algorithm used to detect water from each observed pixel is based on a statistical regression tree analysis of a set of normalised difference indices and corrected band values. The regression is based on a set of water and non-water samples created by visual interpretation of 20 Landsat scenes from across Australia. The sample locations, indicated below, ensure that the logistic regression is based on the full geographic range of conditions experienced in Australia.

The regression analysis determined a set of best indices and bands for the analysis and the associated thresholds in each component to derive a final classification tree, producing a water/non-water classification for pixel in the Data Cube. The final water classification for each pixel is modified by Pixel Quality (see associated PQ product information) and terrain.
Once the water algorithm has completed its process, the water detection for a pixel through time is combined to produce a total number of water observations for each pixel. This is compared to a total number of clear observations for the same pixel, derived from the PQ analysis. The ratio is expressed as a percentage water recurrence.

Confidence that a pixel depicted as having had water detected at some time is calculated by a Confidence Layer. The layer is computed by combining a set of confidence factors using a weighted sum approach, with the weightings derived by logistic regression.

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003 )

