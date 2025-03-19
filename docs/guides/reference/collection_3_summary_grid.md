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

To make information across Australia comparable, continental-scale, 
statistical summary products are produced in a common grid based upon 
Australian Albers (Albers Collection 3 grid). This page
describes how we developed this grid and how it differs from the
previous Australian Albers grid (Albers Collection 2 grid).

## How did we develop the new Collection 3 grid?

In developing this new grid, we had several goals:

* be compatible with the new resolution of Landsat ($30m^2$ from
   $25m^2$)
* be interoperable between both Landsat ($30m^2$) and Sentinel-2
   ($10m^2$, $20m^2$ and $60m^2$)
* have a naming convention that was non-negative, removing the need for
   plus and minus symbols that can be problematic for some software applications

The tile size is defined as $96km^2$. For Landsat, this will result
in a raster size of $3200 \times 3200 pixels$ of $30m^2$. For 
Sentinel-2, this will result in a raster size of $9600 \times 9600 pixels$ 
of $10m^2$.

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

Shown here is an image of the new grid in EPSG:3577 projection, with tiles shown
where we expect to have land imagery available:

![](/_files/reference/collection_3_grid.jpeg)

## How can I use this grid?

This tiling grid scheme has been used to subdivide processing and
storage of our continental products.

This tiling grid can be used as an overlay in other spatial systems to
determine the xMyN reference of a given area of interest from within a
DEA Collection 3 summary product.

Unfortunately, there is no one-to-one mapping of the new Albers
Collection 3 grid to the old Albers Collection 2 grid.

## Shift in origin point of DEA Summary Product Grid

To accommodate an expanded area of coverage of Australia's external territories, the DEA Summary Product Grid has being shifted. The south-west origin point of the grid has been being shifted from `-5472000.0, -2688000.0` to `-6912000.0, -4416000.0` (EPSG:3577). Therefore, all tile grid references have shifted 18 tiles west and 15 tiles south. For instance, a tile reference of `x10y10` has changed to `x28y25`. For a preview, see the [provisional version of the expanded DEA Summary Product Grid](https://maps.dea.ga.gov.au/#share=s-avXJqwjUtf55qGUmweYY5KYoVnI) on DEA Maps. [Download the new grid from AWS S3](https://dea-public-data.s3.ap-southeast-2.amazonaws.com/derivative/ga_summary_grid_c3_expanded.geojson)

The latest versions of all of our 'summary derivative products' have now been updated to the new origin point (but existing versions of the products were not be changed). The last product to be updated was [DEA Land Cover](/data/product/dea-land-cover-landsat/) in its version 2.0.0 release on 5 March 2025.

## References

* [View the Grid in an online map](https://maps.dea.ga.gov.au/#share=s-yUPQrYI0zfAYDldoQSqxzHjpeKx)
* [Download the Grid in GeoJSON map](https://data.dea.ga.gov.au/derivative/ga_summary_grid_c3.geojson)
* [The Grid as implemented in ODC Statistician](https://github.com/opendatacube/odc-tools/blob/dff7b984464a4cc9d6bd9f6f444ef4a292c730d0/libs/dscache/odc/dscache/tools/tiling.py#L13-L41)
