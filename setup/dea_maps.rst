.. _dea_maps:

DEA Maps
========

`Digital Earth Australia (DEA) Maps <https://maps.dea.ga.gov.au/>`_ is a website for interactive map-based access to DEA's products developed by `Data61 CSIRO`_ for `Geoscience Australia`_.

DEA Maps aims to provide easy access to DEA's products to help users to make more informed decisions.

.. _Geoscience Australia: http://www.ga.gov.au/
.. _Data61 CSIRO: https://data61.csiro.au/

Getting started with DEA Maps
-----------------------------

To explore the data available on DEA Maps:

1. Launch DEA Maps: https://maps.dea.ga.gov.au/. A pop-up window will appear:

.. figure:: /_static/DEA_maps/dea_maps_1.jpg
   :align: center
   :alt: Starting with DEA Maps

2. Click ``Take the tour``. A series of pop-up tips will appear explaining how to use the main features of DEA Maps. Click ``Next`` to proceed to the next tip, then finally ``Finish`` to complete the tour.

.. figure:: /_static/DEA_maps/dea_maps_2.jpg
   :align: center
   :alt: Guide to DEA Maps

3. Once the tour is complete, experiment with scrolling and zooming in and out of the map (use your mouse wheel, double click, or click the ``+`` or ``-`` buttons on the top right). For this example, zoom in to Lake Menindee in western New South Wales.

.. note::
   You can also zoom to a location by typing into the ``Search for locations`` box on the top-left, then clicking on your location in the drop-down menu. Try this with "Lake Menindee".

.. figure:: /_static/DEA_maps/dea_maps_3.jpg
   :align: center
   :alt: Menindee

4. Click ``Explore map data`` on the top-left to start adding data to the map. This will bring up a view of the DEA data catalogue.

.. figure:: /_static/DEA_maps/dea_maps_4.jpg
   :align: center
   :alt: Data catalogue

5. We can now add data to the map. In this example, we will load 10 m resolution satellite imagery from the Copernicus Sentinel-2 satellites. First, click on ``Satellite data`` to open this folder, then click on the ``DEA Surface Reflectance (Sentinel-2)`` product. This will show you a preview of the data we are about to load. When you are ready, click ``Add to the map``.

.. figure:: /_static/DEA_maps/dea_maps_5.jpg
   :align: center
   :alt: Adding data

6. The ``DEA Surface Reflectance (Sentinel-2)`` product will now be added to the "workbench" on the left of the screen. At this point, satellite data may not display on the map - this may be because there were no Sentinel-2 images captured over this location on the select day. To filter our satellite data to all images captured at this location, click ``Filter by location``, then click on the map. You will see the filter applied in blue in the workbench on the left.

.. figure:: /_static/DEA_maps/dea_maps_6.jpg
   :align: center
   :alt: Adding data

7. Sentinel-2 satellite data will now appear on the map. To view imagery for a different date, select a new time by clicking on the date in the workbench, or drag the time slider along the bottom of the map window.

.. figure:: /_static/DEA_maps/dea_maps_7.jpg
   :align: center
   :alt: Changing time

.. note::
   The time slider can also be used to animate satellite imagery. Click the arrow "Play" button to the left of the time slider, and control the speed of the animation using the "Play faster" and "Play slower" buttons.


Changing styles
---------------

Data on DEA Maps often contains multiple layers for each product that can be visualised to reveal important information about the Australian landscape. To view these layers:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click the white box below ``Styles`` to bring up a list of available styles for the dataset.

.. figure:: /_static/DEA_maps/dea_maps_styles_1.jpg
   :align: center
   :alt: Styles

2. From this menu, click ``False colour - Green, SWIR, NIR``. This will display a false colour view of the satellite imagery that uses wavelengths of light that are invisible to the human eye (near and short-wave infrared) to highlight the presence of water (blue) and growing vegetation (bright green).

.. figure:: /_static/DEA_maps/dea_maps_styles_2.jpg
   :align: center
   :alt: False colour

3. Experiment with selecting other styles. The list includes several specialised remote sensing indices developed to emphasise different features in the landscape:

* Vegetation (``Normalised Difference Vegetation Index - Red, NIR``)
* Water (``Normalised Difference Water Index - Green, NIR``, ``Modified Normalised Difference Water Index - Green, SWIR``)
* Algal blooms (``Normalised Difference Chlorophyll Index - Red Edge, Red``)
* Burnt areas (``Normalised Burn Ratio - NIR, SWIR``)

.. figure:: /_static/DEA_maps/dea_maps_styles_3.jpg
   :align: center
   :alt: Other styles


Sharing and printing
--------------------

DEA Maps allows you to easily create print-friendly views of satellite data for sharing outside the interactive website. It also allows you to create custom "share links" which preserve the exact layers you have loaded into the map. 

**Creating a share link**

1. Load one or more satellite datasets into your workbench and filter it them your location (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click ``Share / Print`` at the top-right of the map.

2. Click ``Copy`` to copy a customised share link to your clipboard. When opened, this link will contain an identical view of the map containing all the layers you have loaded into the map.

.. figure:: /_static/DEA_maps/dea_maps_share_1.jpg
   :align: center
   :alt: Share 1

**Showing a print view**

1. After clicking ``Share / Print`` at the top-right of the map, click ``Print`` or ``Show Print View`` to bring up a print-friendly view of your map window.

.. figure:: /_static/DEA_maps/dea_maps_share_2.jpg
   :align: center
   :alt: Share 2

.. note::
   Hint: To obtain a high quality image of your map, right click on the image at the top of the print view and select ``Save image as ...``.


Exporting data
--------------

.. note::
   This method is suitable for exporting small areas of DEA data at high resolution. To download large areas of data or multiple timesteps, please use the `DEA Sandbox <Sandbox/sandbox.rst>`_ or `NCI <NCI/README.rst>`_ analysis environments, or download directly from DEA's Amazon S3 bucket: http://dea-public-data-dev.s3-website-ap-southeast-2.amazonaws.com/
   
To export data directly from DEA Maps for use in GIS software:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click the three vertical dots on the dataset ("Show more actions"), then click ``Export``.

.. figure:: /_static/DEA_maps/dea_maps_export_1.jpg
   :align: center
   :alt: Export

2. Follow the instructions in the pop-up by clicking twice on the map to draw a rectangle. When done, press ``Download extent``.

.. figure:: /_static/DEA_maps/dea_maps_export_2.jpg
   :align: center
   :alt: Export 2

3. Satellite data for this extent will be downloaded to your PC. This data can now be loaded into GIS software like QGIS or ArcGIS.


Compare tool
------------

It can be useful to compare different satellite datasets, or imagery from different dates to investigate change over time. To do this, we can use the "Compare" tool:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click the three vertical dots on the dataset ("Show more actions"), then click ``Compare``.

.. figure:: /_static/DEA_maps/dea_maps_compare_1.jpg
   :align: center
   :alt: Compare

2. A screen splitter will appear at the centre of the map, and a new copy of our dataset will be added to the workbench. The workbench has also updated with orange labels to show that this new copy will be shown on the ``Left`` of the screen, and our original data shown on the ``Right``. 

.. figure:: /_static/DEA_maps/dea_maps_compare_2.jpg
   :align: center
   :alt: Screen splitter

3. Filter this new copy of our dataset to the same location (e.g. ``Filter by location`` then click on the map), then select a new date from the "Time" dropdown. The left-hand side of the map will update with Sentinel-2 imagery from this date. Using your mouse, you can now grab the screen splitter in the centre of the screen, and swipe from side to side to compare imagery from these two time periods side-by-side.

.. figure:: /_static/DEA_maps/dea_maps_compare_3.jpg
   :align: center
   :alt: Screen splitter 2

4. To deactive the "Compare" tool, click the orange "Compare" icon on the top right of the map.

.. figure:: /_static/DEA_maps/dea_maps_compare_4.jpg
   :align: center
   :alt: Deactiveate screen splitter

Difference tool
---------------

The "Compare" tool above allowed us to visually compare different satellite data. However, it can also be useful to quantitatively compare differences between different satellite images to reveal parts of the landscape that have changed significantly over time. To do this, we can use the more advanced "Difference" tool:

1. Load a satellite dataset into your workbench (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click the three vertical dots on the dataset ("Show more actions"), then click ``Difference``.

.. figure:: /_static/DEA_maps/dea_maps_diff_1.jpg
   :align: center
   :alt: Difference

2. The "Difference" tool will replace the workbench on the left of the map. This tool allows us to choose satellite images from two different dates, and analyse them to calculate changes across time. As a first step, tell the tool the location we want to analyse by clicking once in the middle of the map.

.. figure:: /_static/DEA_maps/dea_maps_diff_2.jpg
   :align: center
   :alt: Difference 2

3. Once the data is filtered, click on the date below ``Date Comparison A`` and ``Date Comparison B``, and use the date picker (i.e. click on the dates) to change the dates that are displayed on the left and right of the map. Try and choose two dates without clouds, as these will be used to identify parts of the landscape that have changed through time.

.. note::
   If using the Lake Menindee example, try setting ``Date Comparison A`` to ``18/04/2021`` and ``Date Comparison B`` to ``18/05/2021`` for a example of a dry and wet landscape.

.. figure:: /_static/DEA_maps/dea_maps_diff_3.jpg
   :align: center
   :alt: Difference 3

4. We can now run the change detection computation. Click ``Choose a difference output`` on the "Difference" tool. This gives us several options that can be used to compare differences in specific landscape characteristics over time (e.g. water, vegetation, fire scars). For this example, select ``Modified Normalised Difference Water Index - Green, SWIR`` which is useful for comparing the distribution of water in the landscape. When ready, click ``Generate change detection``.

.. figure:: /_static/DEA_maps/dea_maps_diff_4.jpg
   :align: center
   :alt: Difference 4

5. A new layer will appear on the map. Locations that have grown wetter over time are shown in blue, while locations that have have become drier are shown in red. Scroll around the map to explore patterns of change. To close the "Difference" tool, click "Exit" at the top of the window. 

.. figure:: /_static/DEA_maps/dea_maps_diff_5.jpg
   :align: center
   :alt: Difference 5

6. Your workbench will reappear, with the difference output layer added as a new dataset on the map.

.. figure:: /_static/DEA_maps/dea_maps_diff_6.jpg
   :align: center
   :alt: Difference 6

For more assistance
-------------------
DEA Maps contains additional helpful guides for assisting with exploring our datasets. To access this help at any point, click the ``Help`` button on the bottom-right:

.. figure:: /_static/DEA_maps/dea_maps_help_1.jpg
   :align: center
   :alt: Help 1

This will bring up a menu containing detailed guides to performing useful tasks with DEA Maps:

.. figure:: /_static/DEA_maps/dea_maps_help_2.jpg
   :align: center
   :alt: Help 2
