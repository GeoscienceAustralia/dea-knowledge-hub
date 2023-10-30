## Background

Intertidal zones are those which are exposed to the air at low tide and underwater at high tide. These include sandy beaches, tidal flats, rocky shores and reefs. 

Intertidal zones form critical habitats for a wide range of organisms, but are faced with increasing threats, including coastal erosion and a rise in sea levels.  

Accurate knowledge of the extent and topography of these regions can help assess where these threats will have the greatest impact, and provide essential information to underpin monitoring and management strategies. This data is challenging to acquire using traditional survey methods given the dynamic nature of intertidal zones and length of the Australian coastline.

## What this product offers

This product is a national dataset of the exposed intertidal zone: the land between the observed highest and lowest tide. It provides the extent and topography of the intertidal zone of Australia's coastline (excluding off-shore Territories).

This information was collated using observations in the Landsat archive since 1986. This product can be a valuable complementary dataset to both onshore LiDAR survey data and coarser offshore bathymetry data, enabling a more realistic representation of the land and ocean interface.

% ## Data description

## Applications

* Understanding the extent and topography of the Australian intertidal zone
* Environmental monitoring of migratory bird species
* Habitat mapping in coastal regions
* Hydrodynamic modelling
* Geomorphology studies of features in the intertidal zone

## Technical information

The Intertidal Extents Model product is a national scale gridded dataset characterising the spatial extents of the exposed intertidal zone, at intervals of the observed tidal range (Sagar et al. 2017). The current version (2.0) utilises all Landsat observations (5, 7, and 8) for Australian coastal regions (excluding off-shore Territories) between 1986 and 2016 (inclusive).

ITEM v2.0 has implemented an improved tidal modelling framework (see Sagar et al. 2018 and Processing Step: Create a continental scale tidal modelling framework) over that utilised in ITEM v1.0. The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent (Figure 1) to be increased to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands. 

The DEA archive and new tidal modelling framework has improved the coverage and quality of the ITEM v2.0 relative extents model, particularly in regions where AGDC cell boundaries in ITEM v1.0 produced discontinuities or the imposed v1.0 cell structure resulted in poor quality tidal modelling (see Sagar et al. 2017).

Examples of regions in ITEM v2.0 where these significant improvements have been noted include:

* **Dampier Peninsula and King Sound, WA**. Improved modelling within King Sound has removed the discontinuities seen at cell boundaries in ITEM v1.0, and expanded the extent of intertidal region being mapped.
* **Tiwi Islands, Coburg Pensinsula and Croker Island, NT**. Poor spatial representation of the regions tidal regimes in  ITEM v1.0 has been improved in v2.0 resulting in extensive onshore reefs and mudflats now being mapped. 
* The full **Great Barrier Reef** has been mapped, detailing reef structures which expose at low tide. Algorithm amendments have reduced the false positive exposed surface detections resulting from glint and sun glitter.
* **Broad Sound, QLD.** Improved tidal modelling has resulted in a smoother intertidal extent map, and a greatly improved confidence layer value for the region.
* Improvements in the coverage of the DEA archive has allowed many regions unresolved in ITEM v1.0 and showing as 'no data' to be modelled successfully in ITEM 2.0. For example, **Mornington Island, QLD, Eastern sections of Fraser Island, QLD** and pensinsulas in **Bowling Green Bay National Park near Townsville, QLD.**

#### Datasets

The Intertidal Extents Model (ITEM v2.0) consists of three datasets derived from the Landsat NBAR data managed in Digital Earth Australia for the period 1986 to 2016

**1) ITEM v2.0 TIDAL MODEL** 

The **ITEM****v2\_tidalmodel.shp** identifies the location and extents of the 306 polygons (Figure 1) used in the product, defined by the Continental Scale tidal modelling framework (see Processing Step: Create a continental scale tidal modelling framework). The shapefile also includes information on the lowest (LOT) and highest (HOT) observed tides for the cell, and hence the observed tidal range (HOT-LOT), based on tidal modelling for the time of acquisition of each of the corresponding Landsat observations in the cell polygon.

##### **Attributes:**

**ID** - Unique Polygon Identifier 

**lon** - Polygon Centroid Longitude

**lat** - Polygon Centroid Latitude

**LOT** - Lowest Observed Tide – The lowest modelled tidal height based on the acquisition times of all observations in the polygon. Relative to Mean Sea Level (MSL) (m). 

**HOT** \- Highest Observed Tide – The highest modelled tidal height based on the acquisition times of all observations in the polygon. Relative to Mean Sea Level (MSL) (m). 

**LMT** \- Lowest Modelled Tide - The lowest modelled tidal height based on the OTPS model for the full period of the archive. Relative to Mean Sea Level (MSL) (m). 

**HMT** - Highest Modelled Tide - The highest modelled tidal height based on the OTPS model for the full period of the archive. Relative to Mean Sea Level (MSL) (m). 

**2) THE RELATIVE EXTENTS MODEL v2.0**

The **Relative Extents Model *(item\_v2)*** utilises the tidal information attributed to each Landsat observation to indicate the spatial extent of intertidal substratum exposed at percentile intervals of the observed tidal range for the cell. The dataset consists of 306 raster files (NETCDF and Geotiff) corresponding to polygons of the continental scale tidal model.

##### **Naming convention:**

ITEM\_REL\_PolygonID\_CentroidLongitude\_CentroidLatitude

*e.g. ITEM\_REL\_95\_153.67\_-28.77.tif*

##### **Single Band Integer Raster:**

0 – Always water  
1 – Exposed at lowest 0-10% of the observed tidal range  
2 – Exposed at 10-20% of the observed tidal range  
3 – Exposed at 20-30% of the observed tidal range  
4 – Exposed at 30-40% of the observed tidal range  
5 – Exposed at 40-50% of the observed tidal range  
6 – Exposed at 50-60% of the observed tidal range  
7 – Exposed at 60-70% of the observed tidal range  
8 – Exposed at 70-80% of the observed tidal range  
9 - Exposed at highest 80-100% of the observed tidal range (land)  
\-6666 – No Data

**3) THE CONFIDENCE LAYER v2.0**

The **Confidence Layer (item\_v2\_conf)** reflects the confidence level of the Relative Extents Model, based on the distribution of classification metrics (see Processing Step: Calculate NDWI for each Observation) within each of the percentile intervals of the tidal range. The layer should be used to filter region/pixels in the model where the derived spatial extents may be adversely affected by data and modelling errors. The dataset consists of 306 raster files (NETCDF and Geotiff) corresponding to polygons of the continental scale tidal model.

##### **Naming Convention:**

ITEM\_STD\_PolygonID\_CentroidLongitude\_CentroidLatitude

*e.g. ITEM\_STD\_95\_153.67\_-28.77.tif*

##### **Single Band Integer Raster:**

\-6666 - No Data – Model is invalid. Indicates pixels where data quality and/or number of observations have resulted in no available observations in one or more of the percentile interval subsets.

All other values – The pixel-based average of the NDWI standard deviations calculated independently for each percentile interval of the observed tidal range.

## Lineage

The Intertidal Extents Model product analyses GA’s historic archive of satellite imagery to derive a model of the spatial extents of the intertidal zone throughout the tidal cycle. The model can assist in understanding the relative elevation profile of the intertidal zone, delineating exposed areas at differing tidal heights and stages.

The product differs from previous methods used to map the intertidal zone which have been predominately focused on analysing a small number of individual satellite images per location (e.g Ryu et al., 2002; Murray et al., 2012). By utilising a full 30 year time series of observations, the methodology enables us to overcome the requirement for clear, high quality observations acquired concurrent to the time of high and low tide.

## Processing steps

1. Create a continental scale tidal modelling framework

1. Apply the Oregon State University tidal model to coastline cells/polygons

1. Attribute coastal cells with a tidal height

1. Sort time series of observations based on tidal height

1. Mask tile observations for pixel quality

1. Calculate NDWI for each observation

1. Create binary NDWI layers and combine to create Relative Extents Model

% ## Software

## References

Sagar, S., Roberts, D., Bala, B., & Lymburner, L. (2017). Extracting the intertidal extent and topography of the Australian coastline from a 28 year time series of Landsat observations. *Remote Sensing of Environment*, *195*, 153–169. [https://doi.org/10.1016/j.rse.2017.04.009](https://doi.org/10.1016/j.rse.2017.04.009)

Sagar, S., Phillips, C., Bala, B., Roberts, D., & Lymburner, L. (2018). Generating continental scale pixel-based surface reflectance composites in coastal regions with the use of a multi-resolution tidal model. *Remote Sensing*, *10*(3), 480. [https://doi.org/10.3390/rs10030480](https://doi.org/10.3390/rs10030480)

