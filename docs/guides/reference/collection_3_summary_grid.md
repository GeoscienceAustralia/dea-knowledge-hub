# DEA Summary Product Grid (Collection 3)

:::{contents} In this guide
:local:
:backlinks: none
:::

## Introduction

Digital Earth Australia (DEA) maintains and distributes collections of
satellite-derived information sourced from a growing number of different
satellite missions.

Previously, as part of DEA’s Landsat Collection 2, all Landsat Analysis
Ready Data (ARD) was re-projected from native Universal Transverse
Mercator (UTM) to Australia Albers (EPSG:3577) and tiled to a common
$100km^2$ grid. As a result, all products (single observations and
statistical summaries), were published in a common projection and grid tiling scheme.

As part of DEA Landsat Collection 3, ARD and single-observation
derivative products are now distributed in their native UTM projection
in an effort to reduce:

* complexity of our pipelines,
* size on disk,
* lossy re-projection of data from native coordinate reference system.

To make information across continental-Australia comparable,  
statistical summary products are produced in a common grid based upon 
Australian Albers (Albers Collection 3 grid). This page
describes how we developed this grid and how it differs from the
previous Australian Albers grid (Albers Collection 2 grid).

## How did we develop the new Collection 3 grids?

Landsat and Sentinel derivative products are built using two distinct grids.

We call these:
* DEA Landsat Summary Product Grid (Collection 3) and,
* DEA Sentinel Summary Product Grid (Collection 3)

The Landsat tile size is defined as $96km^2$. This results
in a raster size of $3200 \times 3200 pixels$ of $30m^2$. 

For Sentinel based products, the tile size is $32km^2$ this results in a 
raster size of $3200 \times 3200 pixels$ of $10m^2$

We build products from diferent grid schema because the volume of data
in Sentinel-2 makes it difficult to run batch processing jobs using the
$96km^2$ grid used for Landsat products. Both grids are built from the same
origin point, so the smaller tile size of the Sentinel grid fits neatly within
the Landsat grid (i.e 9 Sentinel tiles fit within 1 Landsat tile)

For compatibility with file system and web access tools and protocols,
the grid has been defined to be non-negative, with the x00,y00 cell
located in the South-Western corner of the grid, and positive numbers
progressing Northward and Eastward.

The extent of this grid is based upon the maximal extents of:

* GDA94 / Australian Albers projection coordinate reference system
  (EPSG:3577),
* Digital Earth Australia's Landsat Collection 3,
* Digital Earth Australia's Sentinel-2 Collection,
* With a 3-cell buffer for future growth.

Shown below is an image of both tile grids and their extents

![](/_files/reference/collection_3_grids.png)

## How can I use these grids?

These tiling grids schema have been used to subdivide processing and
storage of our continental products.

These tiling grids can be used as an overlay in other spatial systems to
determine the xMyN reference of a given area of interest from within a
DEA Collection 3 summary product.

Unfortunately, there is no one-to-one mapping of these Albers
Collection 3 grid to the older Albers Collection 2 grid.

## Shift in origin point

To accommodate an expanded area of coverage of Australia's external territories, the DEA Summary Product Grid has being shifted. The south-west origin point of the grid has been being shifted from `-5472000.0, -2688000.0` to `-6912000.0, -4416000.0` (EPSG:3577). Therefore, all tile grid references have shifted 18 tiles west and 15 tiles south. For instance, a tile reference of `x10y10` has changed to `x28y25`. For a preview, see the [provisional version of the expanded DEA Summary Product Grid](https://maps.dea.ga.gov.au/#share=s-avXJqwjUtf55qGUmweYY5KYoVnI) on DEA Maps. [Download the new grid from AWS S3](https://dea-public-data.s3.ap-southeast-2.amazonaws.com/derivative/ga_summary_grid_c3_expanded.geojson)

The latest versions of all of our 'summary derivative products' have now been updated to the new origin point (but existing versions of the products were not be changed). The last product to be updated was [DEA Land Cover](/data/product/dea-land-cover-landsat/) in its version 2.0.0 release on 5 March 2025.

## References

* [Download the Landsat grid in GeoJSON map](https://data.dea.ga.gov.au/derivative/ga_landsat_summary_grid_c3.geojson)
* [Download the Sentinel grid in GeoJSON map](https://data.dea.ga.gov.au/derivative/ga_sentinel_summary_grid_c3.geojson)
* [View the Landsat grid in an online map](https://maps.dea.ga.gov.au/#share=s-yUPQrYI0zfAYDldoQSqxzHjpeKx)
* [Both grids are implemented in odc-dscache](https://github.com/opendatacube/odc-dscache/blob/2dc288b379945627ba2b1c58b1fa175bbaf2189b/odc/dscache/tools/tiling.py#L51C4-L71C7)
