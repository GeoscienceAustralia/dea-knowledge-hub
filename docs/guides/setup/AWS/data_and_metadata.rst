.. highlight:: console

.. data_and_metadata:

Amazon Web Services
===================

DEA hosts data on the Simple Storage Service (S3) of Amazon Web Services (AWS) to facilitate direct data access. Most of the data that is stored on S3 is in the form of Cloud Optimised GeoTIFFs, which can be accessed directly without downloading the files. In addition to data, there are several services available, including an interactive code environment using Jupyter, a metadata explorer, and web services. This page provides technical documentation for using the DEA data and services on AWS.

.. contents:: In this guide
   :local:
   :backlinks: none

Data and services listing
-------------------------

* `Browse the public S3 bucket <https://data.dea.ga.gov.au/>`_ via the web.
* `DEA Explorer <https://explorer.dea.ga.gov.au/>`_ allows browsing geographic extent through time of every dataset we have available.
* The `DEA Explorer STAC endpoint <https://explorer.dea.ga.gov.au/stac/>`_ provides an API for listing and searching DEA Datasets.
* Open Geospatial Consortium Web Services are available through our `Open Web Service <https://ows.dea.ga.gov.au/>`_ and provide access to visualisations and data exports via WMS, WMTS and WCS.
* Execute custom Python code within the `DEA JupyterHub Sandbox <https://app.sandbox.dea.ga.gov.au/>`_ (see `DEA Sandbox`_ for more details).


S3 details
----------

+------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Bucket                             | Purpose                                                                                                     |
+====================================+=============================================================================================================+
| ``s3://dea-public-data``           | Stores all the public DEA Data (more than 1PB and 60M objects in August 2023)                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``s3://dea-public-data-inventory`` | A public `AWS S3 Inventory <https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html>`_ |
|                                    | of DEA Public Data. Provides a faster and more efficient content listing than crawling the data bucket.     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------+


.. note:

    If you use the public data bucket browser website_, you can replace the URL
    components with direct S3 HTTP references in the form
    ``https://dea-public-data.s3-ap-southeast-2.amazonaws.com/<path>``, so for example,
    a link like
    ``https://data.dea.ga.gov.au/baseline/ga_ls8c_ard_3/091/076/2019/07/31/ga_ls8c_nbart_3-1-0_091076_2019-07-31_final_thumbnail.jpg``
    could be changed to an S3 direct link like
    ``https://dea-public-data.s3-ap-southeast-2.amazonaws.com/baseline/ga_ls8c_ard_3/091/076/2019/07/31/ga_ls8c_nbart_3-1-0_091076_2019-07-31_final_thumbnail.jpg``.

Both S3 buckets are in the Sydney AWS region ``ap-southeast-2``. Programmatic access requires the environment variable ``AWS_NO_SIGN_REQUEST=Yes``.

Most of the data that is stored on S3 is Cloud Optimised GeoTIFFs, which can be accessed directly without downloading the files.

Key products that are available on S3 include the following:

+------------------------------------+--------------------------------------+----------------------------------------+
| DEA Product Name                   | S3 Link                              | Web View                               |
+====================================+======================================+========================================+
| `Surface Reflectance (Landsat 5)`_ | `S3: baseline/ga_ls5t_ard_3`_        | `Web: baseline/ga_ls5t_ard_3`_         |
+------------------------------------+--------------------------------------+----------------------------------------+
| `Surface Reflectance (Landsat 7)`_ | `S3: baseline/ga_ls7e_ard_3`_        | `Web: baseline/ga_ls7e_ard_3`_         |
+------------------------------------+--------------------------------------+----------------------------------------+
| `Surface Reflectance (Landsat 8)`_ | `S3: baseline/ga_ls8c_ard_3`_        | `Web: baseline/ga_ls8c_ard_3`_         |
+------------------------------------+--------------------------------------+----------------------------------------+
| `Water Observations`_              | `S3: derivative/ga_ls_wo_3`_         | `Web: derivative/ga_ls_wo_3`_          |
+------------------------------------+--------------------------------------+----------------------------------------+
| `Fractional Cover`_                | `S3: derivative/ga_ls_fc_3`_         | `Web: derivative/ga_ls_fc_3`_          |
+------------------------------------+--------------------------------------+----------------------------------------+
| `Coastlines`_                      | `S3: derivative/dea_coastlines`_     | `Web: derivative/dea_coastlines`_      |
+------------------------------------+--------------------------------------+----------------------------------------+

.. _`Surface Reflectance (Landsat 5)`: /data/product/dea-surface-reflectance-landsat-5-tm
.. _`Surface Reflectance (Landsat 7)`: /data/product/dea-surface-reflectance-landsat-7-etm
.. _`Surface Reflectance (Landsat 8)`: /data/product/dea-surface-reflectance-landsat-8-oli-tirs
.. _`Water Observations`: /data/product/dea-water-observations-landsat
.. _`Fractional Cover`: /data/product/dea-fractional-cover-landsat
.. _`Coastlines`: /data/product/dea-coastlines
.. _`S3: baseline/ga_ls5t_ard_3`: s3://dea-public-data/baseline/ga_ls5t_ard_3
.. _`S3: baseline/ga_ls7e_ard_3`: s3://dea-public-data/baseline/ga_ls7e_ard_3
.. _`S3: baseline/ga_ls8c_ard_3`: s3://dea-public-data/baseline/ga_ls8c_ard_3
.. _`S3: derivative/ga_ls_wo_3`: s3://dea-public-data/derivative/ga_ls_wo_3
.. _`S3: derivative/ga_ls_fc_3`: s3://dea-public-data/derivative/ga_ls_fc_3
.. _`S3: derivative/dea_coastlines`: s3://dea-public-data/derivative/dea_coastlines
.. _`Web: baseline/ga_ls5t_ard_3`: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls5t_ard_3
.. _`Web: baseline/ga_ls7e_ard_3`: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls7e_ard_3
.. _`Web: baseline/ga_ls8c_ard_3`: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls8c_ard_3
.. _`Web: derivative/ga_ls_wo_3`: https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_wo_3
.. _`Web: derivative/ga_ls_fc_3`: https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_fc_3
.. _`Web: derivative/dea_coastlines`: https://data.dea.ga.gov.au/?prefix=derivative/dea_coastlines


SNS Notifications
-----------------

We provide SNS notifications for newly produced DEA Datasets.

+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| SNS Topic                                                                | Description                                                                                                                |
+==========================================================================+============================================================================================================================+
| ``arn:aws:sns:ap-southeast-2:538673716275:DEANewData``                   | This topic sends `S3 Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html>`_ |
|                                                                          | for every object that lands in the ``dea-public-data`` bucket                                                              |
|                                                                          |                                                                                                                            |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3``    | This is a notification that is triggered for each new DEA Surface Reflectance scene                                        |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3-fc`` | This is a notification for each DEA Fractional Cover scene produced                                                        |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3-wo`` | This is a notification for each DEA Water Observations scene produced                                                      |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

All the the scene level notifications include a STAC 1.0.0-beta.2 JSON document
and have message attributes including the following:

+-----------------+-------------------------------------------------------------------------+
| Attribute       | Description                                                             |
+=================+=========================================================================+
| ``action``      | added or archived, whether the scene was created or deleted             |
+-----------------+-------------------------------------------------------------------------+
| ``product``     | the Open Data Cube product name for the scene                           |
+-----------------+-------------------------------------------------------------------------+
| ``datetime``    | the datetime stamp for the scene, this is the capture time of the scene |
+-----------------+-------------------------------------------------------------------------+
| ``maturity``    | the maturity level of the dataset, either "nrt", "interim" or "final"   |
+-----------------+-------------------------------------------------------------------------+
| ``bbox.ll_lon`` | lower left longitude                                                    |
+-----------------+-------------------------------------------------------------------------+
| ``bbox.ll_lat`` | lower left latitude                                                     |
+-----------------+-------------------------------------------------------------------------+
| ``bbox.ur_lon`` | upper right longitude                                                   |
+-----------------+-------------------------------------------------------------------------+
| ``bbox.ur_lat`` | upper right latitude                                                    |
+-----------------+-------------------------------------------------------------------------+

For Surface Reflectance products, the following additional attributes are included:

+---------------------------+------------------------------------------------------+
| Attribute                 | Description                                          |
+===========================+======================================================+
| ``cloud_cover``           | percentage cloud cover, a number between 0 and 100   |
+---------------------------+------------------------------------------------------+
| ``gqa_iterative_mean_xy`` | a measure of the scenes geometric accuracy in pixels |
+---------------------------+------------------------------------------------------+

.. _website: https://data.dea.ga.gov.au
.. _DEA Sandbox: /guides/setup/Sandbox/sandbox/


Download data via S3
--------------------

To learn how to download data from AWS S3, see the `Frequently Asked Questions </guides/about/faq/>`_ page.

