DEA Naming Conventions (Collection 3) 
=====================================

.. contents:: In this guide
   :local:
   :backlinks: none

Introduction
------------

This page explains the naming convention of files/datasets found within Digital 
Earth Australia's (DEA)science data products as well as the 
Open Data Cube (ODC) science data product naming convention. 

DEA maintains and distributes collections of satellite-derived information 
sourced from a growing number of different satellite missions. The DEA Naming 
Conventions aim to make naming of data collections consistent across science 
data products and platforms. 

Diffterent types of Science Data Products
-----------------------------------------

Depending on the type of science data product, or from which satellite mission 
the data was sourced, science data products published by DEA come in three 
principle forms: 

- Baseline Analysis Ready Data (ARD) or surface reflectance. This can use the 
World Reference System (WRS-2) as its spatial reference if sourced from 
Landsat, or the Military Grid Reference System (MGRS) if sourced from 
Sentinel-2. 
- Derivative (of ARD) data that has a one-to-one correspondence of pixels and 
datasets to its parent ARD. This can use WRS-2 as its spatial reference if 
sourced from Landsat, or MGRS if sourced from Sentinel-2. 
- Derivative summary data, or a summary of a time period (monthly, seasonal, 
calendar year, financial year, all of available time). These will use the 
Collection 3 grid specification for its spatial reference. 

Science Data Product naming principles
--------------------------------------

Science data product names meet the following principles: 

1. Unique names/identifiers. 
2. Human readable.
3. Ease of navigation to enable spatio-temporal navigation and minimise number 
of directory levels.
4. Consistency terminology between different representations of the data.
5. Concise directory structure that provides logical context for each step.
6. Informative base filenames that provide what, when and where.
7. No redundant information in the filename.
8. Provides distinction between other providers of similar data.
9. Provides distinction between different instances of data (i.e. maturity levels. 
10. Provides distinction between different versions of a science data product.
11. Correct level of science data product abstraction.
12. Understand limitations on filesystems.
13. Works consistently between different platforms.
14. Directories must have less than 1000 items contained within.

Naming components
-----------------
DEA product names include the following components:

- organisation - typically 'ga' for Geoscience Australia
- platform - the name of the satellite, for example ls5 for Landsat 5 or 
  s2b for Sentinel-2B
- sensor - letter designating the sensor on the satellite that the data
  was sourced from, for instance ls5t in the case of Landsat 5's Thematic 
  Mapper (TM), ls7e for Landsat 7's Enhanced Thematic Mapper (ETM), ls8c
  for Landsat 8's (C)ombined Object Land Imager (OLI) with Thermal 
  Infrared Sensor (TIRS) and s2am or s2bm for Sentinel-2A / B's MultiSpectral
  Instrument (MSI).
- product - name of product, for example fc for "Fractional Cover", wo for
  "Water Observations" or nbart for "Nadir corrected Bi-directional reflectance
  distribution function Adjusted Reflectance with Terrian illumination 
  correction" (NBAR-T).
- version - The version number of product. (See the `Versioning <#versioning>`_ section below.)
- WRS-2 code - 6 digit number defining the WRS-2 path and row (see link 
  below for more details) that the dataset covers
- MGRS grid tile - 5 letters and numbers defining the MGRS grid (see link
  below for more details) that the dataset covers
- X/Y tile reference - 6 letters and numbers defining the tile in
  the DEA Summary Product Grid (see link below for more details) that the
  dataset covers
- acquisition date (range) - could be a single date of format YYYY-MM-DD or
  a period, for instance "2017--P1Y" would denote that it covered the year of
  2017.
- product status - could be nrt for Near Real Time (NRT), interim to indicate
  neither NRT nor final or final to indicate the final version of a dataset.
- file/band name - the particular band of a product contained by the dataset,
  for instance "water" in the case of Water Observations, or band03 in the case
  of Landsat 8's green band.
- file extension - suffix of file to indicate format, in most cases this will be
  .tif for cloud optimized geotiff.

Filename Examples
-----------------

Landsat ARD
^^^^^^^^^^^
|ard_ls_image|

Sentinel-2 ARD
^^^^^^^^^^^^^^
|ard_s2_image|

Landsat Fractional Cover
^^^^^^^^^^^^^^^^^^^^^^^^
|fc_ls_image|

Sentinel-2 Water Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|wo_s2_image|

Landsat Geomedian Summary
^^^^^^^^^^^^^^^^^^^^^^^^^
|summary_image|

ODC Product Examples
--------------------

Landsat ARD ODC Product
^^^^^^^^^^^^^^^^^^^^^^^
|odc_ard_image|

Landsat Fractional Cover ODC Product
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|odc_fc_image|


Versioning
----------

Products use the 'Semantic Versioning' format: Major.Minor.Patch. E.g. ``2.1.0``. The 'Major' number is incremented when there are incompatible changes (non-backward-compatible changes); the 'minor' number is incremented when there are backward-compatible changes; and, the 'Patch' number is incremented for backward-compatible bug fixes.

References
----------

-  `The Worldwide Reference 
   System <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>`__
-  `Wikipedia's article on the Military Grid Refrence
   System <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>`__
-  `DEA Summary Product Grid (Collection 3) </guides/reference/collection_3_summary_grid/>`__

.. |ard_ls_image| image:: /_files/reference/ARD_Landsat_Filename.svg
.. |ard_s2_image| image:: /_files/reference/ARD_S-2_Filename.svg
.. |fc_ls_image| image:: /_files/reference/Landsat_Fractional_Cover.svg
.. |wo_s2_image| image:: /_files/reference/S-2_Water_Observations.svg
.. |summary_image| image:: /_files/reference/Derivative_Summary_Product.svg
.. |odc_ard_image| image:: /_files/reference/ODC_Product_ID_LS_ARD.svg
.. |odc_fc_image| image:: /_files/reference/ODC_Product_ID_LS_FC.svg
