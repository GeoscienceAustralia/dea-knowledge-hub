## Background

Up-to-date information about the extent and location of surface water in Australia provides us with a common understanding of this valuable and increasingly scarce resource.

This dataset is version 3 of DEA Waterbodies, and represents a reprocessing of [DEA Waterbodies version](https://cmi.ga.gov.au/data-products/dea/693/dea-waterbodies-landsat) 2 on [DEA Collection 3 Water Observations](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat), as well as a few incremental improvements.

#FIXME improvement details

See the **"Details"** tab for a discussion of the changes between DEA Waterbodies v1,v2 and v3.

## What this product offers

Digital Earth Australia Waterbodies uses Geoscience Australia’s archive of over 30 years of Landsat satellite imagery to identify where over 300,000 waterbodies are in the Australian landscape and tells us the wet surface area within those waterbodies.

The tool uses a [water classification](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat) for every available Landsat satellite image and maps the locations of waterbodies across Australia. It provides a time series of wet surface area for waterbodies that are present more than 10% of the time and are larger than 2,700m2 (3 Landsat pixels).

The tool indicates changes in the wet surface area of waterbodies. This can be used to identify when waterbodies are increasing or decreasing in wet surface area.

% ## Data description

## Applications

* Understand local through to national-scale surface water dynamics over time and geography
* Provide supporting information to better manage water across Australia
* Gain insights into the severity and spatial distribution of drought
* Identify potential water sources for aerial firefighting during bushfires
* Get deeper insight into [DEA Water Observations](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat) data

## Technical information

The DEA Waterbodies product is comprised of two key components:

\- a polygon dataset of automatically mapped waterbody outlines, and

\- a csv time series for each polygon capturing the surface area of water within each polygon at every available, clear Landsat observation. 

#### Producing DEA Waterbodies

DEA Waterbodies is a polygon-based view of DEA Water Observations (DEA WO), derived through the automatic processing of DEA WO to identify the outlines of persistent waterbodies across Australia (Figure 1). 

![Flow diagram outlining the steps taken to produce DEA Waterbodies polygons](/sites/default/files/inline-images/V2Workflow.JPG)

##### *Figure 1: Flow diagram outlining the steps taken to produce DEA Waterbodies v2 polygons*

For a detailed discussion of the methods used to produce DEA Waterbodies v1, refer to [Krause et al. 2021](https://doi.org/10.3390/rs13081437). 

#### DEA Waterbodies v2

The key difference between DEA Waterbodies v1 and v2 is the underlying satellite imagery used to derive the polygons, and to generate the accompanying csvs. DEA Waterbodies v1 was produced on the [DEA Water Observations from Space](https://cmi.ga.gov.au/data-products/dea/142/dea-water-observations-landsat) product, which was derived from [DEA Surface Reflectance NBART (Landsat) collection 2](https://cmi.ga.gov.au/data-products/dea/115/dea-surface-reflectance-nbart-landsat-deprecated) data. This dataset had a resolution of 25m. 

DEA Waterbodies v2 has been reprocessed on [DEA Water Observations](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat), which has been run on [Landsat 5 TM Level-2 Data Products - Surface Reflectance](https://cmi.ga.gov.au/node/362) / [Landsat 7 ETM+ Level-2 Data Products - Surface Reflectance](https://cmi.ga.gov.au/node/360) / [Landsat 8 OLI/TIRS Level-2 Data Products - Surface Reflectance](https://cmi.ga.gov.au/node/361) collection 3 data, which has a pixel resolution of 30m. The reprocessing of DEA datasets to 30m resolution required that DEA Waterbodies polygon generation be re-run to re-map each waterbody using the new pixel resolution.

DEA Waterbodies v2 differs from v1 in a few additional key areas: 

* v2 polygons have a minimum size of 2,700 m2, while v1 polygons have a minimum size of 3,125 m2 ;
 
* There are new waterbodies in v2 not present in v1; 
 
* There are old waterbodies in v1 that are not present in v2, mainly including very small or rarely full polygons; and 
 
* There are waterbodies in both datasets for which the outlines have changed between v1 and v2. 
 

#### Change in minimum polygon size

A change in the underlying pixel size necessitated a re-evaluation of the minimum polygon size. In v1, the minimum polygon size was 3,125m2, equating to 5 Landsat collection 2 pixels. 

In v2, the size has been lowered slightly to 2,700m2, which equates to 3 Landsat collection 3 pixels. 

This change has resulted in the inclusion of some smaller waterbodies that were not mapped in v1 (Figure 2). 

![Comparison of the number of smaller waterbodies in v1 compared to v2. The second panel shows some waterbodies that have been included in v2 that were missed in v1.](/sites/default/files/inline-images/WaterbodySize_0.JPG)

##### *Figure 2: Comparison of the size distributions of DEA Waterbodies v1 and v2. a) Size distribution for polygons smaller than 1km2. b) Small waterbodies identified in v2 that were not included in v1.*

#### Waterbody polygons manually curated in v2

Our automated waterbody polygon detection produces subpar results for large, very rarely filled waterbodies. This is particularly true of the large salt lakes in South Australia, where our method produces thousands of smaller polygons instead of the single encompassing polygon that is typically used to map these salt lakes. These subpar results come from a combination of elevation and satellite imaging effects. To mitigate these effects, we replaced the most complex large waterbodies with their counterparts in the [Surface Hydrology Polygons (Regional)](https://ecat.ga.gov.au/geonetwork/srv/api/records/12777e32-ec4f-055a-e053-10a3070a2ce2) dataset: 

* Kati Thanda-Lake Eyre (North) 
* Kati Thanda-Lake Eyre (South) 
* Lake Torrens 
* Lake Frome / Munda 
* Lake Gairdner 
* Lake Blanche 
* Lake Everard 

As an example, Kati Thanda is a particularly complex polygon when mapped using automated methods, resulting in 3,118 polygons ranging from 900 m2 to 4,609 km2. Kati Thanda and Lake Everard in v1 and v2 are shown in Figure 3. 

![Large, complex salt lakes in v1 were swapped with polygons from the Surface Hydrology dataset in v2](/sites/default/files/inline-images/SaltLakesSwap.JPG)

##### *Figure 3: Complex polygons replaced for large salt lakes in South Australia. Original polygons are shown in red in the foreground. The polygons that replaced these are shown in the background in blue. a) Focus on the northern edge of Kati Thanda, SA, showing the complexity of the automatically detected polygons. b) Lake Everard, SA.*

#### Polygon names

DEA Waterbodies polygons are named using a [geohash](https://en.wikipedia.org/wiki/Geohash) as the unique identifier for each polygon. A geohash is a representation of the lat/lon coordinates of the centre of each polygon, mapped into a shorter character string. Each polygon's geohash can be [converted](http://geohash.co/) back to a lat/lon pair to make it easy to locate a waterbody from its geohash alone. 

Polygon names/geohashes are not maintained between v1 and v2 of DEA Waterbodies. As in v1, v2 waterbody polygons are named according to the centroid of each polygon, which may have moved between versions. Note that characters at the end of a geohash string represent increasing precision in the accompanying lat/lon coordinate pair, so while the geohash is not directly maintained between versions, it is likely that they will be similar, with only the last few characters varying due to slight differences in the polygon centroids.

In order to prevent polygon identifiers being mixed up between versions, we have introduced explicit version numbers to each unique ID. This has also been applied retrospectively to v1 so that all DEA Watebody polygons are now named with a geohash and a version number. For example, in v1, Kati Thanda was originally *r4ctk0hzm*. In v1.1, the long-term release of v1, Kati Thanda was *r4ctk0hzm\_v1*. In v2 Kati Thanda is *r4ctum36x\_v2*.

## Lineage

This product builds upon [DEA Water Observations](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat), details of which are available [here](https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat).

The code used in the development of this product is available on [GitHub](https://github.com/GeoscienceAustralia/dea-waterbodies).

% ## Processing steps

% ## Software

## References

Krause, Claire E.; Newey, Vanessa; Alger, Matthew J.; Lymburner, Leo. 2021. "Mapping and Monitoring the Multi-Decadal Dynamics of Australia’s Open Waterbodies Using Landsat" Remote Sens. 13, no. 8: 1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437)

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

