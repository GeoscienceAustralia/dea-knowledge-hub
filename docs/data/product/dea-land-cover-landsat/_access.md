:::{dropdown} How to view the data in a web map

To view and access the data interactively, follow these steps.

1. Visit [DEA Maps](https://maps.dea.ga.gov.au).
1. Click **Explore map data**.
1. Click **Land and vegetation** &gt; **DEA Land Cover** &gt; **DEA Land Cover (Landsat)**. 
1. Click **Add to the map**, or the '**+**' symbol to add the data to the map.

:::

:::{dropdown} How to load data with Python in the DEA Sandbox

DEA Sandbox allows you to explore DEA’s Earth Observation datasets in a JupyterLab environment. See the guide to [get started with the DEA Sandbox](/guides/setup/Sandbox/sandbox/).

Once you have signed up to the Sandbox, click into the **DEA products** directory to find the **Introduction to DEA Land Cover** notebook. This notebook will walk you through loading and visualising the DEA Land Cover data.

:::

:::{dropdown} How to download data via web browser

From [DEA's public data (ga_ls_landcover_class_cyear_3)](https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_landcover_class_cyear_3/2-0-0/), navigate through the folders to the year and tile of interest, then click the GeoTIFF file of the relevant layer to download it directly.

To find the X and Y tile values for a particular area, you can use the [DEA Explorer](https://explorer.dea.ga.gov.au/products/ga_ls_landcover_class_cyear_3).

:::

:::{dropdown} How to download data via AWS

DEA Land Cover data can be downloaded in bulk using Amazon Web Service’s Command Line Interface (AWS CLI). This method is for technical users.

1. [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
1. You can now download data from the command line using a command such as this example which downloads all level4 tiles for 2020 into a folder called ‘landcover’. You will need to modify the command based on your particular use case.

    ```bash
    aws s3 --no-sign-request sync s3://dea-public-data/derivative/ga_ls_landcover_class_cyear_3/2-0-0/2020  C:/landcover/ --exclude "*" --include "*_level4.tif"
    ```

    In this command,

    * The S3 bucket and folder to download data from is `s3://dea-public-data/derivative/ga_ls_landcover_class_cyear_3/2-0-0/2020`
    * The directory to download to is `C:/landcover/`
    * When you want to specify specific files to download, first you need to exclude everything, then you can define which files to include: `--exclude "*" --include "*_level4.tif"`

:::

:::{dropdown} How to add DEA Land Cover to QGIS using the OWS web service

Note: You must be using QGIS version 3.22 or above to use the time dimension.

1. From the top menu bar, click **Layer** &gt; **Add Layer** &gt; **Add WMS/WMTS Layer**.
1. Click **New** to set up a new data source, then enter the following.
    * Name: `DEA Services`
    * URL: `https://ows.dea.ga.gov.au/`
1. Click **Connect**.
1. Once the items appear, you can choose which layers to add.
1. Click **Land and Vegetation** &gt; **DEA Land Cover Collection 3**, then select either of the following options.
    * **DEA Land Cover Collection 3 Calendar Year (Landsat)**, then select either **Basic** or **Detailed**.
    * **DEA Land Cover Environmental Descriptors**, then select any of the various descriptor layers (**Lifeform**, **Water Seasonality**, etc.)
1. Click **Add**.

:::

:::{dropdown} How to add DEA Land Cover to QGIS using GeoTIFF files

Individual tiles can be downloaded via web browser or AWS by following the above instructions and can then be uploaded to QGIS.

The QGIS style files can be downloaded from the following locations.

* [Level 3 QGIS Style](https://dea-public-data.s3.ap-southeast-2.amazonaws.com/derivative/ga_ls_landcover_class_cyear_3/ga_ls_landcover_class_cyear_3_style.qml)
* [Level 4 QGIS Style](https://dea-public-data.s3.ap-southeast-2.amazonaws.com/derivative/ga_ls_landcover_class_cyear_3/ga_ls_landcover_class_cyear_4_style.qml)

To add the style to QGIS, do the following.

1. Select the TIF files you would like the styling applied to.
1. Right-click that selection then select **Properties** &gt; **Symbology**.
1. In the bottom left menu, click **Style** &gt; **Load Style**.

The styling will now be applied to the TIF classification file, hence enabling a colour representation of the Land Cover classifications.

:::

:::{dropdown} How to use the Digital Atlas of Australia Land Cover Explorer

[Land Cover Explorer](https://digital.atlas.gov.au/apps/16e1fac8143341aaa87f761a8a2c330e/explore) is a web application in the [Digital Atlas of Australia](https://digital.atlas.gov.au/), developed by Esri. It allows you to navigate and visualise the DEA Land Cover datasets.

Learn [how to use the Land Cover Explorer](/guides/land-cover-explorer/).

:::

:::{dropdown} How to view DEA Land Cover in the Digital Atlas of Australia

The [Digital Atlas of Australia](https://digital.atlas.gov.au/) brings together trusted national data in a central platform. It is a platform where anyone can explore, analyse, and visualise spatial data.

To create a map containing a DEA Land Cover dataset:

1. Go to either of these catalogue pages: 
    * [DEA Land Cover Level 3](https://digital.atlas.gov.au/datasets/4879aeb3e4a7446ba3f0aba4f5d4635e/explore) or
    * [DEA Land Cover Level 4](https://digital.atlas.gov.au/datasets/3626a8506a3c4ab9a424d51774131441/explore) 
1. Click the **I want to use this** menu bar from the bottom of the left-hand column
1. Click **Create a Map**
1. Click **ArcGIS Map Viewer**
1. You will now have a blank map with your DEA Land Cover layer already added in, ready to use.
1. Set the time internal to '1 year'.
    * Ensure that the time slider is enabled to allow you to navigate through the annual layers in the dataset.
    * By default, three years of data will be displayed. You'll need to change this: open the **Time slider options** from the three dots to the right of the time slider bar &gt; open **Time intervals** &gt; set the **Length of one interval** to '1 year'.

![Esri time slider options panel.](/_files/land_cover/Esri_time_options.png)

Alternatively, follow these steps to [create a map using the Digital Atlas](https://digital.atlas.gov.au/apps/6b0a217d5c704e8fb6c353d6245585ce/explore) and then add the DEA Land Cover datasets (along with as any other datasets that are of interest).

:::

:::{dropdown} How to add DEA Land Cover to your own Esri environment

1. Add the layer to your map.
    1. In the top menu bar, click **File** &gt; **Add Data** &gt; **Add Data...**
    1. Select **Add layer from URL** then add one of the following URLs.
        * For [DEA Land Cover Level 3](https://digital.atlas.gov.au/datasets/4879aeb3e4a7446ba3f0aba4f5d4635e/explore):
            ```
            https://di-daa.img.arcgis.com/arcgis/rest/services/Land_and_vegetation/DEA_Landcover_Landsat_Level3/ImageServer
            ```
        * For [DEA Land Cover Level 4](https://digital.atlas.gov.au/datasets/3626a8506a3c4ab9a424d51774131441/explore):
            ```
            https://di-daa.img.arcgis.com/arcgis/rest/services/Land_and_vegetation/DEA_Landcover_Landsat_Level4/ImageServer
            ```
    1. Note that the layer type is **ArcGIS Server web service**.
    1. Click **Add**.
1. Set the time internal to '1 year'.
    1. Ensure that the time slider is enabled to allow you to navigate through the annual layers in the dataset.
    1. By default, three years of data will be displayed. You'll need to change this: open the **Time slider options**  from the three dots to the right of the time slider bar &gt; open **Time intervals** &gt; set the **Length of one interval** to '1 year'.

Learn more about [how to add Esri web services to an ArcGIS environment](https://pro.arcgis.com/en/pro-app/latest/help/projects/available-online-resources.htm).

![Esri time slider options panel.](/_files/land_cover/Esri_time_options.png)

:::


