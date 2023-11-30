
============================
 Frequently Asked Questions
============================

How do I download data from DEA?
================================

There are several options for downloading data from DEA depending on your use case:

**1) You want to download a small area of data from a specific satellite image**

Use :ref:`DEA Maps <dea_maps>` to directly export a small amount of data from the map using the :ref:`Export functionality <dea_maps_exporting>`. This is the easiest method, but it is not suitable for downloading large areas of data or multiple steps (see below).

**2) You want to download all available data for a bounding box and/or time range**

Use DEA's STAC metadata to find the data you are interested in using the `Downloading and streaming data using STAC metadata guide`_. 

.. _Downloading and streaming data using STAC metadata guide:  /notebooks/How_to_guides/Downloading_data_with_STAC/

**3) You want to download specific files from DEA's Amazon S3 buckets**

Download data directly from our `Amazon S3 buckets`_ using the AWS Command Line Interface (AWS CLI). For this you will need to know the path of the file you want to download on DEA's S3 buckets. For example, to download a single file

.. code-block:: bash

   aws s3 cp s3://dea-public-data/derivative/ga_ls_wo_fq_cyear_3/1-6-0/x11/y21/1992--P1Y/ga_ls_wo_fq_cyear_3_x11y21_1992--P1Y_final_frequency.tif . --no-sign-request

.. _Amazon S3 buckets:  /guides/setup/AWS/data_and_metadata/

To download multiple files, for example each annual DEA Water Observations frequency layer for the tile ``x11/y21``

.. code-block:: bash

   aws s3 cp s3://dea-public-data/derivative/ga_ls_wo_fq_cyear_3/1-6-0/x11/y21/ . --recursive --exclude "*" --include "*P1Y_final_frequency.tif" --no-sign-request


Why does Collection 3 ARD have a higher latency than Collection 2 ARD?
======================================================================

Collection 3 ARD appears to lag about a week behind Collection 2 ARD. When will this be fixed?

    Collection 2 ARD uses Collection 5 MODIS Bidirectional Reflectance Distribution Function 
    data (BRDF) which was decommissioned and replaced by Collection 6 BRDF as of 2018. Since 
    no real BRDF is available, Collection 2 ARD uses seasonal MODIS BRDF. In contrast, 
    Collection 3 ARD uses the "real" Collection 6 MODIS BRDF for new acquisitions, so needs 
    to "wait" until this are available. BRDF is derived from 16 days of MODIS observations 
    over the area (to ensure 16 different view/solar angles can be used to simulate the model), 
    hence the delay. To conclude, Collection 3 ARD has a higher latency than Collection 2 ARD, 
    but uses more reliable and up-to-date calibration.
