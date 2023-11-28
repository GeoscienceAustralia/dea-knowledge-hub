## Changelog

This dataset is version 2 of DEA Waterbodies, and represents a reprocessing of DEA Waterbodies version 1 on [DEA Collection 3 Water Observations](/data/product/dea-water-observations-landsat/), as well as a few incremental improvements.

### DEA Waterbodies v2

The key difference between DEA Waterbodies v1 and v2 is the underlying satellite imagery used to derive the polygons, and to generate the accompanying csvs. DEA Waterbodies v1 was produced on the [DEA Water Observations from Space](https://cmi.ga.gov.au/data-products/dea/142/dea-water-observations-landsat) product, which was derived from [DEA Surface Reflectance NBART (Landsat) collection 2](https://cmi.ga.gov.au/data-products/dea/115/dea-surface-reflectance-nbart-landsat-deprecated) data. This dataset had a resolution of 25m. 

DEA Waterbodies v2 has been reprocessed on [DEA Water Observations](/data/product/dea-water-observations-landsat/), which has been run on collection 3 data, which has a pixel resolution of 30m. The reprocessing of DEA datasets to 30m resolution required that DEA Waterbodies polygon generation be re-run to re-map each waterbody using the new pixel resolution.

DEA Waterbodies v2 differs from v1 in a few additional key areas: 
* v2 polygons have a minimum size of 2,700 m2, while v1 polygons have a minimum size of 3,125 m2 ;
* There are new waterbodies in v2 not present in v1;
* There are old waterbodies in v1 that are not present in v2, mainly including very small or rarely full polygons; and
* There are waterbodies in both datasets for which the outlines have changed between v1 and v2.

#### Change in minimum polygon size

A change in the underlying pixel size necessitated a re-evaluation of the minimum polygon size. In v1, the minimum polygon size was 3,125m2, equating to 5 Landsat collection 2 pixels. 

In v2, the size has been lowered slightly to 2,700m2, which equates to 3 Landsat collection 3 pixels. 

This change has resulted in the inclusion of some smaller waterbodies that were not mapped in v1 (Figure 1). 

:::{figure} /_files/cmi/WaterbodySize_0.JPG
:alt: Waterbodies size distribution

Figure 1: Comparison of the size distributions of DEA Waterbodies v1 and v2. a) Size distribution for polygons smaller than 1km2. b) Small waterbodies identified in v2 that were not included in v1.
:::

#### Waterbody polygons manually curated in v2

Our automated waterbody polygon detection produces subpar results for large, very rarely filled waterbodies. This is particularly true of the large salt lakes in South Australia, where our method produces thousands of smaller polygons instead of the single encompassing polygon that is typically used to map these salt lakes. These subpar results come from a combination of elevation and satellite imaging effects. To mitigate these effects, we replaced the most complex large waterbodies with their counterparts in the [Surface Hydrology Polygons (Regional)](https://pid.geoscience.gov.au/dataset/ga/83134) dataset: 
* Kati Thanda-Lake Eyre (North) 
* Kati Thanda-Lake Eyre (South) 
* Lake Torrens 
* Lake Frome / Munda 
* Lake Gairdner 
* Lake Blanche 
* Lake Everard 

As an example, Kati Thanda is a particularly complex polygon when mapped using automated methods, resulting in 3,118 polygons ranging from 900 m2 to 4,609 km2. Kati Thanda and Lake Everard in v1 and v2 are shown in Figure 2. 

:::{figure} /_files/cmi/SaltLakesSwap.JPG
:alt: Complex polygons swapped for mapped polygons

Figure 2: Complex polygons replaced for large salt lakes in South Australia. Original polygons are shown in red in the foreground. The polygons that replaced these are shown in the background in blue. a) Focus on the northern edge of Kati Thanda, SA, showing the complexity of the automatically detected polygons. b) Lake Everard, SA.
:::

#### Polygon names

DEA Waterbodies polygons are named using a [geohash](https://en.wikipedia.org/wiki/Geohash) as the unique identifier for each polygon. A geohash is a representation of the lat/lon coordinates of the centre of each polygon, mapped into a shorter character string. Each polygon's geohash can be [converted](http://geohash.co/) back to a lat/lon pair to make it easy to locate a waterbody from its geohash alone. 

Polygon names/geohashes are not maintained between v1 and v2 of DEA Waterbodies. As in v1, v2 waterbody polygons are named according to the centroid of each polygon, which may have moved between versions. Note that characters at the end of a geohash string represent increasing precision in the accompanying lat/lon coordinate pair, so while the geohash is not directly maintained between versions, it is likely that they will be similar, with only the last few characters varying due to slight differences in the polygon centroids.

In order to prevent polygon identifiers being mixed up between versions, we have introduced explicit version numbers to each unique ID. This has also been applied retrospectively to v1 so that all DEA Watebody polygons are now named with a geohash and a version number. For example, in v1, Kati Thanda was originally *r4ctk0hzm*. In v1.1, the long-term release of v1, Kati Thanda was *r4ctk0hzm\_v1*. In v2 Kati Thanda is *r4ctum36x\_v2*.
