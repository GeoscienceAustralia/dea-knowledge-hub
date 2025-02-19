## Frequently Asked Questions

:::{dropdown} I was using DEA Land Cover Version 1 in my workflow. What are the key differences in Version 2 that I should be aware of?

Version 1 (Collection 2) had a spatial resolution of 25 m, while Version 2 (Collection 3) has a spatial resolution of 30 m.

The 'no data' value has changed from '0' to '255', to maintain consistency with other DEA derivative products.

The descriptor layers, which aggregate information on specific categories such as the distinction between 'Herbaceous' and 'Woody' Natural Terrestrial Vegetation, are now only accessible on [DEA Maps](https://maps.dea.ga.gov.au).

While the overall performance of Version 2 is in line with Version 1, the classification of Artificial Surface (AS) is notably better in Version 2, so the total number of pixels in that class is considerably higher. The Woody Cover ratio also seems to have improved in Version 2.

Some inconsistencies were observed in the areas assigned to the Cultivated Terrestrial Vegetation class between the two versions. However, the overall accuracy for this class remains similar between the two collections.

There is a notable increase in data affected by stripe artefacts from the Landsat 7 SLC-off failure from 2003 to 2011.

Please refer to the [Quality](./?tab=quality) tab of the Land Cover product for further details.

:::

:::{dropdown} What are the main limitations of the DEA Land Cover classification?

There are limitations originating from both the source satellite data and the algorithms applied to generate the final Land Cover product.

The primary intrinsic limitation of Earth Observation itself is data availability. Inconsistent data coverage and extended cloud cover periods can lead to gaps in the data, potentially missing entire intra-annual cycles, which impacts the accuracy of the algorithm.

Another limitation arises from the spatial resolution of 30 m. Smaller landscape features could be missed entirely and incorrectly classified as the surrounding terrain.

Inaccuracies resulting from the performance of the algorithms generally occur when features within the satellite images resemble different types of features, leading to misclassification. For example, events such as fires and rainfall can cause a response in vegetation that mirrors that of agricultural areas. Canopy in residential suburbs may hinder the correct identification of Artificial Surfaces. Shadows cast by buildings in dense urban areas can be classified as water. Bright sandy regions can be assigned to the Artificial Surfaces class.

Additionally, lack of training data for specific sub-classes and filters applied to the input images can limit the capabilities of the models to detect some environment types.

Please refer to the [Quality](./?tab=quality) tab of the Land Cover product for further details.
:::

:::{dropdown} What is the difference between DEA Land Cover Level 3 and Level 4?

DEA Land Cover is based on the globally applicable Food and Agriculture Organisation’s (FAO) Land Cover Classification System (LCCS). The Level 3 classifications are higher-level, macro-categories that broadly classify the continent into six classes.

The Level 4 classifications combine the Level 3 classes with their associated descriptors, resulting in more granular classes. For example, it differentiates between woody and herbaceous vegetation, as well as between open, closed, or sparse cover. It also provides information on water persistence, which corresponds to the number of months in a given year when water was present.

Please refer to the [Description](./?tab=description) tab of the Land Cover product for more details.

:::

:::{dropdown} What Landsat satellites were used for generating the DEA Land Cover classification?

To generate the land cover classification for each calendar year, annual statistics (January to December) derived from Landsat-5, -7, -8, and -9 observations were used. This is an improvement over Version 1, which only used Landsat-5, -7, and -8.

Please refer to the [Specifications](./?tab=specifications) and [Quality](./?tab=quality) tabs of the Land Cover product for more details.
:::

:::{dropdown} Is the DEA Land Cover data available for free?

Yes, the DEA Land Cover data is free of charge and released under the [Creative Commons Attribution 4.0 International Licence](https://creativecommons.org/licenses/by/4.0/). However, licenses for specific platforms where the Land Cover data can be accessed, as well as additional data available on those platforms, may vary.

Please refer to the [Access](./?tab=access) and [Credits](./?tab=credits) tabs of the Land Cover product for more details.

:::

% :::{dropdown} QUESTION
% ANSWER
% :::
