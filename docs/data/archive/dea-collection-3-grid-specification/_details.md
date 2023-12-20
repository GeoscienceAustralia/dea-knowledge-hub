## Background

The extent of this grid has been based upon the maximal extents of:

* GDA94 / Australian Albers projection coordinate reference system (EPSG:3577)
* Digital Earth Australia's Landsat collection 3
* Digital Earth Australia's Sentinel-2 Collection

For compatiblility with the resolutions of Landsat and Sentinel-2 sensors, tiles are 96km^2 in size.

For compatibility with filesystem and web access tools and protocols, the grid has been defined to be non-negative, with the x00,y00 cell in the South-Western corner of the grid.

## What this product offers

The DEA Collection 3 summary product grid specification is a tiling grid scheme shared by all DEA collection 3 summary products. 

DEA has defined a tiling scheme that is common to both Landsat and Sentinel-2 statistical summary products. To be compatible with pixels of size 10m^2, 20m^2 and 60m^2 of Sentinel-2 data as well as 30m2 Landsat data, tiles are proposed to be 96km^2 in size.

In the case of Landsat, this will result in a raster size of 3200x3200 pixels of 30m^2.

In the case of Sentinel-2, this will result in a raster size of 9600x9600 pixels of 10m^2.

% ## Data description

## Applications

This tiling grid scheme has been used to subdivide processing and storage of our continental products.

This tiling grid can be used as an overlay in other spatial systems to determine the xMyN reference of a given area of interest from within a DEA Collection 3 summary product.

% ## Technical information

% ## Lineage

% ## Processing steps

% ## Software

% ## References

