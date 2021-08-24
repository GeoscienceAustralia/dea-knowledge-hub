.. _dea_maps:

DEA Maps
========

`Digital Earth Australia (DEA) Maps <https://maps.dea.ga.gov.au/>`_ is a website for interactive map-based access to DEA's products developed by `Data61 CSIRO`_ for `Geoscience Australia`_.

DEA Maps aims to provide easy access to DEA's products to help users to make more informed decisions.

.. _Geoscience Australia: http://www.ga.gov.au/
.. _Data61 CSIRO: https://data61.csiro.au/

Getting started with DEA Maps
-----------------------------

To explore DEA Maps:

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

6. The ``DEA Surface Reflectance (Sentinel-2)`` product will now be added to the "workbench" on the left of the screen. At this point, satellite data may not display on the map - this may be because there were no Sentinel-2 images captured over this location on the select day. To filter our satellite data to all images captured at this location, click ``Filter by location``, then click on the map. You will see the filter applied in blue in the workbench
 on the left.

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

Data on DEA Maps often contains multiple layers for each product that can be visualised to reveal important information about the Australian landscape. To access this data:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the ``DEA Surface Reflectance (Sentinel-2)`` example above). Click the white box below ``Styles`` at the bottom of the dataset box. This will bring up a list of available styles for the dataset.

.. figure:: /_static/DEA_maps/dea_maps_styles_1.jpg
   :align: center
   :alt: Styles