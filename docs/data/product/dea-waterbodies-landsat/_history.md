## Changelog

### Version 3.0.0

Version 3.0 of DEA Waterbodies uses the same underlying polygon set as DEA Waterbodies version 2. Improvements include additional supporting data for the most recent observations available through web mapping services (WMS) and DEA Maps, more metadata availability, and pipeline improvements.

The update from version 2 to version 3.0 of the DEA Waterbodies product and service was created through a collaboration between Geoscience Australia, the National Aerial Firefighting Centre, Natural Hazards Research Australia, and FrontierSI to make the product more useful in hazard applications. 

#### Key differences

DEA Waterbodies version 3.0 key improvements include: 

* New supporting data has been added to DEA Maps and web services for the most recent relevant observation.
* This supporting data includes: 
    * The last date any water was observed.
    * The most recent date that the satellite passed over the waterbody.
    * The date when attributes were updated.
    * The date that polygons of waterbody boundaries were created.
    * The dataset metadata link.
* Specifications of supporting data are now [available](./?tab=details#data-specification-tables). 
* Data will be uploaded as soon as it is received and processed. There is an approximate two-week latency in processing of the satellite imagery to an Analysis Ready Data (ARD) standard, from which the water information is then produced.
* There have been additions to the shapefile specification to support data delivery. Data specification tables have been [added](./?tab=details#data-specification-tables). 
* Our pipeline has been upgraded to a more reliable production environment.

#### Version 2 decommissioning

DEA Waterbodies version 2 will be decommissioned in coming months after a period of DEA Waterbodies version 3.0 testing. Users will be notified before we decommission version 2.

#### Polygon names

DEA Waterbodies version 3.0 polygon names remain the same as DEA Waterbodies version 2 with the version number at the end of the geohash updated. For example, in v2, Kati Thanda was `r4ctum36x_v2`. In v3.0 Kati Thanda is `r4ctum36x_v3`.

### [Version 2.0.0](/data/old-version/dea-waterbodies-landsat-2.0.0/)

Version 2 of DEA Waterbodies represents a reprocessing of DEA Waterbodies version 1 on [DEA Collection 3 Water Observations](/data/product/dea-water-observations-landsat), as well as a few incremental improvements. 

#### Key differences

The key difference between DEA Waterbodies v1 and v2 is the underlying satellite imagery used to derive the polygons, and to generate the accompanying CSVs. DEA Waterbodies v1 was produced on the [DEA Water Observations from Space](/data/product/dea-water-observations-landsat) product, which was derived from [DEA Surface Reflectance NBART (Landsat) collection 2](/data/old-version/dea-water-observations-landsat-2.1.5/) data. This dataset had a resolution of 25 m. 

DEA Waterbodies v2 has been reprocessed on [DEA Water Observations](/data/product/dea-water-observations-landsat/) which has been run on collection 3 data, with a pixel resolution of 30 m. The reprocessing of DEA datasets to 30 m resolution required that DEA Waterbodies polygon generation be re-run to re-map each waterbody using the new pixel resolution.

DEA Waterbodies v2 differs from v1 in a few additional key areas: 

* v2 polygons have a minimum size of 2,700 m<sup>2</sup>, while v1 polygons have a minimum size of 3,125 m<sup>2</sup>. 
* There are new waterbodies in v2 not present in v1.
* There are old waterbodies in v1 that are not present in v2, mainly including very small or rarely full polygons which no longer exceed the 10% presence threshold.
* There are waterbodies in both datasets for which the outlines have changed between v1 and v2.

### Change in minimum polygon size

A change in the underlying pixel size necessitated a re-evaluation of the minimum polygon size. In v1, the minimum polygon size was 3,125 m<sup>2</sup>, equating to 5 x Landsat collection 2 pixels. 

In v2, the size has been lowered slightly to 2,700 m<sup>2</sup>, which equates to 3 x Landsat collection 3 pixels. 

This change has resulted in the inclusion of some smaller waterbodies that were not mapped in v1. 

:::{figure} /_files/cmi/WaterbodySize_0.JPG
:alt: Waterbodies size distribution

Comparison of the size distributions of DEA Waterbodies v1 and v2. a) Size distribution for polygons smaller than 1 km<sup>2</sup>. b) Small waterbodies identified in v2 that were not included in v1.
:::

### Waterbody polygons manually curated in v2

Our automated waterbody polygon detection produces subpar results for large, very rarely filled waterbodies. This is particularly true of the large salt lakes in South Australia, where our method produces thousands of smaller polygons instead of the single encompassing polygon that is typically used to map these salt lakes. These subpar results come from a combination of elevation and satellite imaging effects. To mitigate these effects, we replaced the most complex large waterbodies with their counterparts in the [Surface Hydrology Polygons (Regional)](https://pid.geoscience.gov.au/dataset/ga/83134) dataset: 

* Kati Thanda-Lake Eyre (North) 
* Kati Thanda-Lake Eyre (South) 
* Lake Torrens 
* Lake Frome / Munda 
* Lake Gairdner 
* Lake Blanche 
* Lake Everard 

As an example, Kati Thanda is a particularly complex polygon when mapped using automated methods, resulting in 3,118 polygons ranging from 900 m<sup>2</sup> to 4,609 km<sup>2</sup>. Kati Thanda and Lake Everard in v1 and v2 are shown below. 

:::{figure} /_files/cmi/SaltLakesSwap.JPG
:alt: Complex polygons swapped for mapped polygons

Complex polygons replaced for large salt lakes in South Australia. Original polygons are shown in red. Blue areas show where polygons were infilled by replacement with the Surface Hydrology Polygons (Regional). a) Focus on the northern edge of Kati Thanda, SA, showing the complexity of the automatically detected polygons. b) Lake Everard, SA.
:::

#### Polygon names

DEA Waterbodies polygons are named using a [geohash](https://en.wikipedia.org/wiki/Geohash) as the unique identifier for each polygon. A geohash is a representation of the latitude/longitude coordinates of the centre of each polygon, mapped into a shorter character string. Each polygon's geohash can be [converted](http://geohash.co/) back to a latitude/longitude pair to make it easy to locate a waterbody from its geohash alone. 

Polygon names (geohashes) are not maintained between v1 and v2 of DEA Waterbodies. As in v1, v2 waterbody polygons are named according to the centroid of each polygon, which may have moved between versions. Note that characters at the end of a geohash string represent increasing precision in the accompanying latitude/longitude coordinate pair, so while the geohash is not directly maintained between versions, it is likely that they will be similar, with only the last few characters varying due to slight differences in the polygon centroids.

In order to prevent polygon identifiers being mixed up between versions, we have introduced explicit version numbers to each unique ID. This has also been applied retrospectively to v1 so that all DEA Waterbodies polygons are now named with a geohash and a version number. For example, in v1, Kati Thanda was originally `r4ctk0hzm`. In v1.1, the long-term release of v1, Kati Thanda was `r4ctk0hzm_v1`. In v2 Kati Thanda is `r4ctum36x_v2`.
