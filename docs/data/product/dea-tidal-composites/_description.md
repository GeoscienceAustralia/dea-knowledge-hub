# Background

Intertidal zones are coastal environments exposed to both air and water, at low and high tide consecutively, and include sandy beaches, tidal flats, rocky shores and reefs.
They also characterise critical coastal habitats and ecosystems, and support a wide range of species and ecosystem-services.
Increasingly though, these dynamic environments are faced with threats from land reclaimation, coastal erosion and rising sea levels, amongst others.

The ever-changing nature of the tides makes it hard to systematically capture consistent imagery of the intertidal zone, particularly across large regions and especially in remote areas of the country.
[Geomedian statistical techniques](https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) provide a robust method to combine tide-attributed time-series satellite imagery and produce representative and artefact free imagery 'composites' of Australia's coastal high and low tide environments.

## Applications

* Mapping cover types within the intertidal zone
* Visualising the full observed extent of the tidal range around the Australian continental coastline
* Monitoring for change in Australian coastal environments

# Technical information

## What this product offers

This product provides a suite of cloud-free composite Sentinel-2 satellite datasets that enable imaging of Australian coastal intertidal zones at both high and low tide. 
Using a geometric median (geomedian), the highest and lowest 20% of observed tidal ranges in Digital Earth Australia (DEA)’s Sentinel-2 imagery archive are combined to deliver annual snapshots of Australian coastal high and low tide environments.

Sentinel-2 satellite images are tidally attributed though pairing with pixel-based local tidal modelling, generated from a selected ensemble of the best performing global tide models under local conditions.
The [ensemble tidal modelling](ensemble-tidal-modelling) approach was implemented to account for the varying performance and biases of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia.
Tidal attribution allows the imagery archive to be sorted by tide height rather than date, so the intertidal zone can be visualised during any stage of the tide regime.  

Spatially and temporally aligned to the [DEA Intertidal product suite](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/), DEA Tidal Composites are an annually updated data suite, generated from rolling 3-year epochs, with a minimum of 10 m spatial resolution.

DEA Tidal Composites include 25 layers of data, separated into lowtide, hightide and quality assurance categories. Lowtide and hightide layers represent composites of the synthetic geomedian surface reflectance from Sentinel-2A, -2B and -2C analysis-ready data streams. The geomedian calculation maintains the spectral relationships between bands, ensuring that the DEA Tidal Composites product delivers robust and valid surface reflectance spectra suitable for uses such as habitat mapping (Li et al., 2012; Roberts et al., 2017) and delivers cloud free and noise reduced visualisation of the shallow water and intertidal coastal regions of Australia (Sagar et al., 2018). Quality assurance layers are provided to support interpretation of the lowtide and hightide datasets and include the tide-height thresholds above and below which associated images were included in the compositing process and the count of clear input images that contributed to each pixel in the composites.

## Features

The DEA Tidal Composites product is a 25-band mosaic, consistent with Sentinel-2, produced to allow visualisation of the shallow water and intertidal coastal regions as observed at high or low tide. It is continental (coastal) in coverage and includes geomedian surface reflectance, along with pixel level metadata for each of the high and low tide mosaics.

The [file naming convention](https://knowledge.dea.ga.gov.au/guides/reference/collection_3_naming/#different-types-of-products) is as follows:

```
[ORGANISATION]_[PLATFORM]_[PRODUCT]_[REPORTING PERIOD]_[COLLECTION]_[TILE REFERENCE]--[DATA PERIOD]_[PRODUCT STATUS]_[BAND NAME].[FILE EXTENSION]
```

For example:

```
 `ga_s2_tidal_composites_cyear_3_x080y125_2022--P1Y_final_low-red-edge-3.tif`
```

## Software

This work was enabled by a range of Python libraries and packages whose code repositories include:

* [DEA Intertidal Github](https://github.com/GeoscienceAustralia/dea-intertidal) &mdash; A codebase for DEA Intertidal product generation workflows 
* [EO-Tides Github](https://github.com/GeoscienceAustralia/eo-tides) &mdash; A codebase for integrating satellite Earth observations with tide modelling
* [DEA Tools Github](https://github.com/GeoscienceAustralia/dea-notebooks) &mdash; Earth observation data manipulation tools 
* [PyTMD Github](https://github.com/tsutterley/pyTMD) &mdash; Python-based tidal prediction software
* [odc-algo](https://github.com/opendatacube/odc-algo) &mdash; A codebase containing algorithms to use with Open Data Cube workflows

## Product layers

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

### Low tide composites

11 bands, prefixed with `low` in the product file name, are delivered in the spectral and spatial resolution of the Sentinel-2 band set and are detailed in the [Specifications tab](./?tab=specifications). Each band represents synthetic data, derived from the geomedian calculation of the input Sentinel-2 satellite data from the lowest 20 % of observed tides during each 3-year analysis epoch. Maintenance of the spectral relationships between geomedian bands ensures they can be combined to produce lowtide imagery and analysis in coastal environments. 

### High tide composites

11 bands, prefixed with `high` in the product file name, are delivered in the spectral and spatial resolution of the Sentinel-2 band set and are detailed in the [Specifications tab](./?tab=specifications). Each band represents synthetic data, derived from the geomedian calculation of the input Sentinel-2 satellite data from the highest 20 % of observed tides during each 3-year analysis epoch. Maintenance of the spectral relationships between geomedian bands ensures they can be combined to produce hightide imagery and analysis in coastal environments.

### Quality assurance

Three bands are delivered to provide quality assurance with DEA Tidal Composites.

#### Low threshold

A pixel-based quality assurance layer, identifying the lowest 20th percentile observed tide height. All satellite observations associated with tide heights lower than this value, per-pixel, are included in the lowtide geomedian composites.

#### High threshold

A pixel-based quality assurance layer, identifying the highest 20th percentile observed tide height. All satellite observations associated with tide heights higher than this value, per-pixel, are included in the hightide geomedian composites.

#### Count clear

A pixel-based quality assurance layer, identifying the number of clear satellite observations in 20 percent of all observations per-pixel. This represents the number of clear observations per-pixel that are used in both the high and low tide composites.

## Ensemble tide modelling

The Ensemble Tidal Modelling approach was implemented to account for the varying [performance and biases](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/?tab=description#ensemble-tidal-modelling) of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia. The ensemble process utilises ancillary data to select and weight tidal models at any given coastal location, based on how well each model correlates with local satellite-observed patterns of tidal inundation, and water levels measured by satellite altimetry. A single ensemble tidal output was generated by combining the top 3 locally optimal models, and then used for all downstream product workflows.

Ensemble tide modelling was implemented in the [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) Python package which integrates satellite Earth observation data with tide modelling, leveraging tide modelling functionality from the [pyTMD](https://github.com/tsutterley/pyTMD) package. The ensemble was based on 10 commonly-used global ocean tidal models:

* Empirical Ocean Tide Model (EOT20; Hart-Davis et al., 2021)
* Finite Element Solution tide models (FES2012, FES2014, FES2022; Carrère et al., 2012; Lyard et al., 2021; Carrère et al., 2022)
* TOPEX/POSEIDON global tide models (TPXO8, TPXO9, TPXO10; Egbert and Erofeeva., 2002, 2010)
* Global Ocean Tide models (GOT4.10, GOT5.5, GOT5.6; Ray, 2013, Padman et al., 2018)

## Lineage

The product has been developed to provide a geomedian composite dataset of coastal regions of Australia for the highest and lowest 20% of the observed tidal range in the Sentinel-2 catalogue, enabling both visualisation and spectral analysis. Coastal Sentinel-2 observations are composited relative to tidal modelling of the Australian coastline using an ensemble of global tide models, leveraging python packages [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) and [pyTMD](https://github.com/tsutterley/pyTMD).

## Processing steps

1. Load and pre-process data
    - [Load](https://github.com/GeoscienceAustralia/dea-intertidal/blob/develop/intertidal/io.py#L166) analysis ready satellite data from Sentinel-2A, -2B and -2C
    - Filter based on [geometric quality assessment](https://knowledge.dea.ga.gov.au/notebooks/DEA_products/DEA_Sentinel2_Surface_Reflectance/#Filtering-by-metadata-to-remove-poorly-georeferenced-scenes) to remove poorly georeferenced scenes
    - Remove [sunglinted](https://github.com/GeoscienceAustralia/dea-notebooks/blob/develop/Tools/dea_tools/coastal.py#L2327) pixels by masking out pixels with glint angles less than 20 degrees
    - Proceed with tide modelling and geomedian calculation only if the time-series of input satellite images has 20 or more observations
2. Calculate high and low tide geomedian composites

    - [Model tide heights](https://github.com/GeoscienceAustralia/eo-tides/blob/main/eo_tides/eo.py#L306) for the spatial extent and timesteps of the loaded satellite data array
    - Attribute tide heights to the valid satellite observations and calculate the satellite observed tide range
    - Calculate the [quantile](https://github.com/opendatacube/odc-algo/blob/main/odc/algo/_percentile.py#L85) tide range and identify the absolute tide value thresholds associated with the top and bottom 20th percentiles of the tide range
    - Select satellite observations below and above the low and high tide thresholds. Calculate a [geomedian](https://github.com/opendatacube/odc-algo/blob/main/odc/algo/_geomedian.py#L188) on each subset and count the contributing number of clear observations.


## References

Carrère L., F. Lyard, M. Cancet, A. Guillot, L. Roblou, 2012. FES2012: A new global tidal model taking advantage of nearly 20 years of altimetry, *Proceedings of meeting "20 Years of Altimetry"*, Venice 2012 

Carrère L., F. Lyard, M. Cancet, D. Allain, M. Dabat, E. Fouchet, E. Sahuc, Y. Faugere, G. Dibarboure, N. Picot, 2022. A new barotropic tide model for global ocean: FES2022, *2022 Ocean Surface Topography Science Team Meeting"*, Venice 2022 

Egbert, G. D., & Erofeeva, S. Y. (2002). Efficient Inverse Modeling of Barotropic Ocean Tides. *Journal of Atmospheric and Oceanic Technology*, *19*(2), 183–204. [https://doi.org/10.1175/1520-0426(2002)019<0183:EIMOBO>2.0.CO;2](https://doi.org/10.1175/1520-0426(2002)019%3c0183:EIMOBO%3e2.0.CO;2)

Egbert, G.D., Erofeeva, S.Y., 2010. The OSU TOPEX/Poseiden Global Inverse Solution TPXO [WWW Document]. TPXO8-Atlas Version 10. URL [http://volkov.oce.orst.edu/tides/global.html](http://volkov.oce.orst.edu/tides/global.html) (accessed 2.15.16).

Hart-Davis, M.G., Piccioni, G., Dettmering, D., Schwatke, C., Passaro, M., Seitz, F., 2021. EOT20: a global ocean tide model from multi-mission satellite altimetry. *Earth System Science Data* 13, 3869–3884. 

Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. *Remote Sensing of Environment*, *124*, 756–770. [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

Lyard, F.H., Allain, D.J., Cancet, M., Carrère, L., Picot, N., 2021. FES2014 global ocean tide atlas: design and performance. *Ocean Science* 17, 615–649. 

Padman, L., Siegfried, M.R., Fricker, H.A., 2018. Ocean Tide Influences on the Antarctic and Greenland Ice Sheets, *Reviews of Geophysics*, 56, 142-184.

Ray, R. D., 2013. Precise comparisons of bottom-pressure and altimetric ocean tides. Journal of Geophysical Research: Oceans, 118(9), 4570–4584.

Roberts, D., Mueller, N., & Mcintyre, A. (2017). High-Dimensional Pixel Composites From Earth Observation Time Series. *IEEE Transactions on Geoscience and Remote Sensing*, *55*(11), 6254–6264. [https://doi.org/10.1109/TGRS.2017.2723896](https://doi.org/10.1109/TGRS.2017.2723896)

Rubel, F., & Kottek, M. (2010). Observed and projected climate shifts 1901-2100 depicted by world maps of the Köppen-Geiger climate classification. *Meteorologische Zeitschrift*, *19*, 135–141. [https://doi.org/10.1127/0941-2948/2010/0430](https://doi.org/10.1127/0941-2948/2010/0430)

Sagar, S., Phillips, C., Bala, B., Roberts, D., & Lymburner, L. (2018). Generating Continental Scale Pixel-Based Surface Reflectance Composites in Coastal Regions with the Use of a Multi-Resolution Tidal Model. *Remote Sensing*, *10*, 480. [https://doi.org/10.3390/rs10030480](https://doi.org/10.3390/rs10030480)

Sagar, S., Roberts, D., Bala, B., & Lymburner, L. (2017). Extracting the intertidal extent and topography of the Australian coastline from a 28year time series of Landsat observations. *Remote Sensing of Environment*, *195*, 153–169. [https://doi.org/10.1016/j.rse.2017.04.009](https://doi.org/10.1016/j.rse.2017.04.009)

