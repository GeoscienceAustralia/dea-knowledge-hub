## Background

Bushfires pose a serious and increasing threat to Australia. Detection and mapping of burns have many applications to support areas impacted by fire. However, the identification of bushfire burn using Earth Observation is often manual, can come with a significant time delay, and at a relatively small scale. This product offers provisional and preliminary change detection using same day satellite data to automatically and rapidly identify burn characteristics.

Knowledge about the potential location and extent of fire helps to understand community and ecosystem impacts, enables directed relief and recovery support, and informs planning of mitigation burning for future fire seasons.

## What this product offers

DEA Burnt Area Vectors contribute to the understanding of the distribution and frequency of fire, in the Australian continent, by identifying change in vegetation cover and soil characteristics that may be indicative of fire activity in the landscape. This product contains vector outlines identifying areas of change between a baseline image and the most recent observation on the Sentinel 2 satellite constellation. 

Change is detected by combining the three indexes from the DEA Burnt Area Characteristic Layers, which describe characteristics of the earth surface that change as the result of a burn. This dataset identifies areas where the input Characteristic Layers detect substantial change, delivered as a vector outline product. This dataset also includes information on areas of the landscape that were not observed within the observation area. These areas might be smoke or cloud obscuring the satellite pass.

% ## Data description

## Applications

* As a preliminary use-case to show the potential of near real-time change detection
* As a screening tool to identify the potential location of new burnt areas
* As a screening tool to identify the potential size of burnt areas
* To visually identify potential changes of known burnt areas between two time periods

## Technical information

This Near Real-Time (NRT) change detection product is based on the DEA Burnt Area Characteristic Layers. The product identifies areas of substantial change by combining the three change layers from the DEA Burnt Area Characteristic Layers; Delta Normalised Burn Ratio ($\Delta$NBR), Delta Bare Soil Index ($\Delta$BSI) and the Delta Normalised Difference Vegetation Index ($\Delta$NDVI).

Substantial change is defined by applying a threshold to each Characteristic Layer of + 0.1. The thresholded layers are then combined in the following way; areas where thresholded delta NBR ($\Delta$NBR) agrees with either of the other thresholded delta layers are considered to be possible burnt area. This possible burnt area then undergoes a process of binary dilation and erosion in order to remove noise from the dataset by removing outlying single 10 x 10 m pixels before areas of possible burn are converted into vector shapes.

A Data Quality Mask is generated from the Sentinel-2 Near Real-Time product fmask layer. Cloud, cloud shadow and water that are detected by fmask are used to generate a binary layer which undergoes the same dilation and erosion process as the possible burnt area. This layer is then converted into vector outlines which are included in the vector product as a Data Quality Mask indicating the areas which should be considered as “Not Analysed” by the change detection algorithms.

## Lineage

The DEA Burnt Area Vectors are generated from the DEA Burnt Area Characteristic Layers and the Sentinel-2 (A and B combined) Near Real-Time provisional satellite data.

The DEA Burnt Area Characteristic Layers are combined to find areas of substantial change. These areas are converted into vectors before being masked with the fmask layer from the corresponding Sentinel-2 Near Real-Time scene.

% ## Processing steps

% ## Software

## References

Cocke A. E., Fulé P. Z., Crouse J. E. (2005) Comparison of burn severity assessments using Differenced Normalized Burn Ratio and ground data. *International Journal of Wildland Fire 14*, 189-198. [https://doi.org/10.1071/WF04010](https://doi.org/10.1071/WF04010)

Dindaroglu, T., Babur, E., Yakupoglu, T., Rodrigo-Comino, J. and Cerdà, A., (2021) Evaluation of geomorphometric characteristics and soil properties after a wildfire using Sentinel-2 MSI imagery for future fire-safe forest. *Fire Safety Journal (122)*. [https://doi.org/10.1016/j.firesaf.2021.103318](https://doi.org/10.1016/j.firesaf.2021.103318).

Huete,  A.R., Jackson, R.D., (1987) Suitability of spectral indices for evaluating vegetation characteristics on arid rangelands, *Remote Sensing of Environment, Volume 23( 2),* (213), [https://doi.org/10.1016/0034-4257(87)90038-1](https://doi.org/10.1016/0034-4257(87)90038-1)

Jin, S., Yang, L., Danielson, P., Homer, C., Fry, J. and Xian, G.  (2013). A comprehensive change detection method for updating the National Land Cover Database to circa 2011. *Remote Sensing of Environment* *132*. (159-175).  [https://doi.org/10.1016/j.rse.2013.01.012](https://doi.org/10.1016/j.rse.2013.01.012)

Keeley, J. E. (2009). Fire intensity, fire severity and burn severity: A brief review and suggested usage. *International Journal of Wildland Fire*, *18*(1), 116–126. [https://doi.org/10.1071/WF07049](https://doi.org/10.1071/WF07049)

Krause, C. E., Newey, V., Alger, M, J., Lymburner, L., (2021). Mapping and Monitoring the Multi-Decadal Dynamics of Australia’s Open Waterbodies Using Landsat, *Remote Sensing*. 13(8), 1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437)

Rahman, S., Chang, H.C., Hehir, W., Magilli, C. and Tomkins, K., (2018) Inter-Comparison of Fire Severity Indices from Moderate (Modis) and Moderate-To-High Spatial Resolution (Landsat 8 & Sentinel-2A) Satellite Sensors. In *IGARSS 2018-2018 IEEE International Geoscience and Remote Sensing Symposium* (2873-2876).  [https://doi.org/](https://doi.org/10.1109/IGARSS.2018.8518449)[10.1109/IGARSS.2018.8518449](https://doi.org/10.1109/IGARSS.2018.8518449)

Rikimaru, A., Roy, P.S. and Miyatake, S., (2002). Tropical forest cover density mapping. *Tropical ecology*, *43*(1), (39-47). [https://www.tropecol.com/pdf/open/PDF\_43\_1/43104.pdf](https://www.tropecol.com/pdf/open/PDF_43_1/43104.pdf)

Roberts, D., Wilford, J. & Ghattas, O. (2019). Exposed soil and mineral map of the Australian continent revealing the land at its barest. *Nature Communications* *10*, Article 5297. [https://doi.org/10.1038/s41467-019-13276-1](https://doi.org/10.1038/s41467-019-13276-1)

Rouse, J.W., Haas, R.H., Schell, J.A. and Deering, D.W., (1974). Monitoring vegetation systems in the Great Plains with ERTS. [*NASA special publication*, *351*(1974), (309)](https://ntrs.nasa.gov/citations/19740022614).

United Nations, *Normalized Burn Ratio (NBR),* Office for Outer Space Affairs  
UN-SPIDER Knowledge Portal. [https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio)

van Wagtendonk, J.W.,  Root, R.R., Key, C. H., (2004) Comparison of AVIRIS and Landsat ETM+ detection capabilities for burn severity, *Remote Sensing of Environment, 92 (3),* (397-408) [https://doi.org/10.1016/j.rse.2003.12.015](https://doi.org/10.1016/j.rse.2003.12.015)

