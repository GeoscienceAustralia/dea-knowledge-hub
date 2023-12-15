## Accuracy

There is a strong r2 = 0.99 correlation between predicted and observed canopy cover based on an independent set of LiDAR surveys. It is worth noting however that the per pixel RMSE is high (26%) because the per pixel canopy cover estimates from the LiDAR are very sensitive to the location of the 25 meter grid placement. The accuracy of the green fraction cover percentage estimates is inherited from the FC product. Based on the comparison with 1565 independent field data points the green cover product has an overall Root Mean Squared Error (RMSE) of 11.9%.

The Global Mangrove Watch polygon that was created using the methods described in Lucas et al. 2014 (https://doi.org/10.1071/MF13177) was used to provide a consistent reference frame. However this product has limitations that will impact on the Mangrove\_25 product. Areas that were mangrove prior to 2010 but were not identified as mangrove in 2010 may be omitted from this sequence of maps. Likewise some small areas of coastal non-mangrove woody vegetation (Casuarina and Melaleuca) are included in the GMW mangrove extent polygons. Whilst all reasonable efforts have been taken to minimise this, some errors of commission (non mangrove being identified as mangrove) will still occur.

For more information, see Lymburner et al. (2020).

## Quality assurance

The quality of this product is related to both the quality of the Fractional\_Cover\_25 product and the PQ\_25 product. During periods when only one satellite is operating (1987 to 2003, and 2011/12) the 10th percentile will sometimes contain cloud/cloud shadow artefacts due to the low number of observations per year in these years. This is typically problematic in cloud prone areas such as the Wet Tropics. This can be mitigated in two ways, either by excluding these years from analysis, or by using the PQ\_COUNT layers to identify locations that had a low number of observations in a given year.

