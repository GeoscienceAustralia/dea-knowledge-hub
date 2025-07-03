## Accuracy

The accuracy limitations reported below are based on the *DEA Landsat Collection 2 version 2.0.2* of the mangroves dataset. The current DEA Mangroves version 4.0.0 product uses input datasets from DEA Landsat Collection 3. The similarities and differences between these two foundation dataset collections can be reviewed [here](https://www.ga.gov.au/scientific-topics/dea/news/dea-landsat-collection-upgrade). 

The primary changes affecting the Collection 3 mangroves product include:
- Pixel resolution change from 25 m to 30 m
- Use of the updated [Collection 3 Fractional Cover Percentiles](/data/product/dea-fractional-cover-percentiles-landsat/) data product
- Use of the updated [Collection 3 Tasseled Cap Percentiles](/data/product/dea-tasseled-cap-percentiles-landsat/) data product

Due to the increased pixel spatial resolution, the reported accuracies and errors will be similar to those reported previously but not identical.

### Calibration Updates

During the upgrade from Collection 2 to Collection 3, the thresholding values for mangrove canopy classes were recalibrated and adjusted to maintain consistency with the Collection 2 version of the product. The current threshold values are set at (14, 40, 62) for the `pv_pc_10` parameter.

### Known Limitations

* The Global Mangrove Watch (GMW) polygon, created using methods described in Lucas et al. 2014 ([https://doi.org/10.1071/MF13177](https://doi.org/10.1071/MF13177)), provides the consistent reference frame for this product. However, this reference dataset has inherent limitations that impact the DEA Mangroves product:
    * **Omission errors:** Areas that were mangrove habitat prior to 2010 but were not identified as mangrove in the 2010 GMW dataset may be excluded from the DEA Mangroves time series maps.
    * **Commission errors:** Some small areas of coastal non-mangrove woody vegetation (such as Casuarina and Melaleuca species) are incorrectly included within the GMW mangrove extent polygons. While efforts have been made to minimize these errors, some non-mangrove vegetation will still be classified as mangrove in the final product.

## Quality Assurance

Product quality depends on the underlying Fractional Cover product quality. Quality issues occur during periods of limited satellite coverage.

**Problem Periods:**

- **2004-2010:** Landsat 5 performance degradation
- **2011-2012:** Landsat 7 sensor failure

**Impact:** Insufficient observations make 10th percentile calculations statistically unreliable, particularly in cloud-prone regions like the Wet Tropics where persistent cloud cover further reduces available data.

**User Guidance:** Exercise caution when interpreting mangrove classifications from 2004-2012, especially in high cloud frequency areas, as reduced observations may produce unreliable canopy cover estimates.
