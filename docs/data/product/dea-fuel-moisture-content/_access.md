:::{dropdown} How to view the data in a web map

To view and access the data interactively, start by exploring [DEA Fuel Moisture Content on DEA Maps](https://maps.dea.ga.gov.au/story/DEAFuelMoistureContent).

Or, you can manually add the DEA Fuel Moisture Content layer to DEA Maps:

1. Open [DEA Maps](https://maps.dea.ga.gov.au).
2. Click **Explore data**.
3. Click **Hazards** &gt; **DEA Fuel Moisture Content** &gt; **DEA FMC Sentinel-2 (A, B & C)** or **DEA FMC Sentinel-2 Most Recent Observation**.
4. Click **Add to the map**, or the '**+**' symbol to add the data to the map.

:::

:::{dropdown} How to load data with Python in the DEA Sandbox (Recommended)

DEA Sandbox allows you to explore DEA’s Earth Observation datasets in a JupyterLab environment. See the guide to [get started with the DEA Sandbox](/guides/setup/Sandbox/sandbox/).

Once you have signed up to the Sandbox, click into the **DEA products** directory to find the **Introduction to DEA Fuel Moisture Content** notebook. This notebook will walk you through loading and visualising the DEA Fuel Moisture Content data.

:::

:::{dropdown} How to load data into a local environment using Python and STAC (Recommended)

Use the [DEA Explorer Spatio-Temporal Asset Catalog (STAC) API](/guides/setup/gis/stac/) to load DEA data through the [odc-stac](https://odc-stac.readthedocs.io/en/latest/) Python package.

Use `ga_s2_fmc_3_v1` for the STAC "collection" ID for DEA Fuel Moisture Content.

:::

:::{dropdown} How to add data to QGIS using the OWS web service

Note: You must be using QGIS version 3.22 or above to use the time dimension.

1. From the top menu bar, click **Layer** &gt; **Add Layer** &gt; **Add WMS/WMTS Layer**.
1. Click **New** to set up a new data source, then enter the following.
    * Name: `DEA Services`
    * URL: `https://ows.dea.ga.gov.au/`
1. Click **Connect**.
1. Once the items appear, you can choose which layers to add.
1. Click **Hazards** &gt; **DEA Fuel Moisture Content**, then select either of the following options:
    * **DEA FMC Sentinel-2 (A, B & C)** or,
    * **DEA FMC Sentinel-2 Most Recent Observation**
1. Click **Add**.

:::

:::{dropdown} How to add data to Esri using the OWS web service

1. From the top menu bar, click **Insert** &gt; **Connections** &gt; **Server** &gt; **New WMS Server**.
1. Enter the following into Server URL: `https://ows.dea.ga.gov.au/`
1. Click **OK**.
1. Once the WMS server appears in the Servers folder in the Catalog, you can choose which layers to add.
1. Open each group using the dropdown arrow and navigate to **Hazards** &gt; **DEA Fuel Moisture Content**, then select either of the following options:
    * **DEA FMC Sentinel-2 (A, B & C)** or,
    * **DEA FMC Sentinel-2 Most Recent Observation**
1. Right-click and **Add to current map** or drag onto Map.

:::

:::{dropdown} How to download data via web browser from DEA Explorer

Using the [DEA Explorer site](https://explorer.dea.ga.gov.au/products/):

1. Navigate to the [DEA FMC Sentinel-2](https://explorer.dea.ga.gov.au/products/ga_s2_fmc_3_v1) page.
2. Using the interactive map and time filters, select the tile of interest.
3. Find the GeoTIFF file under **Location** and click to download it directly.

:::

:::{dropdown} How to download data via web browser from DEA Public Data AWS

Using [DEA's Public Data site](https://data.dea.ga.gov.au/?prefix=derivative/):

1. Navigate to the [DEA FMC Sentinel-2](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_fmc_3_v1/) data folder.
2. Navigate through the folders to the tile and date of interest, then click the GeoTIFF file of the relevant layer to download it directly.

Note that to find the X and Y tile values for a particular area, you can use the interactive map in DEA Explorer (see above).

:::
