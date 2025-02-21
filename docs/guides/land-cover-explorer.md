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

## Level 3 vs Level 4

DEA Land Cover consists of two datasets: Level 3 and Level 4. Level 3 contains a hierarchy of classifications, and Level 4 extends this by adding further sub-classifications. Learn more about the [Level 3 and Level 4 datasets](/data/product/dea-land-cover-landsat/?tab=description).

![Diagram showing the portion of the LCCS taxonomy which is implemented in DEA Land Cover v1.0.0](/_files/cmi/cut_back_0.PNG)

## View Level 3

Click **Level 3** in the bottom panel to view the Level 3 dataset.

The Level 3 dataset allows viewing the six base Land Cover classes. These are displayed in the **Land Use/Land Cover Classes** tool in the bottom panel as **Cultivated Terrestrial Vegetation**, **Natural Terrestrial Vegetation**, **Natural Aquatic Vegetation**, **Artificial Surface**, **Natural Bare Surface**, and **Water**. They are colour coded so that you can identify them on the map.

Click on a Land Cover class to view only that selected class on the map. Click the same class again to revert to viewing all the classes on the map. (By default, all classes are displayed on the map.)

Learn more about the [Level 3 dataset](/data/product/dea-land-cover-landsat/?tab=description).

## View Level 4

Click **Level 4** in the bottom panel to view the Level 4 dataset.

The Level 4 dataset includes the six base Land Cover classes as well as the sub-classifications of each of these. You can selectively view any classification or compilation of classifications on the map by using the **Land Use/Land Cover Classes** tool in the bottom panel. (By default, all classes are displayed on the map.)

* Tick the checkbox of any of the six base classes to view only that selected class on the map, including all sub-classifications.
* Click the name of any of these base classes to view its sub-classifications, and tick the checkbox of any of these to selectively view them on the map.
* Any combination of base classes and sub-classifications can be selectively viewed on the map.
* To reset this tool to the default values, tick then untick each of the base classes.









Click on a Land Cover class to view only that selected class on the map. Click the same class again to revert to viewing all the classes on the map. 



Learn more about the [Level 4 dataset](/data/product/dea-land-cover-landsat/?tab=description).



[Explorer]: https://dev.mapexplorer.dea.ga.gov.au/landcoverexplorer/index.html
[LandCover]: /data/product/dea-land-cover-landsat/
