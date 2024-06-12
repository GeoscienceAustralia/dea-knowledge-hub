% ## Access constraints

% ## Use constraints

:::{dropdown} How to access the data

To download DEA Intertidal data:
1. Click the [Access the data on AWS](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/) link above.
1. Click on the [ga_summary_grid_c3_32km_coastal.geojson](https://data.dea.ga.gov.au/derivative/ga_s2ls_intertidal_cyear_3/ga_summary_grid_c3_32km_coastal.geojson) file to download to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. Alternatively, you can access this file via DEA Maps to identify required tiles (**Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal 32 km tile grid**). 
1. Navigate to the required tile folder, first using the tile 'x' reference (e.g. `x079`) and then the tile 'y' reference (e.g. `y123`). Then select your year of interest.
1. Click on the required product layer to download. See [Technical Information](./?tab=details#technical-information) for details on file naming and product layer details.

:::

:::{dropdown} How to explore DEA Maps
To explore DEA Intertidal on the interactive DEA Maps platform, visit the link below:
[https://maps.dea.ga.gov.au/story/DEAIntertidal](https://maps.dea.ga.gov.au/story/DEAIntertidal)

To add DEA Coastlines to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal (Sentinel-2, Landsat)**
1. Click the **Add to the map** button on top-right.

View the product layer required by selecting the layer from the **Styles** dropdown menu, and use the **Time** selector to view the annual time-series of each product layer.

Note that the colour ramp for the **Elevation** and **Elevation Uncertainty** product layers is scaled dynamically from 'low' to 'high' to account for the wide variation of tidal ranges and elevations found across Australia, and provide the best contrast on the DEA Maps platform. 

To query an absolute value for any of the product layers, click on a location to see a plain text summary of all the DEA Intertidal product suite data values at that pixel location.
:::

:::{dropdown} How to download data via ELVIS
To order and download DEA Intertidal Elevation and Elevation Uncertainty data using the ELVIS platform, visit the link below:
[https://elevation.fsdf.org.au/](https://elevation.fsdf.org.au/)

1. Zoom into your coastal area of interest on the map
1. Click **Order data** on the top-right
1. Select your desired selection method, and click **Draw**
1. Select your area of interest on the map, then click **Search**
1. Locate the **10 Metre Intertidal DEM** results in the right-hand **Search Results** menu
1. Select the years of data you wish to download, enter your industry and email address below, then click **Order dataset**.
1. Your data will be emailed to you as a zipped folder containing DEA Intertidal Elevaton and Elevation Uncertainty GeoTIFF rasters.

:::{figure} /_files/dea-intertidal/DEAIntertidal_ELVIS_access.*
:alt: Accessing DEA Intertidal on ELVIS

Accessing DEA Intertidal Elevation data on ELVIS
:::

:::

