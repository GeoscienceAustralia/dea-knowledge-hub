## Accuracy

The following accuracies and limitations reported for this product are relative to the [DEA Landsat Collection 2 version 2.0.2](https://cmi.ga.gov.au/data-products/dea/191/dea-mangrove-canopy-cover-landsat) of the mangroves dataset. The current DEA Mangroves version 3.0.0 product was produced with input datasets from DEA Landsat Collection 3. The similarities and differences between these two foundation dataset collections can be reviewed [here](https://www.dea.ga.gov.au/news/landsat-collection-upgrade). The primary impact on the collection 3 mangroves product is the change in pixel resolution from 25 to 30 m2 and use of the updated [collection 3 fractional cover](https://cmi.ga.gov.au/data-products/dea/629/dea-fractional-cover-landsat) (FC) data product. Due to the increase in pixel spatial resolution, the reported accuracies and errors will be similar to those reported previously but not identical.

There is a strong r2 = 0.99 correlation between predicted and observed canopy cover based on an independent set of LiDAR surveys. It is worth noting however that the per pixel Root Mean Squared Error (RMSE) is high (26%) because the per pixel canopy cover estimates from the LiDAR are very sensitive to the location of the grid placement. The accuracy of the green fraction cover percentage estimates is inherited from the FC product. Based on the comparison with 1565 independent field data points the green cover product has an overall RMSE of 11.9%.

The Global Mangrove Watch polygon that was created using the methods described in Lucas et al. 2014 ([https://doi.org/10.1071/MF13177](https://doi.org/10.1071/MF13177)) was used to provide a consistent reference frame. However this product has limitations that will impact on the DEA Mangroves product. Areas that were mangrove prior to 2010 but were not identified as mangrove in 2010 may be omitted from this sequence of maps. Likewise some small areas of coastal non-mangrove woody vegetation (Casuarina and Melaleuca) are included in the GMW mangrove extent polygons. Whilst all reasonable efforts have been taken to minimise this, some errors of commission (non mangrove being identified as mangrove) will still occur.

For more information, see Lymburner et al. (2020).

## Quality assurance

The quality of this product is related to the quality of the Fractional Cover product. During periods when only one satellite is operating (1987 to 2003, and 2011/12) the 10th percentile will sometimes contain cloud/cloud shadow artefacts due to the low number of observations per year in these years. This is typically problematic in cloud prone areas such as the Wet Tropics.

