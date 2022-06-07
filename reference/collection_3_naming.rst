 DEA Naming Conventions (Collection 3) 
=========================================

Introduction
------------

Digital Earth Australia (DEA) maintains and distributes collections of
Satellite derived information sourced from a growing number of different
Satellite missions.
The DEA Naming Conventions aim to make naming of collections at rest on 
NCI THREDDS, NCI projects and AWS S3 buckets consistent across products.

Different Types of Products
------------

Depending on the type of digital product, or from which Satellite 
mission the data was sourced, products published by DEA come in 3 
principle forms:
- Analysis Ready Data (ARD) or surface reflectance. This can have WRS-2 
reference if sourced from Landsat or MGRS grid tile if sourced from 
Sentinel-2
- Derivative (of ARD) data that has a one to one corresponence of 
pixels and datasets to its parent ARD. This can have WRS-2 reference if
sourced from Landsat or MGRS grid tile if sourced from Sentinel-2
- Derivative summary data, that is a summary of a time period (monthly,
seasonal, calendar year, financial year, all of available time). These 
will use the Collection 3 grid specification (link)

|ard_ls_image|

|ard_s2_image|

|fc_ls_image|

|wo_s2_image|

|summary_image|

|odc_ard_image|

|odc_fc_image|

.. |ard_ls_image| image:: ./images/ARD_Landsat_Filename.svg
.. |ard_s2_image| image:: ./images/ARD_S-2_Filename.svg
.. |fc_ls_image| image:: ./images/Landsat_Fractional_Cover.svg
.. |wo_s2_image| image:: ./images/S-2_Water_Observations.svg
.. |summary_image| image:: ./images/Derivative_Summary_Product.svg
.. |odc_ard_image| image:: ./images/ODC_Product_ID_LS_ARD.svg
.. |odc_fc_image| image:: ./images/ODC_Product_ID_LS_FC.svg
