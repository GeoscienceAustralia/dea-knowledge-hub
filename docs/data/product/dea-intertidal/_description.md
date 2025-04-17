## Background

Intertidal environments contain many important ecological habitats such as sandy beaches, tidal flats, rocky shores, and reefs. These environments also provide many valuable benefits such as storm surge protection, carbon storage, and natural resources. 

Intertidal zones are being increasingly faced with threats including coastal erosion, land reclamation (e.g. port construction), and sea level rise. These regions are often highly dynamic, and accurate, up-to-date elevation data describing the changing topography and extent of these environments is needed. 

The intertidal zone also forms a critical habitat and foraging ground for migratory shore birds and other species. An improved characterisation of the exposure patterns of these dynamic environments is important to support conservation efforts and to gain a better understanding of migratory species pathways. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.

The DEA Intertidal product suite provides annual continental-scale elevation and exposure product layers for Australia's exposed intertidal zone, mapped at a 10 m resolution from DEA's archive of open-source Landsat and Sentinel-2 satellite data. The exposed intertidal zone consists of coastal  regions periodically inundated by tidal flows, not including areas obscured by vegetation cover such as mangroves. These intertidal products enable users to better monitor and understand some of the most dynamic regions of Australia's coastlines.

## Applications

* Integration with existing topographic and bathymetric data to seamlessly map the elevation of the coastal zone. 

* Providing baseline elevation data to assist coastal hazard impact assessment from extreme weather and inundation events. 

* Investigating coastal erosion and sediment transport processes. 

* Supporting habitat mapping and modelling for coastal ecosystems extending across the terrestrial to marine boundary. 

* Characterise the spatio-temporal exposure patterns of the intertidal zone to support migratory species studies and applications. 

## Technical Information

### DEA Intertidal features

The DEA Intertidal product suite contains 4 core product layers, 7 tidal attribute (`ta`) layers, and 4 quality assessment (`qa`) layers, all provided as continental 10 m resolution GeoTIFFs for the Australian coastal and intertidal region.

All datasets are produced annually from a 3-year composite of input data from combined Sentinel-2 and Landsat DEA Collection 3 surface reflectance products. The product time series commences from 2016, with datasets labelled by the middle year of data. For example, the 2017 layer combines data from 2016, 2017, and 2018. Updates to the product suite are scheduled annually. 

### What this product offers

The DEA Intertidal product suite is the next generation of intertidal products developed in DEA. It improves on the DEA Intertidal Elevation Model (also known as the [National Intertidal Digital Elevation Model](/data/product/dea-intertidal-elevation-landsat/) or NIDEM)  (Bishop-Taylor et al., 2019) and adds several new features and products to help users better understand the intertidal environment.

NIDEM was the first 3D model of Australia’s intertidal zone &mdash; the area of coastline exposed and flooded by ocean tides. The DEA Intertidal suite fundamentally changes and improves the way in which the exposed intertidal zone is modelled compared to the original NIDEM elevation model: 

* The addition of Sentinel-2 data improves the spatial resolution of the model to 10 m, compared to the 25m of the original NIDEM.
* Incorporation of a new pixel-based method supports a reduction in the temporal epoch of the product to 3 years (in comparison to 28 years in NIDEM), improving the ability to capture the current state of dynamic coastal environments and enabling ‘change over time' applications using annual epochs.
* Quantification of the vertical uncertainty of the elevation model.
* An Intertidal Exposure model at 10 m resolution to examine the spatiotemporal patterns of exposure and inundation across the intertidal zone, supporting migratory species studies and habitat mapping applications.
* Tidal metrics to enable users to understand the varied ranges and distributions of tidal stages observed by the Landsat and Sentinel-2 satellites across Australia, and how this information can be used to better understand and interpret the products.
* The implementation of an ensemble tidal modelling approach, acknowledging the wide range of global and regional tide models available and their varying performance across different regions of Australia. See [Ensemble Tidal Modelling](./?tab=description#ensemble-tidal-modelling).
* A coastal extents classification model that identifies five categorical classes to compliment the Elevation and Exposure products. This helps users to characterise different environments in the coastal zone in terms of their inundation characteristics and drivers, mapping confidence and nature of water cover.

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

* [DEA Intertidal GitHub repository](https://github.com/GeoscienceAustralia/dea-intertidal) &mdash; A codebase for DEA Intertidal product generation workflows 
* [EO-Tides GitHub repository](https://github.com/GeoscienceAustralia/eo-tides) &mdash; A codebase for integrating satellite Earth observations with tide modelling
* [DEA Tools GitHub repository](https://github.com/GeoscienceAustralia/dea-notebooks) &mdash; Earth observation data manipulation tools 
* [PyTMD GitHub repository](https://github.com/tsutterley/pyTMD) &mdash; Python-based tidal prediction software 

### Core Product Layers 

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

#### DEA Intertidal Elevation (elevation)

DEA Intertidal Elevation (Figure 1) provides elevation in metre units relative to modelled Mean Sea Level for each pixel of the satellite-observed exposed intertidal zone across the Australian coastline. The elevation model is generated from DEA Landsat and Sentinel-2 surface reflectance data from each 3-year composite period, utilising a pixel-based approach based on [Ensemble Tidal Modelling](#ensemble-tidal-modelling). For every pixel, the time series of surface reflectance data is converted to the Normalised Difference Water Index (NDWI) and each observation tagged with the tidal height modelled at the time of acquisition by the satellite. A rolling median is applied from low to high tide to reduce noise (such as white water, sunglint, and non-tidal water level variability), then analysed to identify the tide height at which the pixel transitions from dry to wet. This tide height represents the elevation of the pixel.

:::{figure} /_files/dea-intertidal/DEAIntertidal_layer_elevation.*
:alt: DEA Intertidal Elevation layer

Figure 1 &mdash; DEA Intertidal Elevation, with low elevation values shown in dark colours and high elevation shown in light colours.
:::

#### DEA Intertidal Elevation Uncertainty (elevation_uncertainty)

DEA Intertidal Elevation Uncertainty (Figure 2) provides a measure of the quality of each modelled elevation value in metre units. Uncertainty is calculated by assessing how cleanly the modelled elevation separates satellite observations into dry and wet observations. This is achieved by identifying satellite observations that were misclassified by the modelled elevation (for instance, pixels that were observed as wet at tide heights lower than the modelled elevation, or alternately, observed as dry at higher tide heights). The spread of tide heights from these misclassified observations is summarised using a robust Median Absolute Deviation (MAD) statistic, and reported as $0.5 \times MAD$ to represent one-sided uncertainty bounds (i.e. ± uncertainty on either side of the pixel's elevation). Common causes of high elevation uncertainty can be poor tidal model performance, rapidly changing intertidal morphology, or noisy underlying satellite data.

:::{figure} /_files/dea-intertidal/DEAIntertidal_layer_elevation_uncertainty.*
:alt: DEA Intertidal Elevation Uncertainty layer

Figure 2 &mdash; DEA Intertidal Elevation Uncertainty, with high uncertainty shown in light colours.
:::

#### DEA Intertidal Exposure (exposure)

DEA Intertidal Exposure (Figure 3) models the percentage of time that any intertidal pixel of known elevation is exposed from tidal inundation. Exposure is calculated by comparing the pixel elevation back against a high temporal resolution model of tide heights for that location, based on the [Ensemble Tidal Modelling](#ensemble-tidal-modelling) approach. Exposure percentage is calculated as the fraction of exposed observations relative to the total number of observations generated in the high temporal resolution tidal model for the 3-year product epoch.

:::{figure} /_files/dea-intertidal/DEAIntertidal_layer_exposure.*
:alt: DEA Intertidal Exposure layer

Figure 3 &mdash; DEA Intertidal Exposure, with low exposure values (i.e. rarely exposed pixels) shown in dark colours.
:::

#### DEA Intertidal Extents (extents)

DEA Intertidal Extents is a categorical dataset classifying coastal areas into five classes (Figure 4), including the satellite-observed extents of the exposed (i.e. non-vegetated) intertidal zone. This classification is based on DEA Intertidal Elevation outputs and other satellite-derived data including the inundation frequency of each pixel and correlations between inundation patterns and modelled tide heights. See [Quality Assessment Layers](quality-assessment-layers). The "intensive urban" land use summary class of the Catchment-scale Land Use Map (CLUM) (ABARES, 2021) dataset was used to mask pixel misclassifications in urban areas.
 
The class definitions of the Intertidal Extents layer are as follows:

* **Ocean and coastal waters (1)** - Pixels that are wet in 50% or more of satellite observations and are located within the coastal mask (a cost-distance connectivity mask combining elevation with distance from the ocean)
* **Exposed intertidal - low confidence (2)** - Pixels that have a correlation between tide height and NDWI of at least 0.15, and are located within the coastal mask (see Ocean and coastal waters)
* **Exposed intertidal - high confidence (3)** - Pixels that are included in the intertidal elevation dataset
* **Inland waters (4)** - Pixels that are wet in more than 50% of satellite observations, and fall outside of the coastal mask (see Ocean and coastal waters)
* **Land (5)** - Pixels that are wet in less than 50% of satellite observations

:::{figure}  /_files/dea-intertidal/DEA_Intertidal_Extents_2022.*
:alt: DEA Intertidal Extents layer
:width: 1200px

Figure 4 &mdash; DEA Intertidal Extents, the five coastal classes include ocean and coastal waters (dark blue), low confidence intertidal (yellow), high confidence intertidal (orange), inland waters (light blue) and land (white).
:::

### Tidal Attribute Layers

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

#### DEA Intertidal tidal spread (ta_spread)

The tidal spread dataset provides the percentage of the full astronomical tidal range observed by the time series of satellite observations at each pixel (see Figure 5a). DEA Intertidal Spread takes the concept of satellite tide bias, introduced in Bishop-Taylor et al (2019), and applies it at a pixel scale to demonstrate the fraction of the full tide range that was sensor observed during the analysis epoch at that location. In this work, the astronomical tide range is defined as that modelled by the [Ensemble Tidal Modelling](#ensemble-tidal-modelling) approach. 

#### DEA Intertidal low tide offset (ta_offset_low)

The low tide offset dataset quantifies the proportion of the lowest tides not observed at any time during the analysis epoch by satellites at each pixel (as a percentage of the astronomical tide range). It is calculated by measuring the offset between the lowest astronomical tide (LAT) and the lowest satellite-observed tide (LOT; see Figure 5b). A high value indicates that DEA Intertidal datasets may not map the lowest regions of the intertidal zone.

#### DEA Intertidal high tide offset (ta_offset_high)

The high tide offset dataset quantifies the proportion of the highest tides not observed at any time during the analysis epoch by satellites at each pixel (as a percentage of the astronomical tide range). It is calculated by measuring the offset between the highest astronomical tide (HAT) and the highest satellite-observed tide (HOT; see Figure 5c). A high value indicates that DEA Intertidal datasets may not map the highest regions of the intertidal zone.

:::{figure} /_files/dea-intertidal/tidalattributes.*
:alt: Tidal Attributes Description Figure

Figure 5 &mdash; Illustration of the concept of observed tide heights (dots corresponding to satellite acquisition time) compared to the full modelled tidal range (blue lines). Descriptions of Spread (a), Lowtide offset (b), and Hightide offset (c) are detailed in the text.
:::

#### DEA Intertidal lowest observed tide (ta_lot)

The lowest observed tide dataset maps the lowest satellite-observed tide (LOT) of the satellite time series at each pixel during the analysis epoch, based on [Ensemble Tidal Modelling](#ensemble-tidal-modelling).

#### DEA Intertidal highest observed tide (ta_hot)

The highest observed tide dataset maps the highest satellite-observed tide (HOT) of the satellite time-series at each pixel during the analysis epoch, based on [Ensemble Tidal Modelling](#ensemble-tidal-modelling).

#### DEA Intertidal lowest astronomical tide (ta_lat)

The lowest astronomical tide dataset maps the lowest astronomical tide (LAT) for each pixel, as modelled by the [Ensemble Tidal Model](#ensemble-tidal-modelling) for the analysis epoch. Note that the LAT modelled for each individual analysis epoch may differ from the LAT modelled across ‘all time’ for any given location.

#### DEA Intertidal highest astronomical tide (ta_hat)

The highest astronomical tide dataset maps the highest astronomical tide (HAT) for each pixel, as modelled by the Ensemble Tidal Model for the analysis epoch. Note that the HAT modelled for each individual analysis epoch may differ from the HAT modelled across ‘all time’ for any given location.

### Quality Assessment Layers

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

##### DEA Intertidal NDWI frequency (qa_ndwi_freq)

This quality assessment band provides the inundation frequency of each pixel across the analysis epoch, as measured by NDWI. High values indicate that a pixel was observed as being inundated regularly in satellite observations.

#### DEA Intertidal NDWI correlation (qa_ndwi_corr)

This quality assessment dataset provides pixel-level Pearson correlations between NDWI satellite observations and tide heights from the [Ensemble Tidal Model](#ensemble-tidal-modelling) over the analysis epoch. High values indicate that patterns of inundation were positively correlated with tide, indicating that the pixel was likely to be tidally influenced.

#### DEA Intertidal Clear Count (qa_count_clear)

This quality assessment dataset returns the number of clear and valid satellite observations for every pixel. By default, a minimum number of 5 clear and cloud-free satellite observations are required to calculate intertidal elevation and exposure.

#### DEA Intertidal Coastal Mask (qa_coastal_mask)

This quality assessment dataset returns the coastal mask used to support the identification of high confidence intertidal pixels in DEA Intertidal Elevation and to separate coastal from inland water classes in the DEA Intertidal Extents layer. It is a cost-distance connectivity mask that combines SRTM elevations with distance from the ocean and is delivered as a thresholded binary coastal/non-coastal mask. We have thresholded conservatively to identify intertidal environments. We advise caution in using this data layer for other types of coastal investigations outside of the intertidal zone.

### Ensemble Tidal Modelling

The Ensemble Tidal Modelling approach was implemented to account for the varying performance and biases of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia (Figure 6). The ensemble process utilises ancillary data to select and weight tidal models at any given coastal location, based on how well each model correlates with local satellite-observed patterns of tidal inundation, and water levels measured by satellite altimetry. A single ensemble tidal output was generated by combining the top 3 locally optimal models, and then used for all downstream product workflows.

Ensemble tide modelling was implemented in the [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) Python package which integrates satellite Earth observation data with tide modelling, leveraging tide modelling functionality from the [pyTMD](https://github.com/tsutterley/pyTMD) package. The ensemble was based on 10 commonly-used global ocean tidal models:

* Empirical Ocean Tide Model (EOT20; Hart-Davis et al., 2021)
* Finite Element Solution tide models (FES2012, FES2014, FES2022; Carrère et al., 2012; Lyard et al., 2021; Carrère et al., 2022)
* TOPEX/POSEIDON global tide models (TPXO8, TPXO9, TPXO10; Egbert and Erofeeva., 2002, 2010)
* Global Ocean Tide models (GOT4.10, GOT5.5, GOT5.6; Ray, 2013, Padman et al., 2018)

:::{figure} /_files/dea-intertidal/ensembletides.*
:alt: Ensemble tide validation Figure
:::

Figure 6 &mdash; Global tide models validated at Australian Baseline Sea Level Monitoring Project (ABSLMP) and Global Extreme Sea Level Analysis (GESLA) tide gauges

## Lineage

The DEA Intertidal product suite extends the concepts developed in the DEA Intertidal Elevation (NIDEM) product, integrating higher resolution 10 m Sentinel-2 data with the original 30 m Landsat data to create annual elevation models and exposure product layers for Australia’s intertidal zone.   

This shift to a more dynamic product suite is achieved through a pixel-based algorithm, replacing the waterline interpolation methods of NIDEM, and an improved tidal modelling process to better leverage the increased data resolution and density provided by the inclusion of Sentinel-2 data.  

## Processing Steps

1. Satellite data from Sentinel-2A, -2B and -2C, Landsat 7, 8, and 9 are loaded
2. Satellite data cloud masked and converted to Normalised Difference water Index (NDWI)
3. Tides modelled for every satellite pixel using [Ensemble Tidal Modelling](#ensemble-tidal-modelling)
4. Satellite data filtered to probable intertidal pixels using NDWI inundation frequency and tide correlation, and masked as coastal or non-coastal using cost-distance connectivity analysis of [SRTM elevation data](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/72759)
5. Pixel-based rolling median applied from low to high tide
6. Intertidal elevation modelled based on tide height at which a rolling median transitions from dry to wet
7. Intertidal elevation uncertainty modelled based on how cleanly modelled elevation divides satellite observations into dry and wet
8. Intertidal extents classes calculated based on Intertidal elevation and NDWI inundation frequency and tide correlation, with additional masking to remove urban false positives using abares_clum_2020 (ABARES, 2021)
9. Intertidal exposure calculated by comparing Intertidal elevation against high frequency modelled tides
10. Tidal metrics calculated by comparing satellite-observed tides against high frequency modelled tides

## References

ABARES, 2021. Catchment Scale Land Use of Australia - Update December 2020, Australian Bureau of Agricultural and Resource Economics and Sciences, Canberra

Bishop-Taylor, R., Sagar, S., Lymburner, L., Beaman, R.J., 2019. Between the tides: Modelling the elevation of Australia’s exposed intertidal zone at continental scale. *Estuarine, Coastal and Shelf Science* 23, 115–128.

Carrère L., F. Lyard, M. Cancet, A. Guillot, L. Roblou, 2012. FES2012: A new global tidal model taking advantage of nearly 20 years of altimetry, *Proceedings of meeting "20 Years of Altimetry"*, Venice 2012 

Carrère L., F. Lyard, M. Cancet, D. Allain, M. Dabat, E. Fouchet, E. Sahuc, Y. Faugere, G. Dibarboure, N. Picot, 2022. A new barotropic tide model for global ocean: FES2022, *2022 Ocean Surface Topography Science Team Meeting"*, Venice 2022 

Egbert, G.D., Erofeeva, S.Y., 2002. Efficient Inverse Modeling of Barotropic Ocean Tides. *J. Atmospheric Ocean. Technol.* 19, 183–204.

Egbert, G.D., Erofeeva, S.Y., 2010. The OSU TOPEX/Poseiden Global Inverse Solution TPXO. *TPXO8*-atlas Version 1.0*

Hart-Davis, M.G., Piccioni, G., Dettmering, D., Schwatke, C., Passaro, M., Seitz, F., 2021. EOT20: a global ocean tide model from multi-mission satellite altimetry. *Earth System Science Data* 13, 3869–3884. 

Lyard, F.H., Allain, D.J., Cancet, M., Carrère, L., Picot, N., 2021. FES2014 global ocean tide atlas: design and performance. *Ocean Science* 17, 615–649. 

Padman, L., Siegfried, M.R., Fricker, H.A., 2018. Ocean Tide Influences on the Antarctic and Greenland Ice Sheets, *Reviews of Geophysics*, 56, 142-184.

Ray, R. D., 2013. Precise comparisons of bottom-pressure and altimetric ocean tides. Journal of Geophysical Research: Oceans, 118(9), 4570–4584.

Sagar, S., Roberts, D., Bala, B., Lymburner, L., 2017. Extracting the intertidal extent and topography of the Australian coastline from a 28 year time series of Landsat observations. *Remote Sensing of Environment* 195, 153–169.


