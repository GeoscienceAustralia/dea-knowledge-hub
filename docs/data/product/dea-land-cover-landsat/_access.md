% ## Access constraints

## Use constraints

DEA Land Cover is appropriate to use at the national scale where other more detailed information on land cover is not available. Where DEA land cover shows conflicting information to state or local datasets, those datasets should be considered authoritative.

:::{dropdown} How to view the data in a web map

To view and access the data interactively:
1) Visit [DEA Maps](https://maps.dea.ga.gov.au).

2) Click `Explore map data`.

3) Select `Land and vegetation` > `DEA Land Cover` > `DEA Land Cover (Landsat)`. 

5) Click `Add to the map`, or the `+` symbol to add the data to the map.
:::

:::{dropdown} How to load data with Python in the DEA Sandbox

DEA Sandbox allows you to explore DEA’s Earth Observation datasets in a JupyterLab environment. To sign up for DEA Sandbox see the [user guide](/guides/setup/Sandbox/sandbox/)

Once you have access, click into the `DEA products` directory to find the `Introduction to DEA Land Cover` notebook on the Sandbox. This notebook will walk you through loading and visualising the DEA Land Cover data.
:::

:::{dropdown} Downloading the DEA Landcover data

DEA Land Cover data can be downloaded from DEA’s public data holdings through a web browser, or using Amazon Web Service’s Command Line Interface (AWS CLI). 

***via web browser:***

From [here](https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_landcover_class_cyear_3/2-0-0/), simply navigate to the year and tile* of interest and directly download the GeoTIFF file for the layer you’re after.

**To find x and y tile values for an area, see the Explorer [here](https://explorer.dea.ga.gov.au/products/ga_ls_landcover_class_cyear_2).**

***Bulk download using AWS CLI (for technical users):***

First you need to install AWS CLI, instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Then you can download data from the command line with a command such as:  
```
aws s3 --no-sign-request sync s3://dea-public-data/derivative/ga_ls_landcover_class_cyear_3/2-0-0/2020  C:/landcover/ --exclude "*" --include "*_level4.tif"
```

(This downloads all level4 tiles for 2020 into a folder called ‘landcover’)

**Basis of the command:**
```
aws s3 --no-sign-request sync [1][2][3][4]
```
Where:

[1] The s3 bucket and folder to download data from: e.g.,
```
s3://dea-public-data/derivative/ga_ls_landcover_class_cyear_3/2-0-0/2020
```
[2] The directory to download to: e.g.,
```
C:/landcover/
```
[3] When you want to specify specific files to download, first you need to exclude everything
```
--exclude "*"
```
[4] Then you can define what you want to include (you can add this multiple times), e.g.,
```
--include "*_level4.tif" --include "*_level4_rgb.tif"
```
:::

:::{dropdown} Adding DEA Landcover to QGIS

There are two options for adding DEA Lancover to QGIS.

1. Adding the web service
2. Uploading the downloaded individual tif files 

**Adding the web service:**

*(for the time dimension to work you need version 3.22+)*

From the drop down menus at the top select `Layer` > `Add Layer` > `Add WMS/WMTS Layer`

Click 'New' to setup a new data source, then enter
```
    Name: DEA Services

    URL: [https://ows.dea.ga.gov.au/](https://ows.dea.ga.gov.au/)
```
Click `Connect`

Once the items appear you can choose which layers to add.

Select `Land and Vegetation` > `DEA Land Cover`, then either:

* `DEA Land Cover Calendar Year (Landsat)`, then the **basic** or **detailed**
* `DEA Land Cover Environmental Descriptors`, then any of the various descriptor layers (lifeform, water seasonality etc)

Once you have selected a layer, click `Add` at the bottom of the window to add it to your project.

Temporal information can be accessed by clicking the clock icon next to the name of the layer in the layers list.

**Adding the individual tif files:**

Individual tiles can be downloaded from s3 via the above instruction, and can be then uploaded to QGIS.

Once the files are uploaded the styling for the tif files can be downloaded here: [Level 3 QGIS Style](/_files/land_cover/ga_ls_landcover_class_cyear_3_style.qml)

To add the style,

1. Select the tif files you would like the styling applied to

2. Right click and select `Properties` then `Symbology`

3. Select `Style` and the `Load Style` in the bottom left hand menu

The styling will now be applied to the tif classification file, to enable a colour representation of the land cover classifications

:::

:::{dropdown} Adding DEA Landcover to ArcMap

First add Digital Earth Australia to the GIS Servers:

1. Select `Windows` > `Catalog` > `GIS Servers` > `Add WMTS Server`

2. Enter [https://ows.dea.ga.gov.au/](https://ows.dea.ga.gov.au/) into the URL field

3. Click `OK`

Now add the layer to your map:

1. From the drop down menus at the top select `File` > `Add Data` > `Add Data...`

2. Click the `Look in` selector, and choose `GIS Servers`

3. Double click `Digital Earth Australia – OGC Web Services...`

4. Select `DEA Land Cover Calendar Year (Landsat)` or `DEA Land Cover Environmental Descriptors`

5. Click `Add`

:::
