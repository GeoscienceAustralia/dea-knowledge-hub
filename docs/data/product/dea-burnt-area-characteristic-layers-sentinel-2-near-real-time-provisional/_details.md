## Background

Bushfires pose a serious and increasing threat to Australia. The detection and mapping of burns has many applications to support management of areas impacted by fire. The identification of bushfire burn using Earth Observation is often manual, can come with a significant time delay, and only available at a relatively small scale. This product offers provisional and preliminary change detection using same day satellite data to automatically and rapidly identify burn characteristics. 

Knowledge about the potential location and extent of fire helps to understand community and ecosystem impacts, enables directed relief and recovery support, and informs planning of mitigation burning for future fire seasons.

## What this product offers

DEA Provisional Burnt Area Characteristic Layers contribute to the understanding of the distribution and frequency of fire in the Australian continent by measuring change in vegetation cover and soil characteristics that may be indicative of fire activity in the landscape. This product contains three layers that each describe change in a specific remote sensing index. Change in each index is measured between a baseline reference image and the most recent observation of Australia from the Sentinel 2 satellite constellation.  

The indexes contained in each dataset describe change in a characteristic of the Earth’s surface that may be the result of a burn. The characteristic described are green vegetation cover and the reflective properties of bare soil and of burnt materials. These layers can be used to detect areas that may have been recently burnt, as fire will change the presence of these characteristics in the satellite data. These layers should be used with other information sources to determine if the change is the result of fire or other processes.

% ## Data description

## Applications

* As a preliminary use-case to show the potential of near real-time change detection 
 

* As a screening tool to identify the potential location of new burnt areas 
 

* As a screening tool to identify the potential size of burnt areas 
 

* To visually identify potential changes of known burnt areas between two time periods

## Technical information

This Near Real-Time (NRT) change detection product is based on: 

1. a pre-fire reference baseline dataset (baseline\_metric) - DEA Sentinel 2 Barest Earth (Roberts, et al. 2019). 
 

2. the latest (NRT\_metric) daily Sentinel-2 (A and B combined) Near Real-Time provisional satellite data. 
 

The following metrics were calculated to identify burnt area characteristics: 

* Bare Soil Index (BSI) 
 

* Normalized Difference Vegetation Index (NDVI) 
 

* Normalized Burn Ratio (NBR) 
 

This product contains delta (differenced) indexes for the three metrics above and how the NRT image has changed compared to a reference image. This means, the change metrics are not just describing what the satellite has analysed on a given day but how that day’s landscape has changed from a baseline. Delta indexes, sometimes called differenced indexes, are a useful tool in remote sensing for detecting and mapping environmental or manmade events that have an effect on land cover. This dataset contains three data layers; Delta Normalised Burn Ratio (dNBR), Delta Bare Soil Index (dBSI) and the Delta Normalised Difference Vegetation Index (dNDVI). 

The indexes in this dataset enhance specific characteristics of the Earth’s surface which change as a result of a fire. The delta layers show areas where these characteristics have increased or decreased between the baseline and new scenes. Each delta layer displays values between -1 and +1. Positive values indicate a change that may be indicative of a fire, for example loss of green vegetation or increased soil exposure. Negative values indicate a change that shouldn’t be caused by a fire, such as increased vegetation cover.

It should be noted, values that are further away from zero indicate a greater rate of change from the baseline state. A larger positive value does not necessarily indicate a greater confidence of burn being detected relative to a smaller positive value. 

#### Baseline Imagery 

The baseline image used is the Sentinel 2 ‘Barest Earth’ dataset; a cloud free mosaic generated from Sentinel 2 imagery using the methodology from Roberts et al. 2019 (exposed soil and mineral map of the Australian continent revealing the land at its barest). Using the Barest Earth image as a baseline has a number of advantages. By providing an already very dry baseline state it reduces the number of false positives in the dataset. Vegetation types with strong seasonal variation like grasslands and agricultural areas appear as relatively bare in the baseline image and so little change is visible when harvesting or seasonal drying occurs.

#### Delta Normalised Burn Ratio (dNBR) 

Normalized Burn Ratio (NBR), first published in Wagtendonk et al. (2004), identifies areas that have the characteristics of burnt vegetation. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral response. Burnt vegetation strongly absorbs light in NIR but not in SWIR. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite trend is seen in healthy vegetation. 

NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2). 

The change (delta) in NBR is calculated as: dNBR = baseline\_NBR – NRT\_NBR  

The delta NBR layer displays values between -1 and +1, with positive value being more indicative that an area has been burnt, colour bar provided below.

![colourbar ranging from -1 to +1](/_files/dea-burnt-area/legend_dnbr.png)

#### Delta Bare Soil Index (dBSI) 

The Bare Soil Index (BSI), first proposed in Rikimaru and Miyatake (2002), identifies soil or bare-land characteristics by combining blue, red, near infrared (NIR), and short wave infrared (SWIR) spectral bands. SWIR and red spectral bands can be used to identify basic soil mineralogy while blue and NIR spectral bands can help to detect vegetation. Fire generally increases the visibility of bare soil by reducing vegetation cover so burnt areas can be expected to have a high BSI signal. 

The Bare Soil Index is calculated as: BSI = ((SWIR2 + RED) - (NIR + BLUE)) / ((SWIR2 + RED) + (NIR + BLUE)). 

The change (delta) in BSI is calculated as: dBSI = (baseline\_BSI – NRT\_BSI) \*-1.

Delta BSI is multiplied by negative 1 in order to reverse the scaling so that it can be presented the same way as the other delta indexes, which all have positive values for areas that shows characteristics of being burnt. The dBSI layer displays values between -1 and +1, with a positive value being more indicative that an area has increased exposure of bare soil. Colour bar provided, below.

![Colourbar for dBSI product between -1 to +1](/_files/dea-burnt-area/legend_dbsi.png)

#### Delta Normalised Difference Vegetation Index (dNDVI) 

Normalized Difference Vegetation Index (NDVI), first published in Rouse et al. (1974), is used to detect green photosynthetic vegetation characteristics by identifying the difference between red/visible and near infrared (NIR) spectral bands. Fires generally decrease the presence of green vegetation. 

NDVI is calculated as: NDVI =  (NIR - RED)/(NIR + RED)

The change (delta) in NDVI is calculated as: dNDVI= baseline\_NDVI – NRT\_NDVI

The dNDVI layer displays values between -1 and +1, with positive values being more indicative that green vegetation in an area has decreased, and therefore showing the characteristics of being burnt.

![Colourbar for dNDVI product between -1 to +1](/_files/dea-burnt-area/legend_dndvi.png)

## Lineage

The DEA Burnt Area Characteristic Layers is a change detection product derived from two data sources:

* DEA Sentinel 2 Barest Earth (based on method of Roberts, et al. 2019).
* The daily Sentinel-2 (A and B combined) Near Real-Time provisional satellite data.

The Sentinel-2 (A and B combined) Near Real-Time data is masked for cloud, shadows and other image artefacts using the Sentinel-2 fmask pixel quality layer to help provide as clear a set of observations as possible for change detection.

The following indexes are calculated from both the DEA Sentinel 2 Barest Earth and the Sentinel-2 Near Real-Time data:

* Bare Soil Index (BSI)
* Normalized Difference Vegetation Index (NDVI)
* Normalized Burn Ratio (NBR)

The change layers for each index are then calculated in the following way for each index:

* Change(index) = Barest Earth(index) - Near Real-Time(index)

% ## Processing steps

% ## Software

## References

Cocke A. E., Fulé P. Z., Crouse J. E. (2005) Comparison of burn severity assessments using Differenced Normalized Burn Ratio and ground data. *International Journal of Wildland Fire 14*, 189-198. [https://doi.org/10.1071/WF04010](https://doi.org/10.1071/WF04010)

Dindaroglu, T., Babur, E., Yakupoglu, T., Rodrigo-Comino, J. and Cerdà, A., (2021) Evaluation of geomorphometric characteristics and soil properties after a wildfire using Sentinel-2 MSI imagery for future fire-safe forest. *Fire Safety Journal 122*. [https://doi.org/10.1016/j.firesaf.2021.103318](https://doi.org/10.1016/j.firesaf.2021.103318)

Huete,  A.R., Jackson, R.D., (1987) Suitability of spectral indices for evaluating vegetation characteristics on arid rangelands, *Remote Sensing of Environment, 23( 2),* 213, [https://doi.org/10.1016/0034-4257(87)90038-1](https://doi.org/10.1016/0034-4257(87)90038-1)

Jin, S., Yang, L., Danielson, P., Homer, C., Fry, J. and Xian, G.  (2013). A comprehensive change detection method for updating the National Land Cover Database to circa 2011. *Remote Sensing of Environment* *132*. 159-175 [https://doi.org/10.1016/j.rse.2013.01.012](https://doi.org/10.1016/j.rse.2013.01.012)

Keeley, J. E. (2009). Fire intensity, fire severity and burn severity: A brief review and suggested usage. *International Journal of Wildland Fire*, *18*(1), 116–126  [https://doi.org/10.1071/WF07049](https://doi.org/10.1071/WF07049)

Rahman, S., Chang, H.C., Hehir, W., Magilli, C. and Tomkins, K., (2018) Inter-Comparison of Fire Severity Indices from Moderate (Modis) and Moderate-To-High Spatial Resolution (Landsat 8 & Sentinel-2A) Satellite Sensors. In *IGARSS 2018-2018 IEEE International Geoscience and Remote Sensing Symposium* 2873-2876 [https://doi.org/](https://doi.org/10.1109/IGARSS.2018.8518449)[10.1109/IGARSS.2018.8518449](https://doi.org/10.1109/IGARSS.2018.8518449)

Rikimaru, A., Roy, P.S. and Miyatake, S., (2002). Tropical forest cover density mapping. *Tropical ecology*, *43*(1), 39-47. [https://www.tropecol.com/pdf/open/PDF\_43\_1/43104.pdf](https://www.tropecol.com/pdf/open/PDF_43_1/43104.pdf)

Roberts, D., Wilford, J. & Ghattas, O. (2019). Exposed soil and mineral map of the Australian continent revealing the land at its barest. *Nature Communications* *10*, Article 5297. [https://doi.org/10.1038/s41467-019-13276-1](https://doi.org/10.1038/s41467-019-13276-1)

Rouse, J.W., Haas, R.H., Schell, J.A. and Deering, D.W., (1974). Monitoring vegetation systems in the Great Plains with ERTS. [*NASA special publication*, *351*, 309](https://ntrs.nasa.gov/citations/19740022614)

United Nations, *Normalized Burn Ratio (NBR),* Office for Outer Space Affairs  
UN-SPIDER Knowledge Portal.  [https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio)

van Wagtendonk, J.W.,  Root, R.R., Key, C. H., (2004) Comparison of AVIRIS and Landsat ETM+ detection capabilities for burn severity, *Remote Sensing of Environment, 92 (3),* 397-408 [https://doi.org/10.1016/j.rse.2003.12.015](https://doi.org/10.1016/j.rse.2003.12.015)

