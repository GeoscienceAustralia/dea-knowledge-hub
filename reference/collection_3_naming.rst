DEA Naming Conventions (Collection 3) 
=========================================

Introduction
------------

Digital Earth Australia (DEA) maintains and distributes collections of
Satellite derived information sourced from a growing number of different
Satellite missions.
The DEA Naming Conventions aim to make naming of collections at rest on 
NCI THREDDS, NCI projects and AWS S3 buckets consistent across products.

This page explains the naming convention of files/datasets found within 
DEA's digital products as well as the Open Data Cube (ODC) product naming
convention.

Different types of products
------------

Depending on the type of digital product, or from which Satellite 
mission the data was sourced, products published by DEA come in 3 
principle forms:

- Analysis Ready Data (ARD) or surface reflectance. This can use 
  the World Reference System (WRS-2) if sourced from Landsat or 
  the Military Grid Reference System (MGRS) if sourced from Sentinel-2
  as its spatial reference.
- Derivative (of ARD) data that has a one to one corresponence of 
  pixels and datasets to its parent ARD. This can use WRS-2 if
  sourced from Landsat or MGRS if sourced from Sentinel-2 as its
  spatial reference.
- Derivative summary data, that is a summary of a time period (monthly,
  seasonal, calendar year, financial year, all of available time). These 
  will use the Collection 3 grid specification for its spatial reference.

Filename Examples
------------

Landsat ARD
^^^^^^^^^^^^
|ard_ls_image|

Sentinel-2 ARD
^^^^^^^^^^^^
|ard_s2_image|

Landsat Fractional Cover
^^^^^^^^^^^^
|fc_ls_image|

Sentinel-2 Water Observations
^^^^^^^^^^^^
|wo_s2_image|

Landsat Geomedian Summary
^^^^^^^^^^^^
|summary_image|

ODC Product Examples
------------

Landsat ARD ODC Product
^^^^^^^^^^^^
|odc_ard_image|

Landsat Fractional Cover ODC Product
^^^^^^^^^^^^
|odc_fc_image|

References
----------

-  `The Worldwide Reference 
   System <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>`__
-  `Wikipedia's article on the Military Grid Refrence
   System <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>`__
-  `DEA Summary Product Grid (Collection 3) <./collection_3_summary_grid.rst>`__

.. |ard_ls_image| image:: ./images/ARD_Landsat_Filename.svg
.. |ard_s2_image| image:: ./images/ARD_S-2_Filename.svg
.. |fc_ls_image| image:: ./images/Landsat_Fractional_Cover.svg
.. |wo_s2_image| image:: ./images/S-2_Water_Observations.svg
.. |summary_image| image:: ./images/Derivative_Summary_Product.svg
.. |odc_ard_image| image:: ./images/ODC_Product_ID_LS_ARD.svg
.. |odc_fc_image| image:: ./images/ODC_Product_ID_LS_FC.svg
