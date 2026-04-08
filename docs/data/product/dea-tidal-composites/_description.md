## Background

Intertidal zones are coastal environments that are exposed to both air and water at different times due to the cycle of low and high tides. These zones can include sandy beaches, tidal flats, rocky shores, and reefs. Many of them are critical coastal habitats and ecosystems which support a wide range of species and ecosystem services. Increasingly, these dynamic environments are faced with threats such as land reclamation, coastal erosion, and rising sea levels.

The ever-changing nature of the tides makes it difficult to systematically capture consistent imagery of coastal environments, particularly across large regions and in remote areas of the country. This is where [Geomedian statistical techniques](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) can be used. These are robust techniques which combine tide-attributed time-series satellite imagery to produce representative and artefact-free imagery 'composites' of Australia's coastal high and low tide environments.

## What this product offers

The DEA Tidal Composites product provides cloud-free satellite imagery composites capturing the Australian coastal zone at high and low tide. By applying a geometric median (geomedian) calculation to the highest and lowest 15% of satellite-observed tidal conditions, multiple satellite images from the Digital Earth Australia (DEA) Sentinel-2 analysis-ready data (ARD) archive are combined into high quality annual imagery composites.

Input satellite images are tidally filtered using pixel-based tide modelling generated from a locally optimised ensemble of top-performing global tide models ([see below](#ensemble-tide-modelling)). This ensemble approach was implemented to account for the varying performance and biases of individual ocean models across Australia's complex coastal regimes.

Because the geomedian calculation maintains the spectral relationships between satellite bands (Roberts et al., 2017), the composites deliver robust and valid surface reflectance spectra. This provides clean, cloud-free imagery covering the shallow water and intertidal regions of Australia (Sagar et al., 2018), suitable for downstream applications such as habitat mapping and Machine Learning (ML) classification (Li et al., 2012) .

Alongside low and high tide imagery, the product includes associated quality assurance layers that detail the specific tide-height thresholds used to filter the pixels during the compositing process, as well as a count of the clear satellite observations that contributed to each pixel.

## Applications

Here are some of the ways this data product can be used:

* Mapping coastal environments and cover types usually hidden beneath the ocean's surface at high tide​.
* Monitoring for change across Australia's dynamic coastal environments.
* Visualising how ocean tides influence Australia's coastal environments.
* Training machine learning models and classifiers that require high quality coastal imagery.

## Technical information

### Features

This product consists of 25 continental (coastal) coverage data layers, including 11 geomedian surface reflectance layers for high and low tide respectively (consistent with DEA's Sentinel-2 ARD), and three quality assurance pixel-level metadata layers. Datasets are provided as continental 10 m resolution GeoTIFFs covering the entire Australian coastal zone.

All datasets are produced annually from a 3-year composite of DEA Sentinel-2 Collection 3 surface reflectance data. The product time series commences from 2016, with datasets labelled by the middle year of data. For example, the 2017 layer combines data from 2016, 2017, and 2018. Updates to the product suite are scheduled annually. DEA Tidal Composites is spatially and temporally aligned to the resolution and timesteps of the [DEA Intertidal product suite](/data/product/dea-intertidal/).

#### Datasets

Annual raster files for each of the product bands are available in DEA's Amazon S3 bucket as continental mosaics in cloud-optimised GeoTIFF (COG) format.
These files support [fast and efficient data streaming](/guides/continental-cogs-geotiff-mosaics/).

For access and usage information, see the [Access tab](./?tab=access).

DEA Tidal Composites data follows the [DEA Collection 3 naming conventions](/guides/reference/collection_3_naming/):

```text
ga_s2_tidal_composites_cyear_3_mosaic_2024--P1Y_low-red.tif
{Organisation}_{Platform}_{Product}_{Reporting period}_{Collection}_{Region}_{Data date}--{Data period}_{Band name}.{File extension}
```

Multi-band annual continental data Virtual Raster (VRT) mosaics are also provided for fast and efficient streaming of true colour (red/green/blue) and false colour (green/SWIR/NIR) imagery composites in a GIS environment (e.g. QGIS, Esri ArcGIS Pro).
These VRT files combine and stream multiple single-band COG datasets via a single layer.
Here's an example of the VRT file naming convention:

```text
ga_s2_tidal_composites_cyear_3_mosaic_2024--P1Y_vrt-low-truecolour.vrt
```

### Product layers

See the attributes of these layers in the [Specifications tab](./?tab=specifications).

#### Low tide composites (multiple 'low_' bands)

The 11 bands prefixed with `low_` are provided at 10 m spatial resolution (matching Sentinel-2). Each band represents an annual imagery composite generated by combining the lowest 15% of satellite-observed tidal conditions over a 3-year analysis epoch using a geomedian calculation. Because the geomedian process preserves spectral relationships, these bands deliver robust data for downstream analysis of coastal environments at low tide.

#### High tide composites (multiple 'high_' bands)

The 11 bands prefixed with `high_` are provided at 10 m spatial resolution (matching Sentinel-2). Each band represents an annual imagery composite generated by combining the highest 15% of satellite-observed tidal conditions over a 3-year analysis epoch using a geomedian calculation. Because the geomedian process preserves spectral relationships, these bands deliver robust data for downstream analysis of coastal environments at high tide.

#### Quality assurance: Low threshold (qa_low_threshold)

This quality assurance layer records the maximum tide height included in the low tide composites. While this typically represents the 15th percentile of satellite-observed tides, pixels lacking 20 clear observations within this range are gap-filled with the next lowest available observations. When gap-filling occurs, the layer reports the highest tide height included to reach the 20-observation minimum. While this layer extends inland for modelling purposes, tide heights are only valid for marine and coastal pixels.

#### Quality assurance: High threshold (qa_high_threshold)

This quality assurance layer records the minimum tide height included in the high tide composites. While this typically represents the 85th percentile of satellite-observed tides, pixels lacking 20 clear observations within this range are gap-filled with the next highest available observations. When gap-filling occurs, the layer reports the lowest tide height included to reach the 20-observation minimum. While this layer extends inland for modelling purposes, tide heights are only valid for marine and coastal pixels.

#### Quality assurance: Count clear (qa_count_clear)

This pixel-based quality assurance layer represents the number of clear observations per pixel that are used in both the high and low tide composites.
This layer typically represents 15% of the total count of all clear satellite observations. 
When this value would be less than 20, the nearest tide-height observations (if available) are used to gapfill up to a count of 20 clear observations.

### Ensemble tide modelling

The Ensemble Tidal Modelling approach was implemented to account for the varying performance and biases of existing global ocean tide models across the complex tidal regimes and coastal regions of Australia. The ensemble process utilises ancillary data to select and weight tidal models at any given coastal location based on how well each model correlates with local satellite-observed patterns of tidal inundation and water levels measured by satellite altimetry. A single ensemble tidal output was generated by combining the top three locally optimal models, and used for all downstream product workflows.

Ensemble tide modelling was implemented in the [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) Python package which integrates satellite Earth observation data with tide modelling (Bishop-Taylor et al. 2025). It leverages tide modelling functionality from the [pyTMD](https://github.com/tsutterley/pyTMD) package. The ensemble was based on 9 commonly-used global ocean tidal models:

* Empirical Ocean Tide Model (EOT20; Hart-Davis et al., 2021)
* Finite Element Solution tide models (FES2012, FES2014, FES2022; Carrère et al., 2012; Lyard et al., 2021; Carrère et al., 2022)
* TOPEX/POSEIDON global tide models (TPXO8, TPXO9, TPXO10; Egbert and Erofeeva., 2002, 2010)
* Global Ocean Tide models (GOT4.10, GOT5.6; Ray, 2013, Padman et al., 2018)

## Lineage

The DEA Tidal Composites product suite extends the concepts developed in the [High and Low Tide Composites (HLTC)](/data/version-history/dea-high-and-low-tide-imagery-landsat-2.0.0) product (Sagar et al. 2018), using higher resolution 10 m Sentinel-2 data in place of the original 30 m Landsat data and improved tide modelling techniques to improve high and low tide representation.

## Processing steps

**1. Load and pre-process data**

1. [Load](https://github.com/GeoscienceAustralia/dea-intertidal/blob/develop/intertidal/io.py#L166) analysis ready satellite data from Sentinel-2A, -2B, and -2C for the epoch of interest.
1. Remove [sunglinted](https://github.com/GeoscienceAustralia/dea-notebooks/blob/develop/Tools/dea_tools/coastal.py#L2327) pixels by masking out pixels with glint angles of less than 20 degrees.
1. Proceed with tide modelling and geomedian calculation only if the full time-series of input satellite images has 50 or more observations.

**2. Calculate high and low tide geomedian composites**

1. Model tide heights for the spatial extent and timesteps of the loaded satellite data array using the [ensemble tide modelling](#ensemble-tide-modelling) approach.
1. Attribute tide heights to the valid satellite observations.
1. Rank all observations by ascending tide height.
1. Select the observations in the top and bottom 15% of satellite-observed tide heights by calculating their associated tide height rankings.
1. If the number of observations in the top and bottom 15% is less than 20, gapfill up to the count of 20 observations by taking the next highest or lowest tide heights from the full stack of satellite observations respectively.
1. Calculate a [geomedian](https://github.com/opendatacube/odc-algo/blob/main/odc/algo/_geomedian.py#L188) on each tidally-filtered subset and count the contributing number of clear observations.

## Software

This work was enabled by a range of Python libraries and packages whose code repositories include:

* [DEA Intertidal](https://github.com/GeoscienceAustralia/dea-intertidal) &mdash; DEA Intertidal product generation workflows.
* [eo-tides](https://github.com/GeoscienceAustralia/eo-tides) &mdash; Tools for integrating satellite Earth observations with tide modelling.
* [DEA Tools](https://github.com/GeoscienceAustralia/dea-notebooks/tree/develop/Tools) &mdash; Earth observation data manipulation tools.
* [PyTMD](https://github.com/tsutterley/pyTMD) &mdash; Python-based tidal prediction software.
* [odc-algo](https://github.com/opendatacube/odc-algo) &mdash; Algorithms for use with Open Data Cube workflows.

## References

Bishop-Taylor, R., Phillips, C., Sagar, S., Newey, V., & Sutterley, T., 2025. eo-tides: Tide modelling tools for large-scale satellite Earth observation analysis. *Journal of Open Source Software*, 10(109), 7786. https://doi.org/10.21105/joss.07786

Carrère L., F. Lyard, M. Cancet, A. Guillot, L. Roblou, 2012. FES2012: A new global tidal model taking advantage of nearly 20 years of altimetry, *Proceedings of meeting "20 Years of Altimetry"*, Venice 2012 

Carrère L., F. Lyard, M. Cancet, D. Allain, M. Dabat, E. Fouchet, E. Sahuc, Y. Faugere, G. Dibarboure, N. Picot, 2022. A new barotropic tide model for global ocean: FES2022, *2022 Ocean Surface Topography Science Team Meeting"*, Venice 2022 

Egbert, G. D., & Erofeeva, S. Y. (2002). Efficient Inverse Modeling of Barotropic Ocean Tides. *Journal of Atmospheric and Oceanic Technology*, *19*(2), 183–204. <https://doi.org/10.1175/1520-0426(2002)019%3c0183:EIMOBO%3e2.0.CO;2>

Egbert, G.D., Erofeeva, S.Y., 2010. The OSU TOPEX/Poseiden Global Inverse Solution TPXO [WWW Document]. TPXO8-Atlas Version 10. URL <http://volkov.oce.orst.edu/tides/global.html> (accessed 2.15.16).

Hart-Davis, M.G., Piccioni, G., Dettmering, D., Schwatke, C., Passaro, M., Seitz, F., 2021. EOT20: a global ocean tide model from multi-mission satellite altimetry. *Earth System Science Data* 13, 3869–3884. 

Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. *Remote Sensing of Environment*, *124*, 756–770. <https://doi.org/10.1016/j.rse.2012.06.018>

Lyard, F.H., Allain, D.J., Cancet, M., Carrère, L., Picot, N., 2021. FES2014 global ocean tide atlas: design and performance. *Ocean Science* 17, 615–649. 

Padman, L., Siegfried, M.R., Fricker, H.A., 2018. Ocean Tide Influences on the Antarctic and Greenland Ice Sheets, *Reviews of Geophysics*, 56, 142-184.

Ray, R. D., 2013. Precise comparisons of bottom-pressure and altimetric ocean tides. Journal of Geophysical Research: Oceans, 118(9), 4570–4584.

Roberts, D., Mueller, N., & Mcintyre, A. (2017). High-Dimensional Pixel Composites From Earth Observation Time Series. *IEEE Transactions on Geoscience and Remote Sensing*, *55*(11), 6254–6264. <https://doi.org/10.1109/TGRS.2017.2723896>

Rubel, F., & Kottek, M. (2010). Observed and projected climate shifts 1901-2100 depicted by world maps of the Köppen-Geiger climate classification. *Meteorologische Zeitschrift*, *19*, 135–141. <https://doi.org/10.1127/0941-2948/2010/0430>

Sagar, S., Phillips, C., Bala, B., Roberts, D., & Lymburner, L. (2018). Generating Continental Scale Pixel-Based Surface Reflectance Composites in Coastal Regions with the Use of a Multi-Resolution Tidal Model. *Remote Sensing*, *10*, 480. <https://doi.org/10.3390/rs10030480>

Sagar, S., Roberts, D., Bala, B., & Lymburner, L. (2017). Extracting the intertidal extent and topography of the Australian coastline from a 28year time series of Landsat observations. *Remote Sensing of Environment*, *195*, 153–169. <https://doi.org/10.1016/j.rse.2017.04.009>

