# Web Coverage Service (WCS)

A standard protocol for serving coverage data, which returns the data along with its original semantics (instead of 
just pictures) which may be interpreted, extrapolated, etc., and not just portrayed. With WCS you can retrieve the raw 
geospatial raster data behind an image for performing further analysis.

WCS allows selecting and downloading subsets of full multispectral images at their original spatial resolution, without 
needing to download the entire file. This allows you to limit your downloads to only the information from your area of 
interest.

## How to Connect to WCS using QGIS

This tutorial shows how to create a Web Coverage Service connection using QGIS.

1. Launch QGIS.
2. On the Menu Bar click on **Layer**.
3. A sub-menu tab will show below Layer; click on **Add Layer**, choose **Add WCS Layer**.

![QGIS - Add WCS](/_files/web-services/ows_tutorial_5.png)

4. Click on the **New** button. 
5. A dialogue will open, as shown below: Provide the following details, these can be found at the URL [https://ows.dea.ga.gov.au/](https://ows.dea.ga.gov.au/).

`Name: DEA Services`

`URL:  https://ows.dea.ga.gov.au/?service=WMS&version=1.3.0&request=GetCapabilities`

![QGIS - WCS Connection](/_files/web-services/ows_tutorial_6.png)

6. After providing the details above, click on **OK**.
7. The previous dialogue will show up, in the dropdown above the New button, you will see DEA Services, if it is not there click the dropdown button below and select it.
8. The **Connect** button will be activated, click on it to load the layers. Anytime this page is open, because the connection has already been established, click on the **Connect** button to load the data.
9. The layer will be loaded as shown below in the dialogue.

![QGIS - Loaded WCS](/_files/web-services/ows_tutorial_4.png)

10. Navigate through layers and choose the layer you will need to display on the Map Page. With WCS you can select Time and Format of Image.
11. After selecting the layer click on the **Add** button at the bottom of the dialogue.