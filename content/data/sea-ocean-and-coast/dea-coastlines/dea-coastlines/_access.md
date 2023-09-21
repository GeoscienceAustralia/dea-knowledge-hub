## Access Notes

### Data download

DEA Coastlines data for the entire Australian coastline is available to download in two formats:

-   OGC GeoPackage (recommended): suitable for QGIS; includes built-in symbology for easier interpretation
-   Esri Shapefiles: suitable for ArcMap and QGIS

To download DEA Coastlines data:

1.  Click the [Link to data](https://data.dea.ga.gov.au/?prefix=derivative/dea_coastlines/2-1-0/) link above
2.  Click on either the OGC GeoPackage (`coastlines_v2.1.0.gpkg`) or Esri Shapefiles (`coastlines_v2.1.0.shp.zip`) to download the data to your computer.
3.  If you downloaded the Esri Shapefiles data, unzip the zip file by right clicking on the downloaded file and selecting `Extract all`.

To load OGC GeoPackage data in QGIS:

1.  Drag and drop the `coastlines_v2.1.0.gpkg` file into the main QGIS map window, or select it using `Layer > Add Layer > Add Vector Layer.`
2.  When prompted to `Select Vector Layers to Add`, select all layers and then `OK`.
3.  The DEA Coastlines layers will load with built-in symbology. By default, DEA Coastlines layers automatically transition based on the zoom level of the map. To deactivate this: right click on a layer in the QGIS Layers panel, click `Set Layer Scale Visibility`, and untick `Scale visibility.`

### DEA Maps

To explore DEA Coastlines on the interactive DEA Maps platform, visit the link below:

[https://maps.dea.ga.gov.au/story/DEACoastlines](https://maps.dea.ga.gov.au/#share=s-DEACoastlines&playStory=1)

To add DEA Coastlines to DEA Maps manually:

1.  Open [DEA Maps](https://maps.dea.ga.gov.au/).
2.  Select `Explore map data` on the top-left.
3.  Select `Sea, ocean and coast > DEA Coastlines > DEA Coastlines`
4.  Click the blue `Add to the map` button on top-right.

By default, the map will show hotspots of coastal change at continental scale. Red dots represent retreating coastlines (e.g. erosion), while blue dots indicate seaward growth. The larger the dots and the brighter the colour, the more coastal change that is occurring at the location. 

More detailed rates of change points will be displayed as you zoom in. To view a time series chart of how a coastal region or area of coastline has changed over time, click on any point (press "Expand" on the pop-up for more detail):

![DEA Maps zoom example](https://cmi.ga.gov.au/sites/default/files/inline-images/DEACoastLines_DEAMaps_1.gif)

Zoom in further to view individual annual shorelines:

![DEA Maps coastlines example](https://cmi.ga.gov.au/sites/default/files/inline-images/DEACoastLines_DEAMaps_2.gif)

**Note:** To view a DEA Coastlines layer that is not currently visible (e.g. rates of change points at full zoom), each layer can be added to the map individually from the `Sea, ocean and coast > DEA Coastlines > Supplementary data` directory.

### Loading DEA Coastlines data from the Web Feature Service (WFS) using Python

DEA Coastlines data can be loaded directly in a Python script or Jupyter Notebook using the DEA Coastlines Web Feature Service (WFS) and `geopandas`:

```python
import geopandas as gpd

# Specify bounding box
ymax, xmin = -33.65, 115.28
ymin, xmax = -33.66, 115.30

# Set up WFS requests for annual shorelines & rates of change points
deacl_annualshorelines_wfs = f'https://geoserver.dea.ga.gov.au/geoserver/wfs?'\
                       f'service=WFS&version=1.1.0&request=GetFeature'\
                       f'&typeName=dea:shorelines_annual&maxFeatures=1000'\
                       f'&bbox={ymin},{xmin},{ymax},{xmax},'\
                       f'urn:ogc:def:crs:EPSG:4326'
deacl_ratesofchange_wfs = f'https://geoserver.dea.ga.gov.au/geoserver/wfs?'\
                       f'service=WFS&version=1.1.0&request=GetFeature'\
                       f'&typeName=dea:rates_of_change&maxFeatures=1000'\
                       f'&bbox={ymin},{xmin},{ymax},{xmax},'\
                       f'urn:ogc:def:crs:EPSG:4326'

# Load DEA Coastlines data from WFS using geopandas
deacl_annualshorelines_gdf = gpd.read_file(deacl_annualshorelines_wfs)
deacl_ratesofchange_gdf = gpd.read_file(deacl_ratesofchange_wfs)

# Ensure CRSs are set correctly
deacl_annualshorelines_gdf.crs = 'EPSG:3577'
deacl_ratesofchange_gdf.crs = 'EPSG:3577'

# Optional: Keep only rates of change points with "good" certainty
# (i.e. no poor quality flags)
deacl_ratesofchange_gdf = deacl_ratesofchange_gdf.query("certainty == 'good'")
```

### Loading DEA Coastlines data from the Web Feature Service (WFS) using R

DEA Coastlines data can be loaded directly into R using the DEA Coastlines Web Feature Service (WFS) and the `sf` package:

```python
library(magrittr)
library(glue)
library(sf)

# Specify bounding box
xmin = 115.28
xmax = 115.30
ymin = -33.66
ymax = -33.65

# Read in DEA Coastlines annual shoreline data, using `glue` to insert our bounding
# box into the string, and `sf` to  load the spatial data from the Web Feature Service
# and set the Coordinate Reference System to Australian Albers (EPSG:3577)
deacl_annualshorelines = "https://geoserver.dea.ga.gov.au/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typeName=dea:shorelines_annual&maxFeatures=1000&bbox={ymin},{xmin},{ymax},{xmax},urn:ogc:def:crs:EPSG:4326" %>%
  glue::glue() %>%
  sf::read_sf() %>%
  sf::st_set_crs(3577)

# Read in DEA Coastlines rates of change points
deacl_ratesofchange = "https://geoserver.dea.ga.gov.au/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typeName=dea:rates_of_change&maxFeatures=1000&bbox={ymin},{xmin},{ymax},{xmax},urn:ogc:def:crs:EPSG:4326" %>%
  glue::glue() %>%
  sf::read_sf() %>%
  sf::st_set_crs(3577)
```
