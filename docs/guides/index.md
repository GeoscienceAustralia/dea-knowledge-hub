![](/_files/logos/dea-logo-inline.svg){w=300px}

&nbsp;

# Digital Earth Australia User Guides

Digital Earth Australia is an analysis platform for satellite imagery and other Earth observations.

For more information, see the [DEA website](http://www.ga.gov.au/dea).

Digital Earth Australia is currently in beta for users with accounts on the National Computational Infrastructure (NCI) or the Digital Earth Australia Sandbox (see the [Setup introduction](/guides/setup/README/) page).

Data can be viewed on the interactive [Digital Earth Australia Maps](https://maps.dea.ga.gov.au/) platform, or accessed directly from [Amazon S3 Storage](https://data.dea.ga.gov.au).

Our OGC Web Service supporting WMS, WCS and some WPS functionality is <https://ows.services.dea.ga.gov.au/>.

If you notice an error in this documentation, things that could be explained more clearly, or things that are missing, please let us know by creating an Issue in the [dea-notebooks Github repository](https://github.com/GeoscienceAustralia/dea-notebooks/issues), and list what you would like to see changed.

:::{mermaid}
:caption: GeoMAD stands for Geometric Median and Median Absolute Deviation. Landsat 5 Surface Reflectance includes NBAR, NBART, and Observational Attributes products.

flowchart LR

subgraph DataSources["Data Source(s)"]
    L5Data["`Landsat 5 (TM)`"]
    L7Data["`Landsat 7 (ETM+)`"]
    L8Data["`Landsat 8 (OLI-TIRS)`"]
    L9Data["`Landsat 9 (OLI-TIRS)`"]
end

subgraph InputProducts["Input Product(s)"]
    L5SurfaceReflectance["`Landsat 5 Surface Reflectance`"]
    L7SurfaceReflectance["`Landsat 7 Surface Reflectance`"]
    L8SurfaceReflectance["`Landsat 8 Surface Reflectance`"]
    L9SurfaceReflectance["`Landsat 9 Surface Reflectance`"]
end

subgraph ProcessingMethods["Processing Method(s)"]
    direction TB
    Processing1["`GeoMAD algorithms with morphological cloud operations on fmask (opening and dilation)`"]
end

subgraph Outputs["Output(s)"]
    GeomadLandsat5["`DEA GeoMAD Landsat 5`"]
    GeomadLandsat7["`DEA GeoMAD Landsat 7`"]
    GeomadLandsat8And9["`DEA GeoMAD Landsat 8 and 9`"]
end

L5Data --> L5SurfaceReflectance --> ProcessingMethods
L7Data --> L7SurfaceReflectance --> ProcessingMethods
L8Data --> L8SurfaceReflectance --> ProcessingMethods
L9Data --> L9SurfaceReflectance --> ProcessingMethods

Processing1

ProcessingMethods --> GeomadLandsat5
ProcessingMethods --> GeomadLandsat7
ProcessingMethods --> GeomadLandsat8And9
:::

:::{mermaid}
:caption: The three geomedian products from Landsat with italic names are spaced out temporally. ga_ls8cls9c_gm_cyear_3 product combines images from both Landsat 8 and Landsat 9 when they are available. Only Landsat 7 geomedian is available between 2000 and 2002. 

gantt

dateFormat YYYY
axisFormat %Y
todayMarker off

section ~
    Landsat 5 (1986–2011) : 1986, 2011
    Landsat 7 (1999–2021) : 1999, 2021
    Landsat 8 (2013–2024) : 2013, 2024
    Landsat 9 (2022–2024) : 2022, 2024
:::
