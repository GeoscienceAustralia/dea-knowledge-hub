## Changelog

### 10 Sep 2025: DEA Land Cover continental mosaics

We've added a new way to access our [DEA Land Cover](/data/product/dea-land-cover-landsat/) product; it is now available as continental mosaics, in Cloud-optimised GeoTIFF (COG) format. These mosaics provide a single-file representation of land cover data for **each year available** in the time series, removing the complexity of managing tiled datasets and making it easier to work with land cover data across Australia. 

These COG mosaics are designed for fast and efficient streaming over the internet, loading only the portions of the file that are visible in your current view. This makes them ideal for use in **GIS platforms** such as **QGIS** and **ESRI’s software**, where users can interact with the DEA Land Cover dataset without needing to download entire files.

To enhance visualisation and interpretation, we also provide **Virtual Raster (VRT) files** with embedded colour styling aligned to the official DEA colour scheme. These VRTs make the data ready-to-use and visually meaningful out of the box. 

The mosaics and VRTs can also be streamed for use in Python workflows using tools such as **rioxarray**.

[Explore the latest year's continental mosaics (2024)](https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_landcover_class_cyear_3/2-0-0/continental_mosaics/2024--P1Y/)

[Learn how to use DEA Land Cover continental mosaics](/data/product/dea-land-cover-landsat/?tab=access#access-the-data-2)

![Animation showing COG zoom in](/_files/land_cover/zoom_cog_landcover.gif)

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz68c0df3fa6de5146Pzzzz6567c8b713b5b826/page.html)

### 10 Sep 2025: DEA data in the Digital Atlas of Australia

The [DEA Coastlines](/data/product/dea-coastlines/), [DEA Mangroves](/data/product/dea-mangroves/), and [DEA Water Observations Multi-Year Summary](/data/product/dea-water-observations-statistics-landsat/) datasets have now been added to the Digital Atlas, joining [DEA Land Cover](/data/product/dea-land-cover-landsat/). This integration marks a significant milestone in how DEA data can be accessed, visualised, and applied. By embedding DEA products into the Digital Atlas, users can now interact with trusted Earth observation datasets alongside other authoritative national data — unlocking powerful new opportunities for cross-sector analysis and decision-making. 

[Explore the DEA datasets and tools in the Digital Atlas](https://digital.atlas.gov.au/search?source=Digital%2520Earth%2520Australia)

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz68c0df3fa6de5146Pzzzz6567c8b713b5b826/page.html)

### June 2025: Resolved issue with missing data and artefacts in northern Western Australia

An issue was identified affecting data availability and causing classification artefacts across several tiles in northern Western Australia, particularly between 1988 and 2005. The primary affected tiles were `x39y49`, `x40y47`, and `x41y45`, although a total of 17 adjacent tiles (including the three mentioned) experienced the issue.

The root cause was traced to Geometric Quality Assessment (GQA) values falling below the acceptable threshold set. This threshold was used to filter out low-quality Landsat scenes from the [Analysis Ready Data (ARD)](/guides/reference/analysis_ready_data_corrections/) inputs used to generate DEA Land Cover. The areas affected by this issue corresponded to regions where ground control points may shift over time, such as areas with shifting sand dunes, leading to inconsistencies in the orthorectification process. As a result, a large number of ARD scenes, not necessarily unusable, were excluded due to their lower GQA scores, reducing data coverage in the output product.

The issue was resolved by disabling GQA-based filtering in the affected areas, after observing that this had no noticeable impact on image sharpness or output quality.
 
![timeseries missing data tiles](/_files/land_cover/gqa_tiles_timeseries_geomad_obs_count_gmad.gif)

Figure 1. Time series animation showing the frequency of missing data in the affected region. On the left is a true-colour time series of the yearly geomedian, for reference. On the right is a time series of the yearly clear observation count.

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

