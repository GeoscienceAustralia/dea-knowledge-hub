% ## Access constraints

:::{dropdown} Access the DEA Hotspots product description

The latest version of the DEA Hotspots product description is available in the [DEA Hotspots AWS documents files folder](https://hotspots.dea.ga.gov.au/files/documents). 

Look for the file named "Product Description". This document contains information about:
* How to access DEA Hotspots
* How to register for the secure DEA Hotspots site
* DEA Hotspots algorithm details
* How to access historical DEA Hotspots information

:::

:::{dropdown} How to download historic DEA Hotspots data via the DEA Hotspots website

Using the [DEA Hotspots website](https://hotspots.dea.ga.gov.au/):

1. From the right-side of the top menu bar, click **Search**.
2. Select your preferred dates. This includes all historic DEA Hotspots data.
3. Choose the Source, Attribute and State. This is optional.
4. Select your area of interest by either choosing the State in the previous step or by using the Draw function. Click **Box**, **Circle**, **Polygon** or **Freehand** for your Draw method, then click **Draw**. Proceed to create your area of interest.
5. Click **Search**.
6. Click **Download** to download the search results as either a CSV, GML, KML, JSON or Shapefile.

:::

:::{dropdown} How to download historic DEA Hotspots data in a virtual or local environment using Python

Using a virtual or local Python environment (e.g. DEA Sandbox), run the following code block to load DEA Hotspots data from the WFS for a date and location of your choice:

```python
{
    import geopandas as gpd

    #define query location bounds
    lat = (-35.9699, -35.5699)
    lon= (144.0425, 144.6425)
     
    #set maximum rows to load
    max_features = 10000
     
    #define start and end date of query
    start_date = '2002-01-01'
    end_date = '2003-01-01'
     
    #format WFS request
    hotspots_wfs = (
       f”https://hotspots.dea.ga.gov.au/geoserver/public/wfs?service=WFS”
       f"&version=1.1.0&request=GetFeature&typeName=public:hotspots"
       f"&outputFormat=application/json"
       f"&CQL_FILTER=datetime%20%3E%20%27{start_date}%27%20AND%20datetime%20%3C%20%27{end_date}%27%20"
       f"AND%20INTERSECTS(location,%20POLYGON(({lat[0]}%20{lon[0]},%20{lat[0]}%20{lon[1]},%20{lat[1]}%20{lon[1]},%20{lat[1]}%20{lon[0]},%20{lat[0]}%20{lon[0]})))"
       f"&maxFeatures={max_features}"
    )
     
    #execute request
    hotspots_gdf = gpd.read_file(hotspots_wfs)
     
    #export as your format of choice
    #example of geoJSON
    hotspots_gdf.to_file('hotspots_request_geojson.geojson', driver='GeoJSON')
    #example of shapefile
    hotspots_gdf.to_file('hotspots_request_shapefile.shp', driver='ESRI Shapefile')
}
```

:::