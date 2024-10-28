## Changelog

### Version 2.0.0

* **Breaking change: Shift in grid origin point** &mdash; The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south. Therefore, all tile grid references have been changed. For instance, a tile reference of `x10y10` has changed to `x28y25`. The tile grid references of all derivative products generated from 2024 onwards will also be changed; however, Analysis Ready Data products will not be affected.
* **Enhanced cloud masking to reduce noise** &mdash; An enhancement to cloud masking for input derivative products have reduced cloud and shadow noise. This enhancement (known as 'cloud buffering') involved cleaning cloud masks using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows. Note that some areas of very high surface reflectance (e.g. sand dunes and ocean areas) may exhibit worsened noise or data gaps, but these are infrequent occurrences with low impact.
* **Landsat 9 included** &mdash; Landsat 9 is now included from 2022 onwards which achieves better performance than the standalone Landsat 8 product due to using a larger number of available observations
* **Data Structure Changes** &mdash; Landcover version 1.0.0, contained several tif files including: waterstt-wat-cat-l4a.tif, watersea-veg-cat-l4a-au.tif, waterper-wat-cat-l4d-au.tif, lifeform-veg-cat-l4a.tif, inttidal-wat-cat-l4a.tif, canopyco-veg-cat-l4d.tif, baregrad-phy-cat-l4d-au.tif. These will not be provided in version 2.0.0 as the classifications will be contained within the level4.tif file, allowing users to filter the results as required.
* **Collection Upgrade** &mdash; Landcover version 2.0.0. is based on the latest Landsat Collection 3 Analysis Ready Data. The pixel resolution for Landcover has changed from 25m to 30m resolution.
* **Machine Learning Upgrade** &mdash; Machine Learning methods or algorithms settings for woody cover, cultivated vegetation and artificial surfaces classification have been changed to improve performances.
* **Product ID Upgrade** &mdash; The landcover product ID has been updated to reflect the new ARD collection being used. It was changed from ga_ls_landcover_class_cyear_2 to ga_ls_landcover_class_cyear_3

