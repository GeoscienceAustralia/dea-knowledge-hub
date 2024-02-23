## Background

Up-to-date information about the extent and location of surface water in Australia provides us with a common understanding of this valuable and increasingly scarce resource.

## What this product offers

Digital Earth Australia Waterbodies uses Geoscience Australia’s archive of over 30 years of Landsat satellite imagery to identify where over 300,000 waterbodies are in the Australian landscape and tells us the wet surface area within those waterbodies.

The tool uses a [water classification](/data/product/dea-water-observations-landsat/) for every available Landsat satellite image and maps the locations of waterbodies across Australia. It provides a time series of wet surface area for waterbodies that are present more than 10% of the time and are larger than 2,700m2 (3 Landsat pixels).

The tool indicates changes in the wet surface area of waterbodies. This can be used to identify when waterbodies are increasing or decreasing in wet surface area.

% ## Data description

## Applications

* Understand local through to national-scale surface water dynamics over time and geography
* Provide supporting information to better manage water across Australia
* Gain insights into the severity and spatial distribution of drought
* Identify potential water sources for aerial firefighting during bushfires
* Get deeper insight into [DEA Water Observations](/data/product/dea-water-observations-landsat/) data

## Technical information

The DEA Waterbodies product is comprised of two key components:
* a polygon dataset of automatically mapped waterbody outlines, and
* a csv time series for each polygon capturing the surface area of water within each polygon at every available, clear Landsat observation. 

### Producing DEA Waterbodies

DEA Waterbodies is a polygon-based view of DEA Water Observations (DEA WO), derived through the automatic processing of DEA WO to identify the outlines of persistent waterbodies across Australia (Figure 1). 

:::{figure} /_files/cmi/V2Workflow.JPG
:alt: DEA Waterbodies workflow

Figure 1: Flow diagram outlining the steps taken to produce DEA Waterbodies v2 polygons
:::

For a detailed discussion of the methods used to produce DEA Waterbodies v1, refer to [Krause et al. 2021](https://doi.org/10.3390/rs13081437). 

## Lineage

This product builds upon [DEA Water Observations](/data/product/dea-water-observations-landsat/).

The code used in the development of this product is available on [GitHub](https://github.com/GeoscienceAustralia/dea-waterbodies).

% ## Processing steps

% ## Software

## References

Krause, Claire E., Newey, Vanessa, Alger, Matthew J., Lymburner, Leo. 2021. Mapping and Monitoring the Multi-Decadal Dynamics of Australia’s Open Waterbodies Using Landsat. Remote Sens. 13, no. 8: 1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437)

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

