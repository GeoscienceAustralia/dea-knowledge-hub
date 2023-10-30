## Accuracy

To provide an estimate of accuracy the FC algorithm results were compared with 1565 field sites that were not used to train the FC model.

Based on the comparison with this independent field data the FC product has an overall Root Mean Squared Error (RMSE) of 11.9%. The error margins vary for the three different layers: green RMSE: 11.9%, non-green RMSE: 17.1% and bare RMSE: 14.6%.

The effect of soil moisture may impact the accuracy of the FC product, and the similarity between some bare soil endmembers and non-photosynthetic vegetation endmembers can lead to model instability.  Soil types/colours that were not included in the model training data may also be error prone. Pixels that show poor model stability are flagged in the model error band as a value of 2, and can be omitted from further analysis if necessary.

FC products have no water masking applied, so erroneous values for green vegetation over the water may appear. These should be ignored and can be masked out by applying the Water Observations (WO) layer.

Occasionally the sum of the three components is not equal to 100%. Differences are usually small and are not rounded in order to preserve what may be useful seasonal indicators.

Landsat 8 OLI has different relative spectral response curves to the Landsat 5 TM and Landsat 7 ETM+ sensors. To account for this a spectral band adjustment factor is applied to the Landsat 8 data to make it more similar to reflectance as measured by Landsat 7. The adjustment factors are described in more detail in Flood (2014).

Whilst the same training data has been used to train both the JRSRP fractional cover product and the DEA fractional cover product, differences in the terrain corrected surface reflectance data that are used as model inputs mean that the two products are not identical.  The differences between the two products are typically less than 5% for the bare soil and non-green cover types, and typically less than 10% for green cover.

## Quality assurance

The following details are an extract from the information contained at: [http://data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Seasonal+Fractional+Cover](http://data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Seasonal+Fractional+Cover )

The bare soil, green vegetation and non-green vegetation endmembers are calculated using models linked to an intensive field sampling program that covers a wide range of Australian landscapes covering a wide variety of vegetation, soil and climate types were sampled to measure overstorey and ground cover following the procedure outlined in Muir et al (2011).

