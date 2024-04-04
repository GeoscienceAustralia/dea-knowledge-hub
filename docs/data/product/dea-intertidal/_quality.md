## Accuracy

Product accuracy was validated against high resolution external Digital Elevation Model (DEM) data sources from across the Australian coastline, including aerial LiDAR and multibeam bathymetry datasets. These included datasets from the following sources: 

* Aerial LiDAR hosted on Geoscience Australia’s ELVIS platform 
* Aerial LiDAR and multibeam datasets hosted on the WA Bathymetry Portal 
* Aerial LiDAR over Gulf of Carpentaria tidal flats, Northern Territory Government 
* Aerial LiDAR over the Dampier Archipelago, University of Western Australia 
* Aerial LiDAR over Gulf of Carpentaria, Airborne Research Australia 

To create a consistent basis for comparison against DEA Intertidal outputs, data from each validation data source was mosaicked and reprojected into 10 m DEM rasters. These rasters were then combined into annual continental-scale rasters corresponding to each year of data in the DEA Intertidal product suite. Because these DEMs had varied coverage of the intertidal zone due to being acquired across a range of tidal conditions, true exposed intertidal pixels were identified via a combination of manual digitisation using underlying high-resolution basemap data as a reference, and automated filtering to pixels with elevations between local Lowest and Highest Astronomical Tide. Additional areas of ocean or ‘no data’ contamination were masked using a simple slope rule, considering only pixels with a non-zero slope as viable candidates for intertidal pixels. 

 To evaluate the accuracy of DEA Intertidal Elevation, we calculated RMSE, MAE, correlation, bias, and R-squared statistics by comparing modelled DEA Intertidal Elevation outputs with validation data from the relevant year (e.g. 2021 DEA Intertidal Elevation data was compared against 2021 validation data). To provide insights into product performance across different coastal environments, this analysis was conducted separately on microtidal (tide range &lt; 2 m), mesotidal (2&ndash;4 m) and macrotidal (&gt; 4 m) coastlines (Table 1, Figure 3). 

|             | Microtidal | Mesotidal | Macrotidal |
|-------------|------------|-----------|------------|
| Correlation | 0.6        | 0.86      | **0.96**   |
| R-squared   | 0.36       | 0.74      | **0.92**   |
| RMSE (m)    | 0.28       | **0.27**  | 0.28       |
| MAE (m)     | 0.21       | 0.21      | **0.20**   |
| Bias (m)    | 0.14       | 0.16      | **0.12**   |
| Slope       | 0.44       | 0.80      | **1.03**   |

Table 1 &mdash; DEA Intertidal Elevation validation statistics comparing performance across microtidal, mesotidal and macrotidal coastlines. 

:::{figure} /_files/dea-intertidal/tiderangevalidation.*
:alt: Validation at different tidal ranges

Figure 3 &mdash; DEA Intertidal Elevation validation heatmaps comparing performance across microtidal, mesotidal and macrotidal coastlines. 

### Caveats and limitations

* Model performance improved with increasing tide range, being lowest in microtidal coastlines and highest in mesotidal and macrotidal coastlines. Due to the limited spatial extent of the intertidal zone in microtidal environments and the dominance of non-tidal water level influences (e.g. storm surge and ocean waves in high energy wave dominated environments), DEA Intertidal should be used with caution in microtidal environments. 

* DEA Intertidal relies on accurate tide modelling for reliable results. Although the Ensemble Tidal Modelling approach used in this product attempts to obtain the best local tide modelling data for any given location, areas of poor quality tide modelling still remain. This is particularly the case in areas of complex and unpredictable tide dynamics, such as embayments and estuaries where global ocean tide modelling results may produce highly inaccurate outputs. In these environments, modelled elevations and exposure should be used with caution and evaluated with reference to modelled elevation uncertainty data. Examples of areas affected by poor quality tide modelling inputs include: 

    * Western Port, Victoria 
    * Corner Inlet, Victoria 
    * Broad Sound and Shoalwater Bay, Queensland 
    * Van Diemen Gulf, Northern Territory 
    * Torres Strait Islands, Queensland

* Due to biases in the tidal coverage of satellite sensors like Landsat and Sentinel-2, DEA Intertidal outputs are unlikely to cover the full extent of the intertidal zone from Lowest to Highest Astronomical tide (e.g. Figure 2). These tidal biases can be evaluated using the product’s Tidal Attribute Layers which highlight regions where DEA Intertidal will underestimate the lower, upper or full extent of the intertidal zone. 

* Areas of false positive intertidal data over water exist in areas with low satellite coverage and high levels of environmental or sensor noise. Areas affected include: 

    * Recherche Archipelago, Western Australia 
    * South-eastern Eyre Peninsula, South Australia 
    * Torres Strait Islands, Queensland 

* Areas of highly turbid water can be incorrectly mapped as intertidal terrain, particularly if temporal patterns of turbidity correlate with tidal dynamics. Areas affected by turbidity include:

    * King Sound, Western Australia
    * Cambridge Gulf, Western Australia
    * Joseph Bonaparte Gulf, Northern Territory
    * Daly River, Northern Territory
    * Broad Sound, Queensland


## Quality Assurance

Code used to generate DEA Intertidal is run against automated integration tests to ensure that product quality is maintained as updates and improvements are made. These tests verify that the entire product generation workflow is performing as expected, and track changes in product accuracy over time: https://github.com/GeoscienceAustralia/dea-intertidal/tree/main/tests 
