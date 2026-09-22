## Accuracy

Product accuracy was validated against high resolution external Digital Elevation Model (DEM) data sources from across the Australian coastline, including aerial LiDAR and multibeam bathymetry datasets: 

:::{table} Table 1. Data sources used to validate DEA Intertidal.

| Source | Type | Temporal coverage | Spatial coverage |
|--------|------|-------------------|------------------|
| Elvis Elevation and Depth portal | Aerial LiDAR<br>Multibeam bathymetry | 2016-2022 | Continental |
| Airborne Research Australia Gulf of Carpentaria Airborne Mangrove Dieback Mapping Project | Aerial LiDAR | 2017 | Regional (Gulf of Carpentaria) |
| National Indigenous Australians Agency 2021 Gulf of Carpentaria LiDAR survey | Aerial LiDAR | 2021 | Regional (Gulf of Carpentaria) |
| University of Western Australia Dampier Archipelago bathymetric LiDAR | Aerial LiDAR | 2017 | Regional (Dampier Archipelago) |
| Victoria Department of Energy, Environment and Climate Action 10 m VIC Coastal DEM | Aerial LiDAR | 2021 | Regional (Victoria) |
| Western Australia Department of Transport WA Bathymetry Portal | Aerial LiDAR<br>Multibeam bathymetry | 2016-2022 | Regional (Western Australia) |
:::

For a consistent comparison, data from all validation data sources were mosaicked and reprojected into annual 10 m continental-scale DEM rasters, and transformed to match the Mean Sea level vertical datum of DEA Intertidal. To evaluate accuracy, we calculated RMSE, MAE, correlation, bias, and R-squared statistics by comparing DEA Intertidal Elevation against validation data from the same year. To provide insights into product performance across different coastal environments, this analysis was conducted separately on microtidal (tide range &lt; 2 m), mesotidal (2&ndash;4 m) and macrotidal (&gt; 4 m) coastlines (Table 2, Figure 7). 

For a detailed description of the validation approach, refer to [Bishop-Taylor et al., (2026)](https://doi.org/10.1016/j.rse.2026.115663).

:::{table} Table 2. Validation statistics assessing the performance of DEA Intertidal against independent validation data across macro-, meso- and microtidal intertidal environments. RMSE, MAE and bias statistics are given in both absolute units (m), and as a percentage (%) of the local tide range.

|                 | Macrotidal            | Mesotidal             | Microtidal           |
|-----------------|-----------------------|-----------------------|--------------------- |
| **n**           | 17.5 sq. km           | 703.5 sq. km          | 26.2 sq. km          |
| **Correlation** | 0.96                  | 0.90                  | 0.60                 |
| **R-squared**   | 0.93                  | 0.80                  | 0.36                 |
| **RMSE**        | 0.32 m (5%)           | 0.32 m (10%)          | 0.26 m (18%)         |
| **MAE**         | 0.23 m (4%)           | 0.25 m (8%)           | 0.20 m (13%)         |
| **Bias**        | 0.20 m (3%)           | 0.20 m (6%)           | 0.12 m (8%)          |

:::

:::{figure} /_files/dea-intertidal/tiderangevalidation.*
:alt: Validation at different tidal ranges

Figure 7. Comparison of DEA Intertidal elevation against independent validation data. Panels (a-c) show modelled versus validation elevations across macro-, meso-, and microtidal environments. Panels (d-f) show errors grouped by (d) intertidal elevation, (e) intertidal slope, and (f) clear satellite observations at each pixel. Distributions are visualised by interquartile range (boxes) and 10-90th percentiles (whiskers).
:::

### Caveats and limitations

For more detail about DEA Intertidal caveats and limitations, refer to [Bishop-Taylor et al., (2026)](https://doi.org/10.1016/j.rse.2026.115663).

* DEA Intertidal covers the exposed intertidal zone which includes sandy beaches and shores, tidal flats and rocky shores and reefs. The model excludes intertidal vegetation communities such as mangroves.

* Although DEA Intertidal's absolute elevation mapping accuracy is similar across all environments (Table 2), accuracy relative to the total tide range is significantly greater in meso-tidal and macro-tidal environments. Due to the narrow intertidal zone in microtidal environments and the dominance of non-tidal water level influences like storm surge and ocean waves, DEA Intertidal should be used with caution in microtidal environments.

* DEA Intertidal relies on accurate tide modelling for reliable results. Although the Ensemble Tidal Modelling approach used in this product attempts to obtain the best local tide modelling data for any given location, areas of poor quality tide modelling still remain. This is particularly the case in areas of complex and unpredictable tide dynamics, such as embayments and estuaries where global ocean tide modelling results may produce highly inaccurate outputs. In these environments, modelled elevations and exposure should be used with caution and evaluated with reference to modelled elevation uncertainty data. Examples of areas affected by poor quality tide modelling inputs include: 

    * Western Port, Victoria 
    * Corner Inlet, Victoria 
    * Broad Sound and Shoalwater Bay, Queensland 
    * Van Diemen Gulf, Northern Territory 
    * Torres Strait Islands, Queensland

* Due to biases in the tidal coverage of satellite sensors like Landsat and Sentinel-2, DEA Intertidal outputs rarely cover the full extent of the intertidal zone from Lowest to Highest Astronomical tide (e.g. Figure 6). These tidal biases can be evaluated using the product's Tidal Attribute Layers which highlight regions where DEA Intertidal will underestimate the lower, upper or full extent of the intertidal zone. 

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

* The DEA Intertidal Extents layer classifies two categories of intertidal pixels. Rigorous methods and conservative thresholds are used to identify pixels that are highly likely to be intertidal and are classed as "high confidence" intertidal pixels. Pixels that are less certain to be intertidal (i.e those that meet most but not all of the qualifying criteria) are instead classified as "low confidence" intertidal. These "low confidence" pixels are not included in our Elevation and Exposure datasets. Caution should be applied when interpreting or using "low confidence" intertidal pixel data, as this class is likely to include noisy and inaccurate data.

* Several DEA Intertidal tidal metric layers (e.g. "ta_spread", "ta_offset_low", "ta_offset_high", "ta_lot", "ta_hot") are affected by minor artefacts along processing tile grid boundaries. These artefacts are being investigated, and will likely be fixed in future product updates.

## Quality Assurance

Code used to generate DEA Intertidal is [run against automated integration tests](https://github.com/GeoscienceAustralia/dea-intertidal/tree/main/tests 
) to ensure that product quality is maintained as updates and improvements are made. These tests verify that the entire product generation workflow is performing as expected, and track changes in product accuracy over time.

## References

Bishop-Taylor, R., Phillips, C., Sagar, S., & Newey, V., 2026. Time and tide: Mapping the changing 3D shape of Australia's dynamic intertidal zone using time series satellite data. *Remote Sensing of Environment*, 347, 115663. https://doi.org/10.1016/j.rse.2026.115663