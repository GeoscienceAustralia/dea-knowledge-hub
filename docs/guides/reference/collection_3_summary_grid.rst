DEA Summary Product Grid (Collection 3) 
=======================================

.. contents:: On this page
   :local:
   :backlinks: none

Introduction
------------

Digital Earth Australia (DEA) maintains and distributes collections of
satellite-derived information sourced from a growing number of different
satellite missions.

Previously, as part of DEA’s Landsat Collection 2, all Landsat Analysis
Ready Data (ARD) was re-projected from native Universal Transverse
Mercator (UTM) to Australia Albers (EPSG:3577) and tiled to a common
:math:`100km^2` grid. As a result, all products (single observations and
statistical summaries), were published in a common projection and grid tiling scheme.

As part of DEA Landsat Collection 3, ARD and single-observation
derivative products are now distributed in their native UTM projection
in an effort to reduce:

-  complexity of our pipelines,
-  size on disk,
-  lossy re-projection of data from native coordinate reference system.


To make information across Australia comparable, continental-scale, 
statistical summary products are produced in a common grid based upon 
Australian Albers (Albers Collection 3 grid). This page
describes how we developed this grid and how it differs from the
previous Australian Albers grid (Albers Collection 2 grid).

How did we develop the new Collection 3 grid?
---------------------------------------------

In developing this new grid, we had several goals:

-  be compatible with the new resolution of Landsat (:math:`30m^2` from
   :math:`25m^2`)

-  be interoperable between both Landsat (:math:`30m^2`) and Sentinel-2
   (:math:`10m^2`, :math:`20m^2` and :math:`60m^2`)

-  have a naming convention that was non-negative, removing the need for
   plus and minus symbols that can be problematic for some software applications

The tile size is defined as :math:`96km^2`. For Landsat, this will result
in a raster size of :math:`3200 \times 3200 pixels` of :math:`30m^2`. For 
Sentinel-2, this will result in a raster size of :math:`9600 \times 9600 pixels` 
of :math:`10m^2`.

For compatibility with file system and web access tools and protocols,
the grid has been defined to be non-negative, with the x00,y00 cell
located in the South-Western corner of the grid, and positive numbers
progressing Northward and Eastward.

The extent of this grid is based upon the maximal extents of:

-  GDA94 / Australian Albers projection coordinate reference system
   (EPSG:3577),

-  Digital Earth Australia's Landsat Collection 3,

-  Digital Earth Australia's Sentinel-2 Collection,

-  With a 3-cell buffer for future growth.

Shown here is an image of the new grid in EPSG:3577 projection, with tiles shown
where we expect to have land imagery available:

|grid_image|

How can I use this grid?
------------------------

This tiling grid scheme has been used to subdivide processing and
storage of our continental products.

This tiling grid can be used as an overlay in other spatial systems to
determine the xMyN reference of a given area of interest from within a
DEA Collection 3 summary product.

Unfortunately, there is no one-to-one mapping of the new Albers
Collection 3 grid to the old Albers Collection 2 grid.

References
----------

-  `View the Grid in an online
   map <https://maps.dea.ga.gov.au/#share=s-yUPQrYI0zfAYDldoQSqxzHjpeKx>`__
-  `Download the Grid in GeoJSON
   map <https://data.dea.ga.gov.au/derivative/ga_summary_grid_c3.geojson>`__
-  `The Grid as implemented in ODC Statistician
   <https://github.com/opendatacube/odc-tools/blob/dff7b984464a4cc9d6bd9f6f444ef4a292c730d0/libs/dscache/odc/dscache/tools/tiling.py#L13-L41>`__

.. |grid_image| image:: /_files/reference/collection_3_grid.jpeg
