## Background

Mangroves provide a diverse array of ecosystem services but these are impacted upon by both natural and anthropogenic drivers of change. In Australia, mangroves are protected by law and hence the natural drivers predominate.

It is important to understand the canopy density of mangroves in Australia so that we can measure how mangroves are responding to sea level rise, severe tropical cyclones and climatic cycles.

## What this product offers

This product provides valuable information about the extent and canopy density of mangroves for each year from 1987 for the entire Australian coastline.

The canopy cover classes are:
* 20-50% (pale green)
* 50-80% (mid green)
* 80-100% (dark green)

The product consists of a sequence (one per year) of 30 m resolution maps that are generated by analysing the Landsat [fractional cover](https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the [Global Mangrove Watch layers](https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

It includes cloud and shadow buffering with a size of 6 pixels. This buffering is applied to Landsat 5, Landsat 7, Landsat 8, and Landsat 9 data from 2022 onwards.

% ## Data description

## Applications

The sequence of mangrove maps makes it possible to see how the canopy cover of mangroves changes over time. The maps can be used to understand how mangroves respond to disturbance events such as severe tropical cyclones. The maps can also be used to improve our representation of the ecosystem services provided by mangroves, which include:
* coastal protection
* carbon storage
* providing nursery grounds for commercially important fish and prawn species
* providing habitat for migratory and endemic bird species

## Technical information

To determine annual national level changes in mangroves, changes in their canopy cover type were quantified using dense time-series (nominally every 16 days cloud permitting) of 30 m spatial resolution Landsat sensor data available within Digital Earth Australia (DEA).

The potential area that mangroves occupied over this period was established as the union of mangrove maps generated for 1996, 2007-2010 and 2015/16 through the Japanese Aerospace Exploration Agency (JAXA) Global Mangrove Watch (GMW), and then refined using tasseled cap wetness dynamics and State and Territory mangrove mapping products. Within the potential mangrove area the 10th percentile of photosynthetic vegetation (ga_ls_fc_pc_cyear_3 (pv_pc_10)) is retrieved from the [DEA Fractional Cover Percentiles](https://knowledge.dea.ga.gov.au/data/product/dea-fractional-cover-percentiles-landsat/) product and used to estimate the percentage Planimetric Canopy Cover (PCC%). PCC% is a planar unit, directly related to forest cover, representing the horizontal distribution of forest cover when determined from above, such as by Light Detection And Ranging (LiDAR) or spectral satellite. The PCC% was estimated for each Landsat pixel using a relationship between pv_pc_10 and LiDAR-derived PCC% (< 1 m resolution and based on LiDAR acquisitions from all states supporting mangroves, excluding Victoria).

% ## Lineage

## Processing steps

The product development methodology is outlined in the following steps:

<div class="processing-steps"></div>

1. Calculate the green fractional cover (`pv_pc`) from all available cloud-free Landsat pixels for each year of observation and compare these over an annual time series to identify areas where green cover persists throughout the year.
1. Establish a relationship between the 10th percentile of green fraction (`pv_pc_10`) observed within a year and Planimetric Canopy Cover percentage (PCC%) derived from < 1 m spatial resolution canopy masks derived from Light Detection And Ranging (LiDAR) with this representing a unit that relates directly to forest cover.
1. Constrain the PCC% estimates to areas known to contain mangroves, with reference to the Japanese Aerospace Exploration Agency’s (JAXA) Kyoto and Carbon (K&C) Initiative Global Mangrove Watch (GMW) thematic layers for 1996, 2007-10 and 2015/16 with additional areas identified using tasseled cap wetness and State and Territory mangrove mapping products.
1. Apply PCC% thresholds to map mangrove forest extent (based on a pre-determined 20 PCC% threshold) and differentiate structural categories, namely, woodland (20-50 %), open forest (50-80 %), and closed forest (> 80 %).
1. Quantify the change in the relative extent of mangrove forest and canopy cover types over the period 1987 to the latest full calendar year at a national scale and establish relevance at regional (e.g., State/Territory) and local levels.

% ## Software

## References

Lymburner, L., Bunting, P., Lucas, R., Scarth, P., Alam, I., Phillips, C., Ticehurst, C., & Held, A. (2020). Mapping the multi-decadal mangrove dynamics of the Australian coastline. *Remote Sensing of Environment*, *238*, 111185. [https://doi.org/10.1016/j.rse.2019.05.004](https://doi.org/10.1016/j.rse.2019.05.004)

