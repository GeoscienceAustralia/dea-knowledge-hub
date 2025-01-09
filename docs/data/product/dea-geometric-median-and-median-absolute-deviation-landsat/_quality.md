## Accuracy

The accuracy of the GeoMAD layers is dependent on the accuracy of the earth observation data on which it is based. 

To calculate a reliable geometric median or MAD, the majority of the input data must be free of clouds, shadows, or other visual obstructions. For locations that experience more than 50% of time under clouds and shadows (such as areas of Tasmania) the GeoMAD can produce an output that is obscured by visual noise. Therefore, it is necessary to use a large enough collection of data to prevent this occurring. 

To reduce the impact of poor-quality earth observation data, the input data is screened using the Pixel Quality product.  

Note that where no-data pixels occur in locations that clear observations should occur, the cause is a lack of clear pixels to populate the GeoMAD. 

Also, note that since  the geometric median and MAD are synthetic (not observed directly by satellite), they cannot be verified by field work.

## Known Issues

### 19 Sep 2024: GeoMAD processing bug

In the [DEA Geometric Median and Median Absolute Deviation (Landsat)](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) product, a bug in the processing code related to multithreading using numexpr (a fast numerical expression evaluator for Numpy) has been identified which may cause a 400x400 pixel data block to be misplaced within a tile. For the full GeoMAD archive, it is possible that there are around 8-12 tiles with incorrect data (misplaced blocks). It is unknown at this stage which tiles are affected. We are investigating the bug and will provide more information in late 2024 to early 2025.
