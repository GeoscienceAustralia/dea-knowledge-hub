## Background

Intertidal zones are coastal environments exposed to both air and water, at low and high tide consecutively, and include sandy beaches, tidal flats, rocky shores and reefs.
They also characterise critical coastal habitats and ecosystems, and support a wide range of species and ecosystem-services.
Increasingly though, these dynamic environments are faced with threats from land reclaimation, coastal erosion and rising sea levels, amongst others.

The ever-changing nature of the tides makes it difficult to systematically capture consistent imagery of the intertidal zone, particularly across large regions and especially in remote areas of the country.
[Geomedian statistical techniques](https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) provide a robust method to combine tide-attributed time-series satellite imagery and produce representative and artefact free imagery 'composites' of Australia's coastal high and low tide environments.

## What this product offers

This product provides a suite of cloud-free composite Sentinel-2 satellite datasets that enable imaging of Australian coastal intertidal zones at both high and low tide. 
Using a geometric median (geomedian), the highest and lowest 15 % of satellite-observed tide heights from the Digital Earth Australia (DEA) Sentinel-2 imagery archive are combined to deliver annual snapshots of Australian coastal high and low tide environments.

Sentinel-2 satellite images are tidally attributed though pairing with pixel-based tidal modelling, generated from a selected ensemble of the best performing global tide models under local conditions.
The [ensemble tidal modelling](ensemble-tidal-modelling) approach was implemented to account for the varying performance and biases of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia.
Tidal attribution allows the imagery archive to be sorted by tide height rather than date, enabling visualisation of the intertidal zone during any stage of the tidal cycle.  

Spatially and temporally aligned to the [DEA Intertidal product suite](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/), DEA Tidal Composites are an annually updated data suite, generated from rolling 3-year epochs, at a 10 m spatial resolution.

DEA Tidal Composites include low and high tide imagery products and their associated quality assurance layers. 
Lowtide and hightide layers represent composites of the synthetic geomedian surface reflectance from Sentinel-2A, -2B and -2C analysis-ready data streams. 
The geomedian calculation maintains the spectral relationships between bands (Roberts et al., 2017), ensuring that the DEA Tidal Composites product delivers robust and valid surface reflectance spectra suitable for uses such as habitat mapping (Li et al., 2012) and delivers cloud free and noise reduced visualisation of the shallow water and intertidal coastal regions of Australia (Sagar et al., 2018). 
Quality assurance layers are provided to support interpretation of the lowtide and hightide datasets and include the tide-height thresholds above and below which associated images were included in the compositing process and the count of clear input images that contributed to each pixel in the composites.

## Applications

* Mapping cover types within the intertidal zone
* Visualising the full observed extent of the tidal range around the Australian continental coastline
* Monitoring for change in Australian coastal environments

## Technical information

### Features

The DEA Tidal Composites product is a 25-band mosaic, consistent with Sentinel-2, and produced to allow visualisation of the shallow water and intertidal coastal regions as observed at high or low tide. 
It is continental (coastal) in coverage and includes geomedian surface reflectance, along with pixel level metadata for each of the high and low tide mosaics.

The [file naming convention](https://knowledge.dea.ga.gov.au/guides/reference/collection_3_naming/#different-types-of-products) is as follows:

```
[ORGANISATION]_[PLATFORM]_[PRODUCT]_[REPORTING PERIOD]_[COLLECTION]_[TILE REFERENCE]_[DATA DATE]--[DATA PERIOD]_[PRODUCT STATUS]_[BAND NAME].[FILE EXTENSION]
```

For example:

```
 `ga_s2_tidal_composites_cyear_3_x080y125_2022--P1Y_final_low-red-edge-3.tif`
```

### Ensemble tide modelling

The Ensemble Tidal Modelling approach was implemented to account for the varying [performance and biases](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/?tab=description#ensemble-tidal-modelling) of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia. 
The ensemble process utilises ancillary data to select and weight tidal models at any given coastal location, based on how well each model correlates with local satellite-observed patterns of tidal inundation, and water levels measured by satellite altimetry. 
A single ensemble tidal output was generated by combining the top 3 locally optimal models, and then used for all downstream product workflows.

Ensemble tide modelling was implemented in the [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) Python package which integrates satellite Earth observation data with tide modelling, leveraging tide modelling functionality from the [pyTMD](https://github.com/tsutterley/pyTMD) package. 
The ensemble was based on 10 commonly-used global ocean tidal models:

* Empirical Ocean Tide Model (EOT20; Hart-Davis et al., 2021)
* Finite Element Solution tide models (FES2012, FES2014, FES2022; Carrère et al., 2012; Lyard et al., 2021; Carrère et al., 2022)
* TOPEX/POSEIDON global tide models (TPXO8, TPXO9, TPXO10; Egbert and Erofeeva., 2002, 2010)
* Global Ocean Tide models (GOT4.10, GOT5.5, GOT5.6; Ray, 2013, Padman et al., 2018)

### Product layers

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

#### Low tide composites (multiple 'low_' bands)

11 bands, prefixed by `low_` in the product file name, are delivered in the spectral resolution of the Sentinel-2 band set. 
All bands are reported at 10 m spatial resolution and are detailed in the [Specifications tab](./?tab=specifications). 
Each band represents synthetic data, derived from the geomedian calculation of the input Sentinel-2 satellite data from the lowest 15 % of satellite-observed tide heights during each 3-year analysis epoch. 
Maintenance of the spectral relationships between geomedian bands ensures they can be combined to produce lowtide imagery and analysis in coastal environments. 

#### High tide composites (multiple 'high_' bands)

11 bands, prefixed by `high_` in the product file name, are delivered in the spectral resolution of the Sentinel-2 band set.
All bands are reported at 10 m spatial resolution and are detailed in the [Specifications tab](./?tab=specifications). 
Each band represents synthetic data, derived from the geomedian calculation of the input Sentinel-2 satellite data from the highest 15 % of satellite-observed tide heights during each 3-year analysis epoch. 
Maintenance of the spectral relationships between geomedian bands ensures they can be combined to produce hightide imagery and analysis in coastal environments.

#### Quality assurance: Low threshold (qa_low_threshold)

A pixel-based quality assurance layer, identifying the maximum tide height included in the low tide composite.
Usually, this value corresponds to the lowest 15th percentile satellite-observed tide height. 
Pixels with less than 20 clear observations in this 15th percentile range are gapfilled up to 20 with the next lowest satellite-observed tide height observations to ensure sufficient data density to produce a clear composite image.
When a pixel is gapfilled, the highest gapfilled tide height is reported for that pixel in the `Low threshold` layer.
The `Low threshold` layer is only valid for marine and coastal pixels.

#### Quality assurance: High threshold (qa_high_threshold)

A pixel-based quality assurance layer, identifying the minimum tide height included in the high tide composite.
Usually, this value corresponds to the highest 15th percentile satellite-observed tide height. 
Pixels with less than 20 clear observations in this 15th percentile range are gapfilled up to 20 with the next highest satellite-observed tide height observations to ensure sufficient data density to produce a clear composite image.
When a pixel is gapfilled, the lowest gapfilled tide height is reported for that pixel in the `High threshold` layer.
The `High threshold` layer is only valid for marine and coastal pixels.

#### Quality assurance: Count clear (qa_count_clear)

The `Count clear` pixel-based quality assurance layer represents the number of clear observations per-pixel that are used in both the high and low tide composites.
The layer typically identifies the number of clear satellite observations in 15 percent of all observations per-pixel. 
When the observation count in 15 percent of all observations is less than 20, the nearest tide-height observations are used to gapfill up to a count of 20 clear observations, if available.

## Lineage

The product has been developed to provide a geomedian composite dataset of coastal regions of Australia for the highest and lowest 15 % of satellite-observed tides in the Sentinel-2 catalogue, enabling both visualisation and spectral analysis. 
Coastal Sentinel-2 observations are composited relative to tidal modelling of the Australian coastline using an ensemble of global tide models, leveraging python packages [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) and [pyTMD](https://github.com/tsutterley/pyTMD).

## Processing steps

**1. Load and pre-process data**

1. [Load](https://github.com/GeoscienceAustralia/dea-intertidal/blob/develop/intertidal/io.py#L166) analysis ready satellite data from Sentinel-2A, -2B and -2C for the epoch of interest
1. Remove [sunglinted](https://github.com/GeoscienceAustralia/dea-notebooks/blob/develop/Tools/dea_tools/coastal.py#L2327) pixels by masking out pixels with glint angles of less than 20 degrees
1. Proceed with tide modelling and geomedian calculation only if the full time-series of input satellite images has 50 or more observations

**2. Calculate high and low tide geomedian composites**

1. [Model tide heights](https://github.com/GeoscienceAustralia/eo-tides/blob/main/eo_tides/eo.py#L306) for the spatial extent and timesteps of the loaded satellite data array
1. Attribute tide heights to the valid satellite observations
1. Rank all observations by ascending tide height
1. Select the observations in the top and bottom 15 percent of satellite observed tide heights by identifying their associated tide height rankings
1. If the number of observations in the top and bottom 15 percent is less than 20, gapfill up to 20 by taking the next highest or lowest tide heights from the full stack of satellite observations respectively
1. Calculate a [geomedian](https://github.com/opendatacube/odc-algo/blob/main/odc/algo/_geomedian.py#L188) on each subset and count the contributing number of clear observations.

## Software

This work was enabled by a range of Python libraries and packages whose code repositories include:

* [DEA Intertidal Github](https://github.com/GeoscienceAustralia/dea-intertidal) &mdash; A codebase for DEA Intertidal product generation workflows 
* [EO-Tides Github](https://github.com/GeoscienceAustralia/eo-tides) &mdash; A codebase for integrating satellite Earth observations with tide modelling
* [DEA Tools Github](https://github.com/GeoscienceAustralia/dea-notebooks) &mdash; Earth observation data manipulation tools 
* [PyTMD Github](https://github.com/tsutterley/pyTMD) &mdash; Python-based tidal prediction software
* [odc-algo](https://github.com/opendatacube/odc-algo) &mdash; A codebase containing algorithms to use with Open Data Cube workflows

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

