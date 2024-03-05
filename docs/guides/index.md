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

flowchart LR

%% Data

L5Data["Landsat 5 (TM)"]
L7Data["Landsat 7 (ETM+)"]
L8Data["Landsat 8 (OLI-TIRS)"]
L9Data["Landsat 9 (OLI-TIRS)"]

%% Input Products

L5SurfaceReflectance[Landsat 5 Surface Reflectance]
L7SurfaceReflectance[Landsat 7 Surface Reflectance]
L8SurfaceReflectance[Landsat 8 Surface Reflectance]
L9SurfaceReflectance[Landsat 9 Surface Reflectance]

%% Processing

Processing["Geometric Median and Median Absolute Deviation<br />algorithms with morphological cloud operations<br />on fmask (opening and dilation)"]

%% Output

GeomadLandsat5[DEA Geomedian and Median Absolute Deviation Landsat 5]
GeomadLandsat7[DEA Geomedian and Median Absolute Deviation Landsat 7]
GeomadLandsat8And9[DEA Geomedian and Median Absolute Deviation Landsat 8 and 9]

%% Flows

L5Data --> L5SurfaceReflectance --> Processing
L7Data --> L7SurfaceReflectance --> Processing
L8Data --> L8SurfaceReflectance --> Processing
L9Data --> L9SurfaceReflectance --> Processing

Processing --> GeomadLandsat5
Processing --> GeomadLandsat7
Processing --> GeomadLandsat8And9
:::
