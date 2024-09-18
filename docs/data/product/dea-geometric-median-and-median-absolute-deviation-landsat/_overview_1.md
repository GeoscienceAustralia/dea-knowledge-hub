## About

The DEA Geometric Median and Median Absolute Deviation products use statistical analyses to provide information on variance in the landscape over the given year. They provide insight into the "average" conditions observed over Australia in a given year, as well as the amount of variability experienced around that average. These products are useful for monitoring change detection, such as from cropping, urban expansion, or burnt area mapping.

:::{admonition} This version includes breaking changes
:class: note

All tile grid references have been changed to refer to a new origin point. Learn more in the [Version 4.0.0 changelog](./?tab=history#v4.0.0).
:::

:::{admonition} Bug identified
:class: note

A bug related to multithreading in numexpr has been identified which may cause a 400x400 pixel data block to be misplaced in a tile. For the full GeoMAD archive, it is possible that there are around 8-12 tiles with incorrect data (misplaced blocks). It is unknown at this stage which tiles are effected. We are investigating the bug and will provide more information soon.
:::

