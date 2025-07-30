# DEA Summary Product Grids (Collection 3)

:::{contents} In this guide
:local:
:backlinks: none
:::

## Introduction

Digital Earth Australia (DEA) maintains and distributes collections of
satellite-derived information sourced from a growing number of different
satellite missions.

For DEA Collection 3, ARD and single-observation derivative products (e.g fractional cover) are
distributed in their native UTM projection in an effort to reduce:

* complexity of our pipelines,
* size on disk,
* lossy re-projection of data from native coordinate reference system.

However, statistical summary  products (e.g. geomedians) are
produced in a common grid based upon Australian Albers projection (["EPSG:3577"](https://epsg.io/3577)).
This makes all of DEA's derivative products comparable across Australia.

## What are the Collection 3 grids?

Landsat and Sentinel derivative products are built using two distinct grids.

We call these:
* DEA Landsat Summary Product Grid (Collection 3)
* DEA Sentinel Summary Product Grid (Collection 3)

The Landsat tile size is defined as $96km^2$. This results
in a raster size of $3200 \times 3200$ pixels of $30m^2$. 

For Sentinel based products, the tile size is $32km^2$ which results in a 
raster size of $3200 \times 3200$ pixels of $10m^2$.
We build Sentinel products using smaller grid tiles to enable more efficient
batch processing given the large data volumes involved.

Both grids are built from the same origin point, so the smaller tile size of
the Sentinel grid fits neatly within the Landsat grid (i.e., nine Sentinel tiles 
fit evenly within one Landsat tile)

For compatibility with file system and web access tools and protocols,
the grid has been defined to be non-negative, with the x00,y00 cell
located in the South-Western corner of the grid, and positive numbers
progressing Northward and Eastward.

The extent of these grids is based upon:

* GDA94 / Australian Albers projection coordinate reference system
  (EPSG:3577),
* Digital Earth Australia's Landsat Collection 3,
* Digital Earth Australia's Sentinel-2 Collection,
* The expanded extents of offshore islands, as detailed in the KH page: [DEA's ARD expanded processing extent](https://knowledge.dea.ga.gov.au/guides/reference/ard-expanded-processing-extent/)

Shown below is an image of both tile grids and their extents, clipped to just the region around 
mainland Australia so the grid sizes are visible.

![](/_files/reference/collection_3_grids.png)

## How can I use these grids?

These tiling grids schema have been used to subdivide processing and
storage of our continental products.
These tiling grids can be used as an overlay in other spatial systems to
determine the `xMyN` reference of a given area of interest from within a
DEA Collection 3 summary product.

## Data access

Use the links below to download the grids (as a GeoJSON), and/or view the grid extents.
```{eval-rst}
:download:`Download the Landsat grid </_files/reference/ga_sentinel_summary_grid_c3.geojson>`
```

```{eval-rst}
:download:`Download the Sentinel grid </_files/reference/ga_sentinel_summary_grid_c3.geojson`
```

[View the Landsat grid in an online map](https://maps.dea.ga.gov.au/#share=s-yUPQrYI0zfAYDldoQSqxzHjpeKx)

[Both grids are implemented in odc-dscache](https://github.com/opendatacube/odc-dscache/blob/2dc288b379945627ba2b1c58b1fa175bbaf2189b/odc/dscache/tools/tiling.py#L51C4-L71C7)
