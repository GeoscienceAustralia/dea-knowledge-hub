## Changelog

### 30 Apr 2025: The 2024 annual data is now available

The 2024 annual data for this product was published on 30 April 2025. You are now able to [access the latest data](./?tab=access) via DEA Maps and other methods. [View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz6811775c5a24b812Pzzzz6567c8b713b5b826/page.html).

### Version 2.0.0

This latest version introduces improvements to the DEA Land Cover product, enhancing the translation of over three decades of satellite imagery into evidence of how Australia’s land, vegetation and waterbodies have changed over time. 

* **Breaking change: Shift in grid origin point** &mdash; The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south. Therefore, all tile grid references have been changed. For instance, a tile reference of `x10y10` has changed to `x28y25`.
* **Breaking change: Data structure changes** &mdash; Land Cover version 1.0 contained several TIF files including `waterstt-wat-cat-l4a.tif`, `watersea-veg-cat-l4a-au.tif`, `waterper-wat-cat-l4d-au.tif`, `lifeform-veg-cat-l4a.tif`, `inttidal-wat-cat-l4a.tif`, `canopyco-veg-cat-l4d.tif`, and `baregrad-phy-cat-l4d-au.tif`. These will not be provided in Land Cover 2.0 because the classifications are instead contained within the `level4.tif` file, allowing users to filter the results as required. An RGB TIF colour representation of the Land Cover classifications is also no longer available. Instead, a style file will be provided that can be uploaded to your GIS software which will apply the same colour representations of the classifications in the Level 3 and Level 4 TIF files.
* **Improved cloud masking to reduce noise** &mdash; The masking of clouds and cloud shadows applied to DEA Land Cover model’s input data was improved, resulting in fewer noisy pixels in the final Land Cover product. 
* **Landsat 9 included** &mdash; Landsat 9 is included from 2022 onwards, leading to improved performance compared to the standalone Landsat 8 product. This is due to the increased number of observations from the combined Landsat 8 and 9 sensors.
* **Machine Learning Upgrade** &mdash; The settings for machine learning (ML) methods and algorithms have been changed to improve performance. This is for woody cover, cultivated vegetation, and artificial surface classification. The Urban model uses a different ML approach, shifting from a pixel-based to a raster-based method, and a new model was trained using collection 3 data. The cultivated model maintains the same approach, but the input features were re-engineered using Geoscience Australia’s collection 3 data, and the model was re-trained. The woody cover model also follows the same approach, with the model being re-trained using Geoscience Australia’s collection 3 data.
* **Pixel resolution** &mdash; The pixel resolution for Land Cover 2.0 has changed from 25m to 30m resolution.
* **Product ID Update** &mdash; The Land Cover product ID has been updated to reflect the new ARD collection being used. It was changed to `ga_ls_landcover_class_cyear_3`. This ID is used to [load data from the Open Data Cube (ODC)](/notebooks/Beginners_guide/04_Loading_data/).
* **'No data' value changed** &mdash; The 'no data' value has been changed from '0' to '255' to be consistent with other DEA derivative products.
* **Level 4 classification update** &mdash; The level 4 classifications have been updated to include the class 'Cultivated Terrestrial Vegetated: Woody'.
* **Collection Upgrade** &mdash; Land Cover version 2.0 is based on Geoscience Australia’s latest Landsat collection 3 analysis ready data. 

