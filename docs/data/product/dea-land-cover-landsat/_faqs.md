## Frequently Asked Questions

:::{dropdown} I was using Land Cover Version 1 in my workflow. What are the key differences in Version 2 that I should be aware of?

While Version 1 (Collection 2) was at 25 m spatial resolution, Version 2 (Collection 3) is at 30 m resolution.

The ‘no data’ value has been changed from ‘0’ to ‘255’ to be consistent with other DEA derivative products.

The overall performance of Version 2 is in line with that of Version 1. However, the classification of Artificial Surface is notably better in Version 2, meaning the number of pixels in that class will be considerably higher. The Woody Cover ratio also seems to have improved in Version 2. Some inconsistencies were observed in the areas assigned to the Cultivated Vegetation class, although the overall accuracy for this class remains similar between the two collections. Moreover, a significant degradation in Version 2 is the increase in Landsat 7 stripe artefacts.

Please refer to the [Quality tab](./?tab=quality) for further details.
:::

:::{dropdown} What are the main limitations of the Land Cover classification?

There are limitations originating from both the source satellite data and the algorithms applied to generate the final Land Cover product.

The primary intrinsic limitation of Earth Observation itself is data availability. Inconsistent data coverage and extended cloud cover periods can lead to gaps in the data, potentially missing entire intra-annual cycles, which impacts the accuracy of the algorithm.

Another limitation arises from the spatial resolution of 30 m. Smaller landscape features could be missed entirely and incorrectly classified as the surrounding terrain.

Inaccuracies resulting from the performance of the algorithms generally occur when features within the satellite images resemble different types of features, leading to misclassification. For example, events such as fires and rainfall can cause a response in vegetation that mirrors that of agricultural areas. Canopy in residential suburbs may hinder the correct identification of Artificial Surfaces. Shadows cast by buildings in dense urban areas can be classified as water. Bright sandy regions can be assigned to the Artificial Surfaces class.

Additionally, lack of training data for specific sub-classes and filters applied to the input images can limit the capabilities of the models to detect some environment types.

Please refer to the [Quality tab](./?tab=quality) for further details.
:::

:::{dropdown} What Landsat satellites were used for generating the Land Cover classification?

To generate the land cover classification for each calendar year, annual (January to December) statistics derived from Landsat-5, -7, -8, and -9 observations were used (in contrast to Version 1, which only used Landsat-5, -7, and -8). The combination of data from these different satellites enabled the creation of a timeseries of annual Land Cover classifications over more than 35 years. 
:::

% :::{dropdown} QUESTION
% ANSWER
% :::
