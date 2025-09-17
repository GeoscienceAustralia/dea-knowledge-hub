.. _continental_cogs:

Continental Cloud-Optimised GeoTIFF Mosaics
===========================================

Some Digital Earth Australia (DEA) products are provided as **continental-scale mosaics** in addition to tile-based datasets.

These datasets are made available as **Cloud-Optimised GeoTIFFs (COGs)**, a format that enables users to efficiently *stream* raster data directly from the cloud without downloading the files. This provides a fast and convenient way to access full-continental coverage from tools like QGIS or ArcGIS Pro, especially when working with large datasets.

Not all DEA products provide continental-scale COGs. Currently, this access method is only available for selected products:

- `DEA Land Cover </data/product/dea-land-cover-landsat/>`_
- `DEA Intertidal </data/product/dea-intertidal/>`_
- `DEA Tidal Composites </data/product/dea-tidal-composites/>`_

**VRT (Virtual Raster) files** are provided alongside the ``.tif`` mosaics. These files serve as lightweight wrappers around the main data and can be used to open data in GIS software with visual settings already applied. We use VRTs to provide:

- Predefined **colour legends** for classified products like Land Cover
- **Band combinations**, such as true colour (RGB), for easier visualisation

Accessing COG Mosaics in QGIS
-----------------------------

To stream DEA COGs directly in **QGIS**, follow these steps:

1. Navigate to the AWS S3 directory for the relevant DEA product:
   - `Land Cover COGs <https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_landcover_class_cyear_3/2-0-0/continental_mosaics/>`__
   - `Intertidal COGs <https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/2-0-0/continental_mosaics/>`__
   - `Tidal Composites COGs <https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/>`__

2. Choose a specific year (e.g. ``2024--P1Y``).

3. Right-click on a ``.tif`` or ``.vrt`` file and select **Copy link address**.

4. In QGIS, there are two options for loading the COG:

   **Option 1:**

   - Go to **Layer** → **Add Layer** → **Add Raster Layer**.
   - Under **Source**, next to **Raster dataset(s)**, paste the URL you copied.
   - Click **Add**.
   - If prompted with a message asking whether to stream the data, click **Yes** to avoid downloading the entire file.

   .. image:: /_files/land_cover/load-lc-cog-qgis.png
      :alt: Accessing VRT using QGIS

   **Option 2:**

   - Click **Layer** → **Add Layer** → **Add Raster Layer**.
   - For **Source Type**, select **Protocol: HTTP(S), cloud, etc.**.
   - For **Protocol Type**, select **HTTP/HTTPS/FTP**.
   - In the **URI** field, paste the copied link.
   - Click **Add** to start streaming the layer.

   .. image:: /_files/dea-tidal-composites/cogs_qgis_streaming.jpg
      :alt: Streaming COGs in QGIS

.. admonition:: Tip

   You can avoid prompting the pop-up by adding ``/vsicurl/`` before the HTTPS URL when specifying the raster source. For example:  
   ``/vsicurl/https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_landcover_class_cyear_3/2-0-0/continental_mosaics/2024--P1Y/ga_ls_landcover_class_cyear_3_mosaic_2024--P1Y_level4.vrt``

Accessing COG Mosaics in Esri ArcGIS Pro
----------------------------------------

To connect Esri ArcGIS Pro to DEA's Amazon S3 bucket, follow Esri's tutorial: `Create a cloud storage connection <https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm#ESRI_SECTION1_82576579B8CC43E6AE261E39FACFA947>`__.

1. In **ArcGIS Pro**, click the **Insert** tab → **Connections** → **Cloud Store** → **New Cloud Storage Connection**.

   .. image:: /_files/dea-tidal-composites/cog_arcgispro_connections.jpg
      :alt: Accessing the Connections and Cloud store menu in ArcGIS Pro

2. Add the following details to the **Create Cloud Storage Connection** dialog box:

   - **Connection File Name** — ``DEA_data``
   - **Service Provider** — ``AMAZON``
   - **Bucket Name (Container)** — ``dea-public-data``
   - **Region (Environment)** — ``Asia Pacific (Sydney)``
   - **Service Endpoint** — ``s3.ap-southeast-2.amazonaws.com``
   - **Provider Options**  
     - ``ARC_DEEP_CRAWL`` — ``NO``  
     - ``AWS_NO_SIGN_REQUEST`` — ``TRUE``

   .. image:: /_files/dea-tidal-composites/cog_arcgispro_cloud_connection.jpg
      :alt: Creating a cloud connection to stream Cloud Optimised GeoTIFF (COG) rasters in ArcGIS Pro

3. In the **Catalog** pane:

   - Expand **Cloud Stores**.
   - Expand the **DEA_data.acs** cloud store.
   - Navigate to the relevant product folder, e.g.:  
     ``derivative/ga_ls_landcover_class_cyear_3/2-0-0/continental_mosaics/`` or  
     ``derivative/ga_s2ls_intertidal_cyear_3/2-0-0/continental_mosaics/``.
   - Enter a directory of a particular year, e.g. ``2018--P1Y`` or ``2024--P1Y``.
   - Drag and drop the ``.tif`` or ``.vrt`` COG file onto the map (or right-click and select "Add to map").

   .. image:: /_files/dea-tidal-composites/cog_arcgispro_cloud_store.jpg
      :alt: Navigating to COGs in ArcGIS Pro

.. important::
   When adding COG files to ArcGIS Pro, select **No** when asked whether to build statistics for the layer.

.. note::
   If you experience any issues accessing or streaming DEA COG files, please contact:  
   **earth.observation@ga.gov.au**

