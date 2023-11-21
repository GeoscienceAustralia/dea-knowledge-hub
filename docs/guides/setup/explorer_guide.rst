.. _explorer_guide:

DEA Explorer
============

How do we know specifically **where** and **when** data is available? Before we start any analysis, we can answer this question by verifying existing data on the Digital Earth Australia (DEA) Metadata Explorer.
The Metadata Explorer can be found at https://explorer.dea.ga.gov.au/.

Map or Explorer?
----------------
The `DEA Metadata Explorer <https://explorer.dea.ga.gov.au/>`_ and
`Digital Earth Australia (DEA) Maps <https://maps.dea.ga.gov.au/>`_ look similar, but they are designed for different purposes.

Use the `DEA Maps <https://maps.dea.ga.gov.au/>`_ if you:

* Want to see what the product or dataset looks like and interact with the data in a map viewer display

Use the `DEA Metadata Explorer <https://explorer.dea.ga.gov.au/>`_ if you:

* Want to know exactly where and when you can find data

Open the DEA Metadata Explorer
------------------------------
Open https://explorer.dea.ga.gov.au/. This will display the Metadata Explorer user interface.

.. figure:: /_static/DEA_explorer/DEA_explorer_interface_annotated.png
   :align: center
   :alt: DEA Explorer interface


The DEA Metadata Explorer has four main sections.

1. **Product selection:** This shows the currently-selected product. Click the selected product name to open the products dropdown menu.
2. **Time period:** This shows the time period for which the selected product is being displayed. Click the selected time period on the grey menu bar to open the time selection dropdown menu. The blue bar chart shows the data availability over time for the product you have selected.
3. **Map display:** This shows where data is available, for the selected time and product. Blue shaded tiles indicate the presence of data.
4. **Product information:** The sidebar shows more information about the data for the selected time and product. For example, this includes how many datasets are selected, the total area of the selected datasets, and its coordinate reference system/s.
5. **Sister sites:** This menu allows you to toggle between databases to see metadata for the production and development AWS databases, as well as the production database on the National Computational Infrastructure (NCI).

Select the Landsat 9 Analysis Ready product
-------------------------------------------
1. Click the **product selection** bar to open the dropdown menu. Select **ga_ls9c_ard_3**. This selects the Landsat 9 product.

.. figure:: /_static/DEA_explorer/DEA_explorer_select_product.png
   :align: center
   :alt: DEA Explorer product selection


2. Click the **time** bar to open the dropdown menu. Select **2022**. This will show all Landsat 9 datasets for 2022.

.. figure:: /_static/DEA_explorer/DEA_explorer_select_year.png
   :align: center
   :alt: DEA Explorer year selection


3. Click the **all months** bar to open the dropdown menu. Select **August**. This will show all the Landsat 9 datasets for August 2022.

.. figure:: /_static/DEA_explorer/DEA_explorer_select_month.png
   :align: center
   :alt: DEA Explorer month selection


4. Click the **all days** bar to open the dropdown menu. Select **11th**. This will show all the Landsat 9 datasets for 11 August 2022.

.. figure:: /_static/DEA_explorer/DEA_explorer_select_day.png
   :align: center
   :alt: DEA Explorer day selection


5. The **map display** will now show all the Landsat 9 datasets for 11 August 2022 as blue shaded boxes. Use the **+** button on the map to zoom in, and click and drag to pan the map.

.. figure:: /_static/DEA_explorer/DEA_explorer_available_data.png
   :align: center
   :alt: DEA Explorer available data


We can see that there is only data available for some parts of Australia. Let's take a closer look at Adelaide.

Zoom in on Adelaide
-------------------

Use the map's **+** button to zoom in on Adelaide.

.. figure:: /_static/DEA_explorer/DEA_explorer_Adelaide.png
   :align: center
   :alt: DEA Explorer zoom in on Adelaide


When we hover over Adelaide, we can see there there is one dataset for Adelaide for the 11 August 2022. Click on the dataset on the map.
We can now see a preview of the data for that tile, as well as all the metadata associated with that dataset below the map viewer.

.. figure:: /_static/DEA_explorer/DEA_explorer_dataset_metadata.png
   :align: center
   :alt: DEA Explorer Adelaide dataset with metadata
