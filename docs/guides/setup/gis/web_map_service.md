# Web Map Service (WMS)

WMS is a standard protocol for serving georeferenced map images over the internet that are generated from a map server 
using data from a GIS database.

WMS retrieves images of geospatial data (i.e. JPG, GIF, PNG file), enabling fast (pre)viewing of data, without needing 
to download and process it. Note that this imagery does not contain any of the underlying geospatial data that was used 
to generate the image. It can be thought of as taking a screenshot of Google Maps.

## How to connect to WMS using QGIS

This tutorial shows how to set up Web Map Services in QGIS, and use it with other data on your computer such as drone 
imagery, vector or raster data. This may be useful if you cannot upload the data to the DEA Maps or the DEA Sandbox due 
to file size or internet bandwidth. It may also be useful if you feel more comfortable doing analysis in a GIS application.

Although this tutorial focuses on QGIS, the same process can be used to connect other Desktop GIS applications. 
[QGIS](https://qgis.org/en/site/) is a free and open-source desktop GIS application. You can download it from [https://qgis.org/en/site/](https://qgis.org/en/site/).

1. Launch QGIS. 
2. On the Menu Bar click on **Layer**. 
3. A sub-menu tab will show below Layer; click on **Add Layer**, choose **Add WMS/WMTS Layer**.

![QGIS - Add Layer](/_files/web-services/ows_tutorial_1.png)

4. A dialogue will open as shown below. Click on the **New** button.

![QGIS - New Layer](/_files/web-services/ows_tutorial_2.png)

5. A dialogue will open, as shown below: Provide the following details, these can be found at the URL [https://ows.dea.ga.gov.au/](https://ows.dea.ga.gov.au/).

`Name: DEA Services`
`URL:  https://ows.dea.ga.gov.au/?service=WMS&version=1.3.0&request=GetCapabilities`

![QGIS - Create New Connection](/_files/web-services/ows_tutorial_3.png)

6. After providing the details above, click on **OK**. 
7. The previous dialogue will show up, in the dropdown above the **New** button, you will see DEA Services. If it is not there click the dropdown button below and select it.
8. The **Connect** button will be activated, click on it to load the layers. Anytime this page is open, because the connection has already been established, click on **Connect** to load the data.

![QGIS - View Connection](/_files/web-services/ows_tutorial_4.png)

9. The layer will be loaded as shown below in the dialogue. 
10. Navigate through layers and choose the layer you will need to display on the Map Page. 
11. After selecting the layer, click on **Add** button at the bottom of the dialogue.
12. Close the dialogue, the selected layer will be loaded onto the Map Page.


## For web developers

The sites below provide instructions on how to load these map services onto your platform:
* [https://leafletjs.com/examples/wms/wms.html](https://leafletjs.com/examples/wms/wms.html)
* [https://openlayers.org/en/latest/examples/wms-tiled.html](https://openlayers.org/en/latest/examples/wms-tiled.html)
* [https://docs.microsoft.com/en-us/bingmaps/v8-web-control/map-control-concepts/layers/wms-tile-layer-example](https://docs.microsoft.com/en-us/bingmaps/v8-web-control/map-control-concepts/layers/wms-tile-layer-example)