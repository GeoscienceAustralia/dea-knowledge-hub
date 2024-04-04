## Background

Intertidal environments contain many important ecological habitats such as sandy beaches, tidal flats, rocky shores, and reefs. These environments also provide many valuable benefits such as storm surge protection, carbon storage, and natural resources. 

Intertidal zones are being increasingly faced with threats including coastal erosion, land reclamation (e.g. port construction), and sea level rise. These regions are often highly dynamic, and accurate, up-to-date elevation data describing the changing topography and extent of these environments is needed. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.

The intertidal zone also forms a critical habitat and foraging ground for migratory shore birds and other species. An improved characterisation of the exposure patterns of these dynamic environments is important to support conservation efforts and to gain a better understanding of migratory species pathways.

The DEA Intertidal Suite provides annual continental-scale elevation and exposure product layers for Australia’s intertidal zone, mapped at a 10 m resolution, from DEA’s archive of open-source Landsat and Sentinel-2 satellite data. These intertidal products enable users to better monitor and understand some of the most dynamic regions of Australia’s coastlines.

## Applications

* Integration with existing topographic and bathymetric data to seamlessly map the elevation of the coastal zone. 

* Providing baseline elevation data to assist coastal hazard impact assessment from extreme weather and inundation events. 

* Investigating coastal erosion and sediment transport processes. 

* Supporting habitat mapping and modelling for coastal ecosystems extending across the terrestrial to marine boundary. 

* Characterise the spatio-temporal exposure patterns of the intertidal zone to support migratory species studies and applications. 

## Technical Information

### DEA Intertidal features

The DEA Intertidal product suite contains 3 core product layers, 7 tidal attribute (ta) layers, and 2 quality assessment (qa) layers, all provided as continental 10 m resolution GeoTIFFs for the Australian coastal and intertidal region.

All datasets are produced annually from a 3-year composite of input data from the combined Sentinel-2 and Landsat 7, 8, and 9 DEA Collection 3 surface reflectance products. The product time series commences from 2016, with datasets labelled by the middle year of data. For example, the 2017 layer combines data from 2016, 2017, and 2018. Updates to the product suite are scheduled annually. 

### What this product offers

The DEA Intertidal product suite is the next generation of intertidal products developed in DEA. It improves on the DEA Intertidal Elevation Model (also known as the [National Intertidal Digital Elevation Model](/data/product/dea-intertidal-elevation-landsat/) or NIDEM)  (Bishop-Taylor et al., 2019) and adds several new features and products to help users better understand the intertidal environment.

NIDEM was the first 3D model of Australia’s intertidal zone &mdash; the area of coastline exposed and flooded by ocean tides. The DEA Intertidal suite fundamentally changes and improves the way in which the intertidal zone is modelled compared to the original NIDEM elevation model: 

* The addition of Sentinel-2 data improves the spatial resolution of the model to 10 m, compared to the 25m of the original NIDEM.

* Incorporation of a new pixel-based method supports a reduction in the temporal epoch of the product to 3 years (in comparison to 28 years in NIDEM), improving the ability to capture the current state of dynamic coastal environments and enabling ‘change over time' applications using annual epochs.

* Quantification of the vertical uncertainty of the elevation model.

* An Intertidal Exposure model at 10 m resolution to examine the spatiotemporal patterns of exposure and inundation across the intertidal zone, supporting migratory species studies and habitat mapping applications.

* Tidal metrics to enable users to understand the varied ranges and distributions of tidal stages observed by the Landsat and Sentinel-2 satellites across Australia, and how this information can be used to better understand and interpret the products.

* The implementation of an ensemble tidal modelling approach, acknowledging the wide range of global and regional tide models available and their varying performance across different regions of Australia. See [Ensemble Tidal Modelling](./?tab=details#ensemble-tidal-modelling).

### File Naming Convention 

File names use the format:

```text
{product_name}_{x tile code}{y tile code}_{year--frequency}_{dataset maturity}_{layer_name}.tif
```

For example: 

```text
ga_s2ls_intertidal_cyear_3_x082y139_2022--P1Y_final_elevation.tif
```

### Code repositories

* [DEA Intertidal Github](https://github.com/GeoscienceAustralia/dea-intertidal) &mdash; A codebase for DEA Intertidal product generation workflows 
* [DEA Tools Github](https://github.com/GeoscienceAustralia/dea-notebooks) &mdash; Parallelised tide modelling and data manipulation tools 
* [PyTMD Github](https://github.com/tsutterley/pyTMD) &mdash; Python-based tidal prediction software 

### Core Product Layers 

#### DEA Intertidal Elevation

:::{list-table}
:class: small

* - **Name**
  - `elevation`
* - **Data type**
  - `float32`
* - **Units**
  - `metres above MSL`
* - **'No data' value**
  - `NaN`
:::

DEA Intertidal Elevation provides elevation in metre units relative to modelled Mean Sea Level for each pixel of the satellite-observed exposed intertidal zone across the Australian coastline. The elevation model is generated from DEA Landsat and Sentinel-2 surface reflectance data from each 3-year composite period, utilising a pixel-based approach based on Ensemble Tidal Modelling. For every pixel, the time series of surface reflectance data is converted to the Normalised Difference Water Index (NDWI) and each observation tagged with the tidal height modelled at the time of acquisition by the satellite. A rolling median is applied from low to high tide to reduce noise (such as white water, sunglint, and non-tidal water level variability), then analysed to identify the tide height at which the pixel transitions from dry to wet. This tide height represents the elevation of the pixel. 

#### DEA Intertidal Elevation Uncertainty

:::{list-table}
:class: small

* - **Name**
  - `elevation_uncertainty`
* - **Data type**
  - `float32`
* - **Units**
  - `metres`
* - **'No data' value**
  - `NaN`
:::

DEA Intertidal Elevation Uncertainty provides a measure of the quality of each modelled elevation value in metre units. Uncertainty is calculated by assessing how cleanly the modelled elevation separates satellite observations into dry and wet observations. This is achieved by identifying satellite observations that were misclassified by the modelled elevation (for instance, pixels that were observed as wet at tide heights lower than the modelled elevation, or alternately, observed as dry at higher tide heights). The spread of tide heights from these misclassified observations is summarised using a robust Median Absolute Deviation (MAD) statistic, and reported as $0.5 \times MAD$ to represent one-sided uncertainty bounds (i.e. ± uncertainty on either side of the pixel's elevation). Common causes of high elevation uncertainty can be poor tidal model performance, rapidly changing intertidal morphology, or noisy underlying satellite data.  

#### DEA Intertidal Exposure

:::{list-table}
:class: small

* - **Name**
  - `exposure`
* - **Data type**
  - `uint8`
* - **Units**
  - `percent`
* - **'No data' value**
  - `255`
:::

DEA Intertidal Exposure models the relative amount of time that any intertidal pixel is exposed from water coverage. Exposure is calculated by comparing the pixel elevation back against a high temporal resolution model of tide heights for that location, based on the Ensemble Tidal Modelling approach. The Exposure dataset reflects the percentage of time any given pixel of known elevation is exposed from tidal inundation. This is calculated as the fraction of exposed observations relative to the total number of observations generated in the high temporal resolution tidal model for the 3-year product epoch.   

### Tidal Attribute Layers (ta)

#### DEA Intertidal tidal spread

:::{list-table}
:class: small

* - **Name**
  - `ta_spread`
* - **Data type**
  - `uint8`
* - **Units**
  - `percent`
* - **'No data' value**
  - `255`
:::

The tidal spread dataset provides the percentage of the full astronomical tidal range observed by the time series of satellite observations at each pixel (see Figure 1a). DEA Intertidal Spread takes the concept of satellite tide bias, introduced in Bishop-Taylor et al (2019), and applies it at a pixel scale to demonstrate the fraction of the full tide range that was sensor observed during the analysis epoch at that location. In this work, the astronomical tide range is defined as that modelled by the ensemble tide modelling approach. 

#### DEA Intertidal low tide offset

:::{list-table}
:class: small

* - **Name**
  - `ta_offset_low`
* - **Data type**
  - `uint8`
* - **Units**
  - `percent`
* - **'No data' value**
  - `255`
:::

The low tide offset dataset quantifies the proportion of the lowest tides not observed at any time during the analysis epoch by satellites at each pixel (as a percentage of the astronomical tide range). It is calculated by measuring the offset between the lowest astronomical tide (LAT) and the lowest satellite-observed tide (LOT; see Figure 1b). A high value indicates that DEA Intertidal datasets may not map the lowest regions of the intertidal zone.  

#### DEA Intertidal high tide offset

:::{list-table}
:class: small

* - **Name**
  - `ta_offset_high`
* - **Data type**
  - `uint8`
* - **Units**
  - `percent`
* - **'No data' value**
  - `255`
:::

The high tide offset dataset quantifies the proportion of the highest tides not observed at any time during the analysis epoch by satellites at each pixel (as a percentage of the astronomical tide range). It is calculated by measuring the offset between the highest astronomical tide (HAT) and the highest satellite-observed tide (HOT; see Figure 1c). A high value indicates that DEA Intertidal datasets may not map the highest regions of the intertidal zone.  

:::{figure} /_files/dea-intertidal/tidalattributes.*
:alt: Tidal Attributes Description Figure

Figure 1 – Illustration of the concept of observed tide heights (dots corresponding to satellite acquisition time) compared to the full modelled tidal range (blue lines). Descriptions of Spread (a), Lowtide offset (b), and Hightide offset (c) are detailed in the text.  
:::

#### DEA Intertidal lowest observed tide

:::{list-table}
:class: small

* - **Name**
  - `ta_lot`
* - **Data type**
  - `float32`
* - **Units**
  - `metres above MSL`
* - **'No data' value**
  - `NaN`
:::

The lowest observed tide dataset maps the lowest satellite-observed tide (LOT) of the satellite time series at each pixel during the analysis epoch, based on the Ensemble Tidal Modelling.  

#### DEA Intertidal highest observed tide

:::{list-table}
:class: small

* - **Name**
  - `ta_hot`
* - **Data type**
  - `float32`
* - **Units**
  - `metres above MSL`
* - **'No data' value**
  - `NaN`
:::

The highest observed tide dataset maps the highest satellite-observed tide (HOT) of the satellite time-series at each pixel during the analysis epoch, based on the Ensemble Tidal Modelling.  

#### DEA Intertidal lowest astronomical tide

:::{list-table}
:class: small

* - **Name**
  - `ta_lat`
* - **Data type**
  - `float32`
* - **Units**
  - `metres above MSL`
* - **'No data' value**
  - `NaN`
:::

The lowest astronomical tide dataset maps the lowest astronomical tide (LAT) for each pixel, as modelled by the Ensemble Tidal Model for the analysis epoch. Note that the LAT modelled for each individual analysis epoch may differ from the LAT modelled across ‘all time’ for any given location.

#### DEA Intertidal highest astronomical tide

:::{list-table}
:class: small

* - **Name**
  - `ta_hat`
* - **Data type**
  - `float32`
* - **Units**
  - `metres above MSL`
* - **'No data' value**
  - `NaN`
:::

The highest astronomical tide dataset maps the highest astronomical tide (HAT) for each pixel, as modelled by the Ensemble Tidal Model for the analysis epoch.Note that the HAT modelled for each individual analysis epoch may differ from the HAT modelled across ‘all time’ for any given location. 

### Quality Assessment Layers (qa) 

##### DEA Intertidal NDWI frequency

:::{list-table}
:class: small

* - **Name**
  - `qa_ndwi_freq`
* - **Data type**
  - `uint8`
* - **Units**
  - `percent`
* - **'No data' value**
  - `255`
:::

This quality assessment band provides the inundation frequency of each pixel across the analysis epoch, as measured by NDWI. High values indicate that a pixel was observed as being inundated regularly in satellite observations. 

#### DEA Intertidal NDWI correlation

:::{list-table}
:class: small

* - **Name**
  - `qa_ndwi_corr`
* - **Data type**
  - `float32`
* - **Units**
  - `correlation`
* - **'No data' value**
  - `NaN`
:::

This quality assessment dataset provides pixel-level Pearson correlations between NDWI satellite observations and tide heights from the Ensemble Tidal Model over the analysis epoch. High values indicate that patterns of inundation were positively correlated with tide, indicating that the pixel was likely to be tidally influenced. 

### Ensemble Tidal Modelling

The Ensemble Tidal Modelling approach was implemented to account for the varying performance and biases of 7 commonly used global tidal models when applied to the various regions and tidal regimes of continental Australia (Figure 2).

The tidal models listed below were implemented within the DEA environment using the [pyTMD](https://github.com/tsutterley/pyTMD) and [DEA Tools](https://github.com/GeoscienceAustralia/dea-notebooks) Python packages: 

 
* FES2014 (Lydard et al., 2021) 
* FES2012 (Carrère et al., 2012) 
* TPXO8-atlas-v1 (Egbert & Erofeeva, 2002) 
* TPXO9-atlas-v5  (Egbert & Erofeeva, 2002) 
* EOT20 (Hart-Davis et al., 2021) 
* HAMTIDE11 (Taguchi et al., 2014) 
* GOT4.10 (Ray, 2013) 

The ensemble process utilises ancillary data (in this case, the correlation of the NDWI values to each individual tidal model output) to weight and selects the top 3 tidal models for a given location. A single ensemble tidal output from these 3 optimal models is then generated for use in all downstream product workflows.   

:::{figure} /_files/dea-intertidal/ensembletides.*
:alt: Ensemble tide validation Figure

Figure 2 – Global Tide Models validated at Australian Sea Level Monitoring Tide Gauges 
:::

## Lineage

The DEA Intertidal product suite extends the concepts developed in the DEA Intertidal Elevation (NIDEM) product, integrating higher resolution 10 m Sentinel-2 data with the original 30 m Landsat data to create annual elevation models and exposure product layers for Australia’s intertidal zone.   

This shift to a more dynamic product suite is achieved through a pixel-based algorithm, replacing the waterline interpolation methods of NIDEM, and an improved tidal modelling process to better leverage the increased data resolution and density provided by the inclusion of Sentinel-2 data.  

## Processing Steps

* Satellite data from Sentinel-2A and -2B, Landsat 7, 8, and 9 are loaded. 

* Satellite data cloud masked and converted to NDWI. 

* Tides modelled for every satellite pixel using [Ensemble Tidal Modelling](#ensemble-tidal-modelling). 

* Satellite data filtered to probable intertidal pixels using NDWI inundation frequency and tide correlation and masked to remove deep ocean water using bathymetry from [GA Australian 250m Bathymetry and Topography Grid](https://explorer.dea.ga.gov.au/products/ga_ausbathytopo250m_2023) (Beaman, 2023). 

* Pixel-based rolling median applied from low to high tide. 

* Intertidal elevation modelled based on tide height at which a rolling median transitions from dry to wet. 

* Intertidal elevation uncertainty modelled based on how cleanly modelled elevation divides satellite observations into dry and wet. 

* Intertidal exposure calculated by comparing Intertidal elevation against high frequency modelled tides. 

* Tidal metrics calculated by comparing satellite-observed tides against high frequency modelled tides. 

## References

Beaman, R. 2023. AusBathyTopo 250m (Australia) 2023 Grid - A High-resolution Depth Model for Australia (20230004C). Geoscience Australia, Canberra. 

Bishop-Taylor, R., Sagar, S., Lymburner, L., Beaman, R.J., 2019. Between the tides: Modelling the elevation of Australia’s exposed intertidal zone at continental scale. *Estuarine, Coastal and Shelf Science* 23, 115–128.

Carrère L., F. Lyard, M. Cancet, A. Guillot, L. Roblou, 2012. FES2012: A new global tidal model taking advantage of nearly 20 years of altimetry, *Proceedings of meeting "20 Years of Altimetry"*, Venice 2012 

Egbert, G.D., Erofeeva, S.Y., 2002. Efficient Inverse Modeling of Barotropic Ocean Tides. *J. Atmospheric Ocean. Technol.* 19, 183–204.

Hart-Davis, M.G., Piccioni, G., Dettmering, D., Schwatke, C., Passaro, M., Seitz, F., 2021. EOT20: a global ocean tide model from multi-mission satellite altimetry. *Earth System Science Data* 13, 3869–3884. 

Lyard, F.H., Allain, D.J., Cancet, M., Carrère, L., Picot, N., 2021. FES2014 global ocean tide atlas: design and performance. *Ocean Science* 17, 615–649. 

Sagar, S., Roberts, D., Bala, B., Lymburner, L., 2017. Extracting the intertidal extent and topography of the Australian coastline from a 28 year time series of Landsat observations. *Remote Sensing of Environment* 195, 153–169.

Ray, R. D. (2013). Precise comparisons of bottom-pressure and altimetric ocean tides. *Journal of Geophysical Research: Oceans*, 118(9), 4570–4584. 

Taguchi, E., Stammer, D., and Zahel, W. (2014), Inferring deep ocean tidal energy dissipation from the global high-resolution data-assimilative HAMTIDE model, *J. Geophys. Res. Oceans*, 119, 4573– 4592. 

