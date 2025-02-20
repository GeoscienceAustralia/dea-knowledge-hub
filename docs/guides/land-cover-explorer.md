# Land Cover Explorer

[Land Cover Explorer][Explorer] is a web application for exploring [DEA Land Cover][LandCover] data. It contains tools for navigating and visualising the data.

:::{admonition} Start exploring
:class: note

Open the [Land Cover Explorer][Explorer]
:::

:::{contents} In this guide
:local:
:backlinks: none
:::

## Navigate through time and place

To navigate to a place on a map, use your mouse to zoom in and drag to move around. Or, enter an address or place into the search bar on the top left to jump directly to a location, e.g. "Warragamba Dam"

To navigate through time, drag the slider underneath **Choose a year to view** on the bottom panel. You can view data for any year for which there is coverage, from 1988 onwards.

## Level 3 vs Level 4 datasets

DEA Land Cover consists of two datasets: Level 3 and Level 4. Level 3 contains a hierarchy of classifications, and Level 4 extends this by adding further sub-classifications.

![Diagram showing the portion of the LCCS taxonomy which is implemented in DEA Land Cover v1.0.0](/_files/cmi/cut_back_0.PNG)

## View the Level 3 dataset

The Level 3 dataset allows viewing the six base Land Cover classes. These are displayed underneath **Land Use/Land Cover Classes** in the bottom panel as **Cultivated Terrestrial Vegetation**, **Natural Terrestrial Vegetation**, **Natural Aquatic Vegetation**, **Artificial Surface**, **Natural Bare Surface**, and **Water**. They are colour coded so that you can identify them on the map.

Click on a Land Cover class to view only that selected class on the map. Click the same class again to revert to viewing all the classes on the map.

## View the Level 4 dataset

[Explorer]: https://dev.mapexplorer.dea.ga.gov.au/landcoverexplorer/index.html
[LandCover]: /data/product/dea-land-cover-landsat/
