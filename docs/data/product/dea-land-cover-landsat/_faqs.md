## Frequently Asked Questions

:::{dropdown} What are the differences between Version 1.0 and Version 2.0 of this product?

The main differences are as follows.

* Version 1.0 (Collection 2) had a spatial resolution of 25 m, while Version 2.0 (Collection 3) has a spatial resolution of 30 m.
* The 'No data' value has changed from '0' to '255'. This is for consistency with other DEA derivative products.
* The descriptor layers are now only accessible on [DEA Maps](https://maps.dea.ga.gov.au). These layers aggregate information on specific categories such as the distinction between 'Herbaceous' and 'Woody' Natural Terrestrial Vegetation.
* While the overall performance of Version 2.0 is similar to Version 1.0, the classification of Artificial Surface (AS) is notably better in Version 2.0, so the total number of pixels in that class is considerably higher. The Woody Cover ratio also seems to have improved in Version 2.0.
* Some inconsistencies were observed in the areas assigned to the Cultivated Terrestrial Vegetation class between the two versions; however, the overall accuracy for this class remains similar between the two collections.
* There is a notable increase in data affected by stripe artefacts from the Landsat 7 SLC-off failure from 2003 to 2011.

For more details, see the [Quality tab](./?tab=quality).

:::

:::{dropdown} What are the main limitations of the DEA Land Cover classification?

There are limitations originating from both the source satellite data and the algorithms applied to generate the final Land Cover product.

A fundamental limitation of any form of Earth Observation is data availability. Inconsistent data coverage and extended cloud cover periods can lead to gaps in the data, potentially missing entire intra-annual cycles, and this impairs the accuracy of the algorithm.

Another limitation arises from the spatial resolution of 30 m. Smaller landscape features could be missed entirely and incorrectly classified as the surrounding terrain.

Inaccuracies resulting from the performance of the algorithms generally occur when features within the satellite images resemble different features, leading to misclassification. Some examples are as follows: a) Events such as fires and rainfall can cause a response in vegetation that mirrors that of agricultural areas; b) Canopy in residential suburbs may obscure the correct identification of Artificial Surfaces; c) Shadows cast by buildings in dense urban areas can be classified as water; d) Bright sandy regions can be assigned to the Artificial Surfaces class.

Additionally, lack of training data for specific sub-classes and filters applied to the input images can limit the capabilities of the models to detect some environment types.

For more details, see the [Quality tab](./?tab=quality).
:::

:::{dropdown} What is the difference between Level 3 and Level 4 of the product?

DEA Land Cover is based on the globally applicable Food and Agriculture Organisation’s (FAO) Land Cover Classification System (LCCS). The Level 3 classifications are high-level macro-categories that broadly classify the continent into six classes.

The Level 4 classifications combine the Level 3 classes with their associated descriptors, resulting in more granular classes. For example, it differentiates between woody and herbaceous vegetation, as well as between open, closed, and sparse cover. It also provides information on water persistence, which corresponds to the number of months in a given year when water was present.

For more details, see the [Quality tab](./?tab=quality).
:::

:::{dropdown} Which Landsat satellites were used for generating the DEA Land Cover classification?

To generate the Land Cover classification for each calendar year, annual statistics (January to December) derived from the following Landsat satellites were used: Landsat 5, Landsat 7, Landsat 8, Landsat 9

This is an improvement over Version 1.0, which only used Landsat 5, Landsat 7, and Landsat 8.

For more details, see the [Specifications tab](./?tab=specifications) and [Quality tab](./?tab=quality).
:::

:::{dropdown} Is the DEA Land Cover data available for free?

Yes, the DEA Land Cover data is free of charge and released under the [Creative Commons Attribution 4.0 International Licence](https://creativecommons.org/licenses/by/4.0/). However, licenses for specific platforms where the Land Cover data can be accessed, as well as additional data available on those platforms, may vary.

For more details, see the [Access tab](./?tab=access) and [Credits tab](./?tab=credits).
:::

% :::{dropdown} QUESTION
% ANSWER
% :::
