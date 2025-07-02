## Background

DEA Mangroves was developed to address the critical need for comprehensive, long-term monitoring of Australia's mangrove ecosystems, which face increasing pressures from climate change, coastal development, and extreme weather events.

## Applications

This dataset provides annual mangrove canopy density information across Australia's entire coastline since 1987, offering valuable insights into ecosystem dynamics. 
The timeseries capabilities enable effective monitoring and quantification of mangrove canopy cover changes, supporting important conservation and management decisions. 
The extensive spatial and temporal coverage provides opportunities to understand how mangroves respond to major disturbance events such as severe tropical cyclones. 
These maps enhance our understanding of the vital ecosystem services that mangroves provide, including coastal protection, carbon storage, nursery grounds for commercially important fish and prawn species, and habitat for migratory and endemic bird species.

## Technical Information

The DEA Mangroves product consists of 30 m resolution annual maps of mangrove canopy cover classes. Each annual map contains one layer (band) `canopy_cover_class`, with values defined as follows:

* Not observed (grey) `0`: insufficient observations per year to determine if mangroves exist
* Woodland 20-50% (pale green) `1`: mangroves present with Planimetric Canopy Cover Percentage (PCC%) between 20% and 50%
* Open forest 50-80% (mid green) `2`: mangroves present with PCC% between 50% and 80%
* Closed forest 80-100% (dark green) `3`: mangroves present with PCC% above 80%
* No data (transparent) `255`: no mangroves present, either PCC% below 20% or outside mangrove habitat

## Lineage

The mangrove footprint is defined by combining the maximum spatial extent from two sources:
- [Global Mangrove Watch layers](https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency
- State and Territory mangrove mapping products from Queensland, Northern Territory, and South Australia

This potential mangrove habitat is then refined using DEA Tasseled Cap Percentiles (specifically the `wet_pc_10` band).

Mangrove canopy classification is performed using DEA Fractional Cover Percentiles bands:
- pixels are classified by thresholding `pv_pc_10` values (which serve as a proxy for PCC%) when quality assurance flag `qa=2`
- pixels are marked as `Not observed` when quality assurance flag `qa=1`

**Note:** The maximum spatial extent remains consistent across all product versions. However, the mangrove habitat refinement and classification thresholds are updated and recalibrated for each version.

## Processing Steps

The product development follows a three-stage methodology:

#### Stage 1: Determine the maximum spatial extent of mangroves
1. Establish the potential mangrove area from 1987 to 2019 by combining mangrove maps from multiple time periods (1996, 2007-2010, and 2015/16) generated through the Japanese Aerospace Exploration Agency (JAXA) Global Mangrove Watch (GMW)
2. Refine this combined map using State and Territory mangrove mapping products

#### Stage 2: Calibrate thresholding values for mangrove canopy cover classes
1. Extract Planimetric Canopy Cover Percentage (PCC%) from high-resolution Light Detection and Ranging (LiDAR) data (1 m resolution)
2. Perform regression analysis between satellite-derived `pv_pc_10` values and LiDAR-derived PCC% for corresponding locations and time periods
3. Determine the specific `pv_pc_10` threshold values that correspond to 20%, 50%, and 80% PCC% levels

#### Stage 3: Classify mangrove canopy density
1. Refine the mangrove footprint by applying `wet_pc_10` thresholds within the maximum spatial extent established in Stage 1
2. Classify pixels within the refined mangrove footprint by applying the calibrated `pv_pc_10` threshold values (from Stage 2) to assign appropriate canopy cover classes
3. Assign `Not observed` classification to pixels where the quality assurance flag `qa=1` indicates insufficient data quality

**Note:** 
- Stage 1 is performed only once during initial product development to establish the maximum spatial extent. 
- Stage 2 is performed during major version upgrades to recalibrate threshold values. 
- Stage 3 (mangrove canopy density classification) is performed annually using the established thresholds to generate each year's mangrove map from 1987 to present.


% ## Software

## References

Lymburner, L., Bunting, P., Lucas, R., Scarth, P., Alam, I., Phillips, C., Ticehurst, C., & Held, A. (2020). Mapping the multi-decadal mangrove dynamics of the Australian coastline. *Remote Sensing of Environment*, *238*, 111185. [https://doi.org/10.1016/j.rse.2019.05.004](https://doi.org/10.1016/j.rse.2019.05.004)

