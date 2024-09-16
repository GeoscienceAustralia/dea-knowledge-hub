## Accuracy

The following limitations reported for this product are relative to the *DEA Landsat Collection 2 version 2.0.2* of the mangroves dataset. The current DEA Mangroves version 4.0.0 product was produced with input datasets from DEA Landsat Collection 3. The similarities and differences between these two foundation dataset collections can be reviewed [here](https://www.ga.gov.au/scientific-topics/dea/news/dea-landsat-collection-upgrade). The primary impact on the Collection 3 mangroves product is the change in pixel resolution from 25m to 30m and use of the updated [Collection 3 Fractional Cover](/data/product/dea-fractional-cover-landsat/) data product. Due to the increase in pixel spatial resolution, the reported accuracies and errors will be similar to those reported previously but not identical.

During the upgrade process from Collection 2 to Collection 3, the mangrove thresholds for different classes were adjusted to more closely align with the Collection 2 version of the products. The current thresholds are set at (14, 40, 62).

The Global Mangrove Watch (GMW) polygon that was created using the methods described in Lucas et al. 2014 ([https://doi.org/10.1071/MF13177](https://doi.org/10.1071/MF13177)) was used to provide a consistent reference frame. However this product has limitations that will impact the DEA Mangroves product. Areas that were mangrove prior to 2010 but were not identified as mangrove in 2010 may be omitted from this sequence of maps. Likewise some small areas of coastal non-mangrove woody vegetation (Casuarina and Melaleuca) are included in the GMW mangrove extent polygons. Whilst all reasonable efforts have been taken to minimise this, some errors of commission (non mangrove being identified as mangrove) will still occur.

For more information, see Lymburner et al. (2020).

## Quality assurance

The quality of this product is related to the quality of the Fractional Cover product. During periods when only one satellite is operating (1987 to 2003, and 2011/12) the 10th percentile will sometimes contain cloud/cloud shadow artefacts due to the low number of observations per year in these years. This is typically problematic in cloud prone areas such as the Wet Tropics.

