## Background

Intertidal environments support important ecological habitats (e.g. sandy beaches and shores, tidal flats and rocky shores and reefs), and provide many valuable benefits such as storm surge protection, carbon storage and natural resources for recreational and commercial use.

Intertidal zones are faced with increasing threats from coastal erosion, land reclamation (e.g. port construction), and sea level rise. Accurate elevation data describing the height and shape of the coastline is needed to help predict when and where these threats will have the greatest impact. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.

The intertidal zone also forms a critical habitat and foraging ground for migratory shore birds and other species. An improved characterisation of the exposure patterns of this dynamic environment is important to support conservation efforts and to gain a better understanding of migratory species pathways.

% ## What this product offers

% ## Data description

## Applications

* Integrating with existing topographic and bathymetric data to seamlessly map the elevation of the coastal zone
* Providing baseline elevation data for predicting the impact of coastal hazards such as storm surges, tsunami inundation or future sea-level rise
* Investigating coastal erosion and sediment transport processes
* Supporting habitat mapping and modelling for coastal ecosystems extending across the terrestrial to marine boundary
* Characterise the spatio-temporal exposure patterns of the intertidal zone to support migratory species studies and applications

## Technical information

The DEA Intertidal Suite is the next generation of intertidal products developed in DEA, leveraging our approach of combining time-series earth observation data with tidal modelling to create continental scale products for the intertidal region. The Intertidal Suite improves on the DEA Intertidal Elevation Model (NIDEM) (https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat), and adds a number of new features and products to help users better understand the intertidal environment and interpret the data.

The National Intertidal Digital Elevation Model (NIDEM) was the first 3D model of Australia’s intertidal zone - the area of coastline exposed and flooded by ocean tides. Intertidal environments support important ecological habitats (e.g. tidal mudflats, sandy beaches and coral reefs), and provide many valuable benefits such as storm surge protection, carbon storage and natural resources for recreational and commercial use. However, intertidal zones are faced with increasing threats from coastal erosion, land reclamation (e.g. port construction), and sea level rise. Accurate elevation data describing the height and shape of the coastline is needed to help predict when and where these threats will have the greatest impact. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.

The DEA Intertidal Suite fundamentally changes and improves the way in which we model the intertidal zone when compared to the original NIDEM elevation model, along with the addition of number of new features and products:

* The addition of Sentinel-2 data improves the resolution of the model to 10m, compared to the 25m of the original NIDEM.
* Incorporation of a new pixel-based method supports a reduction in the temporal epoch of the product to 3 years (in comparison to 28 years in NIDEM), improving the ability to capture the current state of dynamic coastal environments, and opening up change over time applications through the use of multiple epochs.
* Quantification of the vertical uncertainty of the elevation model.
* An Intertidal Exposure model at 10m resolution to examine the spatio-temporal patterns of exposure and inundation across the intertidal zone, supporting migratory species studies and habitat mapping applications.
* Tidal metrics to enable users to understand the varied ranges and distributions of tidal stages observed by the Landsat and Sentinel-2 satellites across Australia, and how this information can be used to better understand and interpret the products.
* A change in global tide model from OSU TPXO8 to AVISO FES (Finite Element Solution) 2014 to improve tide modelling performance (Carrère et al. 2016).

A key addition in the DEA Intertidal Suite is the inclusion of a Toolkit and Jupyter Notebook which enable users to create their own customised versions of the core products (for details, see Toolkit Design XXXX)

#### Features

The DEA Intertidal Suite contains four (4) core datasets and seven (7) tidal metric layers, all provided as continental 10m resolution geotiffs for the Australian coastal and intertidal region.

##### **DEA Intertidal Elevation**

The DEA Intertidal Elevation dataset provides elevation in metre units relative to modelled Mean Sea Level for each pixel of intertidal terrain across the Australian coastline. The elevation model is generated from Landsat and Sentinel-2 data from 2020-2022, utilising a pixel-based approach and tidal modelling from the FES 2014 tidal model. For every pixel, the time-series of surface reflectance data is converted to the Normalised Difference Water Index (NDWI), and each observation tagged with the tidal height modelled at the time of acquisition by the satellite. A median trend line is then fitted to the pixel observations based on NDWI vs tidal height, with the intersection of the median line at the NDW threshold = 0.1  used to extract the elevation for the pixel.

Data type - Float32

No Data - NaN

##### **DEA Intertidal Elevation Uncertainty**

Need Robbi input 

Data type - Float32

No Data - NaN

##### **DEA Intertidal Exposure**

Need Claire input

Data type - Int16

No Data -999

##### **DEA Intertidal Extents**

Unsure of the wording and current 5? Classifications

Data type - Int16

No Data -999

##### DEA Intertidal tidal spread

The tidal spread dataset provides the percentage of the full astronomical tidal range observed by the time series of satellite observations at each pixel (see figure XXXX)

Data type - Int16

No Data -999

##### DEA Intertidal low tide offset

The low tide offset dataset  quantifies (in percentage of the modelled astronomical tidal range) the offset of the lowest observed tide (LOT) observed by the satellite time-series to the lowest astronomical tide (LAT). (see figure XXX)

Data type - Int16

No Data -999

##### DEA Intertidal high tide offset

The high tide offset dataset  quantifies (in percentage of the modelled astronomical tidal range) the offset of the highest observed tide (HOT) observed by the satellite time-series to the highest astronomical tide (HAT).(see figure XXX)

Data type - Int16

No Data -999

##### DEA Intertidal lowest observed tide

The lowest observed tide dataset maps the lowest observed tide (LOT) of the satellite time-series at each pixel, based on the FES 2014 model.

Data type - Float32

No Data - NaN

##### DEA Intertidal highest observed tide

The highest observed tide dataset maps the highest observed tide (HOT) of the satellite time-series at each pixel, based on the FES 2014 model.

Data type - Float32

No Data - NaN

##### DEA Intertidal lowest astronomical tide

The lowest astronomical tide dataset maps the lowest astronomical tide (LAT) for each pixel, as modelled by the FES 2014 for the 2020-2022 temporal epoch.

Data type - Float32

No Data - NaN

##### DEA Intertidal highest astronomical tide

The highest astronomical tide dataset maps the highest astronomical tide (HAT) for each pixel, as modelled by the FES 2014 for the 2020-2022 temporal epoch.

Data type - Float32

No Data - NaN

## Lineage

The product differs from previous methods used to model the elevation of the intertidal zone which have predominately focused on extracting waterlines from a limited selection of satellite images using manual digitisation and visual interpretation (e.g. Chen and Rau 1998; Zhao et al. 2008; Liu et al. 2013; Chen et al. 2016). This manual process introduces subjectivity, is impractical to apply at a continental-scale, and has inherent restrictions based on the availability of high quality image data at appropriate tidal stages. By developing an automated approach to generating satellite-derived elevation data based on a 30 year time series of observations managed within the Digital Earth Australia (DEA) platform, we were able to produce the first continental-scale three-dimensional model of the intertidal zone.

## Processing steps

1. Extract waterline contours along boundary of each ITEM tidal interval (i.e. each ten percent of the observed tidal range)

1. Assign contours with median and standard deviation tide heights of Landsat observations for each tidal interval

1. Generate continuous elevation data from median tide heights per contour using Triangulated Irregular Network interpolation

1. Clean and filter DEMs to remove noise, modelling artefacts and invalid elevation estimates

% ## Software

## References

Bishop-Taylor, R., Sagar, S., Lymburner, L., & Beaman, R. J. (2019). Between the tides: Modelling the elevation of Australia’s exposed intertidal zone at continental scale. *Estuarine, Coastal and Shelf Science*, *223*, 115–128. [https://doi.org/10.1016/j.ecss.2019.03.006](https://doi.org/10.1016/j.ecss.2019.03.006)

Carrère, L., Lyard, F., Cancet, M., Guillot, A. and Picot, N., 2016, May. FES 2014, a new tidal model—Validation results and perspectives for improvements. In Proceedings of the ESA living planet symposium (pp. 9-13).

FES2014 was produced by Noveltis, Legos and CLS and distributed by Aviso+, with support from Cnes ([https://www.aviso.altimetry.fr/](https://www.aviso.altimetry.fr/)).

