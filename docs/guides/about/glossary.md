# DEA Glossary

This glossary contains terms that are used by Digital Earth Australia (DEA), including several technical terms used in the fields of Earth Observation and software engineering.

<span id="acquisition"></span>

## Acquisition

An image captured by a satellite sensor.

<span id="alos"></span>

## Advanced Land Observing Satellite (ALOS)

A Japanese satellite launched in 2006. After five years of service, the satellite lost power and ceased communication 
with Earth, but remains in orbit.

<span id="aster"></span>

## Advanced Spaceborne Thermal and Reflection radiometer (ASTER)

An imaging instrument onboard Terra, the flagship satellite of NASA's Earth Observing System (EOS) launched in December 
1999. ASTER data is used to create detailed maps of land surface temperature, reflectance, and elevation. Learn more:
[NASA: ASTER.](https://asterweb.jpl.nasa.gov/)

<span id="avhrr"></span>

## Advanced Very-High Resolution Radiometer (AVHRR)

A radiation-detection sensor that can be used for remotely determining cloud cover and the surface temperature. AVHRR 
instruments are carried by the National Oceanic and Atmospheric Administration (NOAA) family of polar orbiting 
and European MetOp satellites. Learn more: [ESA: AVHRR.](https://earth.esa.int/eogateway/missions/noaa)

<span id="aerosol-optical-depth"></span>

## Aerosol optical depth

Aerosol optical depth is a measure of the extinction of the solar beam by dust and haze. Learn more: [NASA Earth Observatory.](https://earthobservatory.nasa.gov/global-maps/MODAL2_M_AER_OD)

<span id="albedo"></span>

## Albedo

The fraction of light that a surface reflects. Albedo is measured on a scale of 0-1, with 1 indicating that all light 
has been reflected by the surface.

<span id="algorithm"></span>

## Algorithm

In the context of remote sensing, algorithms generally specify how to determine higher-level data products from 
lower-level source data. For example, algorithms prescribe how atmospheric temperature and moisture profiles are 
determined from a set of radiation observations originally sensed by satellite sounding instruments.

<span id="ancillary"></span>

## Ancillary datasets

Data which enhance processing and utilisation of remote sensing instrument data. Ancillary datasets are used to assist
in the analysis and classification of e.g. [ARD](#ard) by providing supporting data on conditions at the time of 
satellite data acquisition, such as aerosol and water vapour concentrations. 

<span id="aws"></span>

## Amazon Web Services (AWS)

One of the two environments used for hosting [Digital Earth Australia](#dea). Amazon Web Services is a commercial cloud 
computing provider. Used by Digital Earth Australia for our JupyterHub [Sandbox](#dea-sandbox) and Web Mapping Services.

<span id="ard"></span>

## Analysis Ready Data (ARD)

Satellite data that has been processed to a minimum set of requirements and organised into a form that allows 
immediate analysis and interoperability through time and with other datasets.

<span id="api"></span>

## Application Programming Interface (API)

A software intermediary that allows two applications to talk to each other. The 
[Open Data Cube](#odc) API gives programmers full access to the capabilities of the Cube, 
allowing query and advanced data retrieval.

<span id="atm-corr"></span>

## Atmospheric correction

The process of removing the effects of the atmosphere on the reflectance values of images taken by satellite or 
airborne sensors.

<span id="agdc"></span>

## Australian Geoscience Data Cube (AGDC)

A collaborative prototype project between Geoscience Australia, [CSIRO](#csiro) and 
[NCI](#nci), which aimed to  provide better public access to NASA’s extensive Landsat archive. 
The AGDC has since been superseded by [Digital Earth Australia](#dea).

<span id="are"></span>

## Australian Research Environment (ARE)

The ARE is an interface for using the data and software available on the [NCI](#nci). 
It is a replacement for the old [VDI](#vdi) system. Learn more:
[Australian Research Environment](https://are.nci.org.au/).

<span id="azimuth"></span>

## Azimuth

The angle of an object’s position from true north.

<span id="azimuth-exit"></span>

## Azimuthal exiting (degrees)

The angle between true north and the exiting direction in the slope geometry.

<span id="azimuth-inc"></span>

## Azimuthal incident (degrees)

The angle between true north and the incident direction in the slope geometry.

<span id="band"></span>

## Band

Each remote sensing instrument (i.e. a satellite) can observe the Earth at multiple
wavelengths. A single, discrete wavelength interval or range is referred to as a band.

<span id="barest-earth"></span>

## Barest Earth

An estimate of the spectra of the barest state (i.e. least vegetation) observed from imagery of the Australian 
continent collected by the Landsat 5, 7, and 8 satellites.

<span id="brdf"></span>

## Bidirectional Reflectance Distribution Function (BRDF)

Bidirectional reflectance distribution function is a theoretical concept that describes the relationship between light 
and an opaque surface. It uses a target's irradiance geometry and the remote sensing system’s relative angle to the 
target.

<span id="brdf-albedo"></span>

## Bidirectional Reflectance Distribution Function (BRDF) / Albedo Parameter

The BRDF/Albedo parameters provide: a) coefficients for mathematical functions that describe the BRDF of each pixel in the seven [MODIS](#modis) 'Land' bands (1- 7); and, b) [albedo](#albedo) measurements derived simultaneously from the BRDF for bands 1&ndash;7 as well as three broad bands (0.4&ndash;0.7, 0.7&ndash;3.0, and 0.4&ndash;3.0 micrometers). Learn more: [NASA BRDF/Albedo parameters](https://modis.gsfc.nasa.gov/data/dataprod/mod43.php).

<span id="cog"></span>

## Cloud Optimised GeoTIFF (COG)

A data file format optimised for efficient workflows on the cloud and partial file access.

<span id="collection"></span>

## Collection

All products downstream of the rawest form of the main input data ([telemetry](#telemetry)), 
produced sequentially and processed with consistent algorithms/code/inputs/outputs.

<span id="c2"></span>

## Collection 2 (C2)

Digital Earth Australia's second [collection](#collection) of Landsat data. Now superseded by 
[Collection 3](#c3). Note that there was no DEA Collection 2 of Sentinel 2 products.

<span id="c3"></span>

## Collection 3 (C3)

The third [collection](#collection) of Digital Earth Australia's Landsat or Sentinel 2 data, 
and the most up-to-date collection available.

<span id="collection-upgrade"></span>

## Collection upgrade

The reproduction of the [collection](#collection), including all downstream products, with the 
initial input being the rawest form ([telemetry](#telemetry)). Collections are updated when 
there are fundamental changes and upgrades to the data suite that make it incompatible with the existing collection. 
Therefore, a collection upgrade is more akin to a movie franchise reboot than a re-release.

<span id="ceos-seo"></span>

## Committee on Earth Observations, Systems Engineering Office (CEOS-SEO)

Established in 1984, CEOS is the primary forum for the international coordination of space-based Earth observations. 
The SEO performs historical coverage analyses using the data archives for the Landsat, Sentinel-1, and Sentinel-2 missions.

<span id="csiro"></span>

## Commonwealth Scientific and Industrial Research Organisation (CSIRO)

An Australian federal government agency responsible for scientific research. Learn more: [CSIRO](https://www.csiro.au/).

<span id="crs"></span>

## Coordinate reference system (CRS)

A mathematical method of assigning coordinates to locations on the Earth's surface. There are many different CRSs in use, including Australian Albers (EPSG:3577) which is used for DEA's derived products.

<span id="cophub"></span>

## Copernicus Australasia Regional Data Hub

Copernicus Australasia is a regional hub supporting the [Copernicus Program](#cop-prog). The 
Copernicus Australasia Regional Data Hub provides free and open access to data from Europe's Sentinel satellite
missions for the following South-East Asia and South Pacific region. Learn more:
[Copernicus Australasia](https://www.copernicus.gov.au/).

<span id="cop-prog"></span>

## Copernicus Programme

The Copernicus Programme, established in 2014, is the European Union (EU)'s Earth observation programme coordinated and 
managed by the European Commission in partnership with the European Space Agency (ESA), the EU Member States and EU 
Agencies. Learn more: [Copernicus Programme](https://www.copernicus.eu/en).

<span id="dataset"></span>

## Dataset

A related set of files composed of separate elements that can be manipulated as a unit. It is an instantiation of a 
[product](#product).

<span id="dea"></span>

## Digital Earth Australia (DEA)

A Program of [Geoscience Australia](#ga) that uses spatial data and images recorded by satellites 
orbiting our planet to detect physical changes across Australia. DEA prepares these vast volumes of Earth observation 
data and makes it available to governments and industry for easy use. DEA is the Australian implementation of the 
[Open Data Cube](#odc). Learn more: [Digital Earth Australia](https://www.dea.ga.gov.au/).

<span id="dea-nb"></span>

## DEA Notebooks

An open-source repository containing [Jupyter Notebooks](#jupyter-nb), tools and workflows for 
geospatial analysis with [Open Data Cube](#odc) and [xarray](#xarray). Learn more:
[dea-notebooks GitHub repository](https://github.com/GeoscienceAustralia/dea-notebooks).

<span id="dea-sandbox"></span>

## DEA Sandbox

The Digital Earth Australia Sandbox is a learning and analysis environment for getting started with DEA and the 
[Open Data Cube](#odc). It includes sample data and [Jupyter Notebooks](#jupyter-nb) that demonstrate the capability 
of the [Open Data Cube](#odc). Learn more:
[DEA Notebooks Wiki](https://github.com/GeoscienceAustralia/dea-notebooks/wiki).

<span id="deafrica"></span>

## Digital Earth Africa (DE Africa)

A sister project to Digital Earth Australia but for the African Continent. Learn more: [Digital Earth Africa](https://www.digitalearthafrica.org/).

<span id="dynamic-range"></span>

## Dynamic range

The range between the maximum and minimum amount of input radiant energy that an instrument can measure.

<span id="eo"></span>

## Earth Observation (EO)

The process of acquiring observations of the Earth's surface via remote sensing instruments. These can include 
satellite-based observations, as well as drone or aerial images.

<span id="etmp"></span>

## Enhanced Thematic Mapper Plus (ETM+)

The sensor aboard Landsat 7 that picks up solar radiation reflected by or emitted from the Earth. It is an enhanced 
version of the [Thematic Mapper](#tm). Learn more:
[NASA Enhanced Thematic Mapper Plus](https://landsat.gsfc.nasa.gov/etm-plus/).

<span id="ephemeris"></span>

## Ephemeris

A table of satellite orbital locations for specific time intervals. The ephemeris data helps characterise the 
conditions under which remotely sensed data is collected and is commonly used to correct the sensor data before analysis.

<span id="esa"></span>

## European Space Agency (ESA)

The European Space Agency is a European intergovernmental collaboration focussed on the development of Europe's space 
capability. The ESA is a partner of the [Copernicus Programme](#cop-prog).

<span id="exiting-angle"></span>

## Exiting angle (degrees)

The angle between a ray reflected from a surface and the line perpendicular to the surface at the point of emergence.

<span id="final"></span>

## Final

A stage in DEA's dataset maturity lifecycle. DEA’s best quality [ARD](#ard), produced using high quality [ancillary](#ancillary) 
datasets derived from observed data. Learn more: [DEA dataset maturity](/guides/reference/dataset_maturity_guide#final).

<span id="fc"></span>

## Fractional Cover (FC)

Fractional Cover (FC) is a DEA product that uses an algorithm to split the landscape into three parts, or fractions: green (leaves, grass, and growing crops), brown (branches, dry grass or hay, and dead leaf litter), and bare ground (soil or rock). FC provides a representation of the proportions of living vegetation, dry and dying vegetation (including deciduous trees during autumn, dying grass, etc.), and bare soils across the Australian continent for any point in time in the Landsat archive since 1987. Learn more: [DEA Fractional Cover](/data/category/dea-fractional-cover/).

<span id="gain"></span>

## Gain

A general term used to denote an increase in signal power in transmission from one point to another, usually expressed 
in decibels. It can also be used to represent the multiplier used to transform satellite image digital numbers to 
measures of at-sensor radiance.

<span id="ga"></span>

## Geoscience Australia (GA)

Geoscience Australia is the national public-sector geoscience organisation. It is the government’s technical advisor 
on all aspects of geoscience and is the custodian of geographic and geological data.
[Digital Earth Australia](#dea) is a program of Geoscience Australia. Learn more:
[Geoscience Australia](https://www.ga.gov.au/).

<span id="geomedian"></span>

## Geomedian

Geometric median is a robust high-dimensional statistic that maintains relationships between spectral bands, while 
producing a multidimensional median over a timeseries of satellite images. The Geometric Median provides information on the general conditions of a landscape over a timeseries. Learn more: [DEA Geometric Median and Median Absolute Deviation (Landsat)](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/).

<span id="gee"></span>

## Google Earth Engine (GEE)

A Google-based platform for analysis and visualisation of geospatial datasets.

<span id="gis"></span>

## Geographic Information System (GIS)

A system that manages and visualises spatially referenced data.

<span id="hltc"></span>

## High and Low Tide Imagery (HLTC)

Previously called High and Low Tide Composites. DEA High and Low Tide Imagery is a Digital Earth Australia product 
providing cloud-free imagery mosaics of Australia's coast, estuaries and reefs at low and high tide. Learn more: [DEA High and Low Tide Imagery (Landsat)](/data/product/dea-high-and-low-tide-imagery-landsat/).

<span id="hpc"></span>

## High Performance Computing (HPC)

The practice of aggregating computing power in a way that delivers much higher performance than one could get out of 
a typical desktop computer or workstation in order to solve large problems in science, engineering, or business.

<span id="incident-angle"></span>

## Incident angle (degrees)

The angle between a ray incident on a surface and the line perpendicular to the surface at the point of incidence.

<span id="interim"></span>

## Interim

A stage in DEA's dataset maturity lifecycle. Interim production means that one or more [ancillary](#ancillary) datasets were not 
available at the time of production, and the dataset has instead been corrected using a combination of [NRT](#nrt) 
climatological ancillaries, and [final](#final) observed ancillaries. Learn more:
[DEA dataset maturity](/guides/reference/dataset_maturity_guide#interim).

<span id="nidem"></span>

## Intertidal Elevation

Previously called National Intertidal Digital Elevation Model (NIDEM). A DEA product derived from DEA Intertidal 
Extents that maps the elevation of the Australian intertidal zone relative to Mean Sea Level. Learn more: [DEA Intertidal](/data/product/dea-intertidal/).

<span id="item"></span>

## Intertidal Extents

Previously called Intertidal Extents Model (ITEM). DEA Intertidal Extents is a DEA product that maps the relative 
extent of the Australian intertidal zone at regular intervals of the observed tidal range. Learn more: [DEA Intertidal Extents (Landsat)](/data/product/dea-intertidal-extents-landsat/).

<span id="indexing"></span>

## Indexing

The process of registering a dataset with associated metadata (in a folder or at a URI) to an Open Data Cube
instance so that it is searchable and accessible through the datacube API.

<span id="jupyter-nb"></span>

## Jupyter Notebook

A document format (with .ipynb file extension) that contains live code that can be used to analyse data, display charts, and more. Learn more: [Introduction to Jupyter notebooks](/notebooks/Beginners_guide/01_Jupyter_notebooks/).

<span id="jupyter-lab"></span>

## JupyterLab

An interactive web-based user interface for editing and running Jupyter Notebooks. JupyterLab is used as an analysis 
environment on both the [DEA Sandbox](#dea-sandbox) and the NCI's [ARE](#are).

<span id="landsat"></span>

## Landsat

A joint [NASA](#nasa)/[USGS](#usgs) program of medium resolution satellites that have been collecting publicly 
available Earth observation data continuously since 1972. Learn more: [Landsat Science](https://landsat.gsfc.nasa.gov/).

<span id="lccs"></span>

## Land Cover Classification Scheme (LCCS)

The Land Cover Classification Scheme was developed by the United Nations Food and Agriculture Organization to provide 
a consistent framework for the classification and mapping of land cover. Learn more: [LCCS](https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/category/details/en/c/1036361/).
  
<span id="mad}"></span>

## Median Absolute Deviation (MAD)

Median Absolute Deviation, used as a form of standard deviation for the geomedians. The Median Absolute Deviation provides information on how a landscape is changing over a timeseries. Learn more: [MAD](https://doi.org/10.1109/IGARSS.2018.8518312).

<span id="modis"></span>

## Moderate Resolution Imaging Spectroradiometer (MODIS)

A sensor aboard NASA’s Terra and Aqua satellites. MODIS instruments view the entire Earth’s surface every 1-2 days, 
acquiring data in 36 spectral bands. It plays a vital role in the development of validated, global, interactive 
Earth system models which aim to accurately predict global change. Learn more:
[NASA: MODIS](https://modis.gsfc.nasa.gov/about/).

<span id="msi"></span>

## MultiSpectral Instrument (MSI)

The MSI is carried on the Sentinel-2 satellites. Light reflected up to the MSI instrument from the Earth and its 
atmosphere is collected by a three-mirror (M1, M2 and M3) telescope and 
focused, via a beam-splitter, onto two Focal Plane Assemblies: one for the ten very-near infrared wavelengths and one 
for the three shortwave infrared wavelengths. Learn more:
[ESA missions - Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2).

<span id="mss"></span>

## Multispectral Scanner (MSS)

A line-scanning instrument carried by Landsat satellites that continually scans the Earth in a 185 km swath and 
collects data over a variety of wavelengths. Learn more:
[Landsat: Multispectral Scanner](https://landsat.gsfc.nasa.gov/multispectral-scanner/).

<span id="nadir"></span>

## Nadir

The point of the celestial sphere that is vertically downward from the observer and directly opposite the 
[zenith](#zenith).

<span id="nbar"></span>

## Nadir-corrected BRDF Adjusted Reflectance (NBAR)

Surface reflectance data that has been corrected to remove the effects of topography and angular variation using 
bidirectional reflectance modelling ([BRDF](#brdf)).

<span id="nbart"></span>

## Nadir-corrected BRDF Adjusted Reflectance with Terrain illumination correction (NBART)

Surface reflectance data that has been corrected to remove the effects of topography and angular variation using 
bidirectional reflectance modelling ([BRDF](#brdf)), as well as corrected for the effects of terrain shadow.

<span id="nasa"></span>

## National Aeronautics and Space Administration (NASA)

The United States of America's federal government's civil space, aeronautics and space research agency.

<span id="nci"></span>

## National Computational Infrastructure (NCI)

A national facility that provides world-class, high-end computing services to Australian researchers, including those 
working in the data-intensive areas of climate and Earth system science. Learn more:
[National Computational Infrastructure](https://www.nci.org.au/).

<span id="noaa"></span>

## National Oceanic and Atmospheric Administration (NOAA)

A scientific agency within the United States Department of Commerce that focuses on the conditions of the oceans, 
major waterways and atmosphere. Learn more: [NOAA](https://www.noaa.gov/).

<span id="nbr"></span>

## Normalised Burn Ratio (NBR)

Calculated from near-infrared ([NIR](#nir)) and short wave infrared ([SWIR](#swir)).

<span id="ndvi}"></span>

## Normalised Difference Vegetation Index (NDVI)

Calculated from visible and near-infrared ([NIR](#nir)) light reflected by vegetation.

<span id="nir"></span>

## Near Infrared (NIR)

Radiation just beyond the visible light spectrum. In Landsat and Sentinel 2 Earth observation satellites, it refers to 
radiation in the range of 0.7 to 0.9 micrometers.

<span id="nrt"></span>

## Near real-time (NRT)

A stage in DEA's dataset maturity lifecycle. NRT data is a less refined/calibrated dataset, which is available much 
sooner after satellite acquisition than standard [ARD](#ard) data. Learn more:
[DEA dataset maturity](/guides/reference/dataset_maturity_guide#nrt).

<span id="odc"></span>

## Open Data Cube (ODC)

An open source geospatial data management and analysis software project. It is a global initiative to increase the 
value and use of satellite data by providing users with access to free and open data management technologies and 
analysis platforms. At its core, ODC is a set of Python libraries and a [PostgreSQL](#postgresql) database that allows you to work with 
geospatial raster data. Learn more: [Open Data Cube](https://www.opendatacube.org).

<span id="oli"></span>

## Operational Land Imager (OLI)

The Operational Land Imager is carried by the Landsat 8 satellite. It measures in the visible, near infrared 
[NIR](#nir), and short wave infrared [SWIR](#swir) portions of the spectrum. Its images have 15-meter (49 ft.) 
[panchromatic](#panchromatic) and 30-meter multi-spectral spatial resolutions along a 185 km (115 miles) wide swath.
Learn more: [Landsat 8](https://landsat.gsfc.nasa.gov/satellites/landsat-8/).

<span id="oli2"></span>

## Operational Land Imager 2 (OLI2)

The OLI-2 instrument is carried by the Landsat 9 satellite. It provides visible and near infrared / shortwave infrared 
(VNIR/[SWIR](#swir)) imagery consistent with previous Landsat spectral, spatial, radiometric and geometric qualities.
The OLI-2 instrument includes an optical telescope, Focal Plane Array / Focal Plane Electronics, calibration hardware, 
and instrument support electronics. OLI-2 provides data for nine spectral bands with a maximum ground sampling distance 
(GSD), both in-track and cross track, of 30 m (98 ft) for all bands except the panchromatic band, which has a 15 m 
(49 ft) GSD. Learn more:
[Landsat 9 instruments](https://landsat.gsfc.nasa.gov/satellites/landsat-9/landsat-9-instruments/).

<span id="panchromatic"></span>

## Panchromatic band

A band that measures a wide range of light at high resolution, compared to standard multispectral bands that measure a 
narrow range of light at lower resolution. On Landsat 7, 8, and 9, the panchromatic band can be used to "sharpen" 30 
metre visible bands to higher 15 metre resolution. Learn more:
[Pansharpening Landsat](/notebooks/How_to_guides/Pansharpening/).

<span id="pixel"></span>

## Pixel

The minimum size area on the ground detectable by a remote sensing device. The size varies depending on the type of sensor.

<span id="pq"></span>

## Pixel quality (PQ)

A categorical assessment of the quality of an observation at the pixel level.

<span id="polar-orbit"></span>

## Polar orbit

An orbit with an orbital inclination of near 90 degrees where the satellite ground track will cross both polar regions 
once during each orbit. The term describes the near-polar orbits of a spacecraft.

<span id="postgresql"></span>

## PostgreSQL

Also known as Postgres, it is an open source object-relational database management system with an emphasis on 
extensibility and standards compliance. It is a high performance database engine used as both a relational and document 
database by the [Open Data Cube](#odc).

<span id="process"></span>

## Process

The generation of some form of output as the result of a set of actions, which may include sub-processes.

<span id="product"></span>

## Product

A categorical term applied to describe the output from a process. Typically, a product has an associated product 
definition which contains the product description and specification. An example of a product is
[DEA Water Observations (Landsat)](/data/product/dea-water-observations-landsat/)

<span id="python"></span>

## Python

The programming language used to develop the [Open Data Cube](#odc) and most of [Digital Earth Australia](#dea). 
It is an easy-to-use language, which also provides simple access to high performance processing capabilities.
Learn more: [Python](https://www.python.org/).

<span id="radiance"></span>

## Radiance

The amount of light directly detected by remote sensing instruments.

<span id="radiometer"></span>

## Radiometer

A device that detects and measures electromagnetic radiation.

<span id="radiometric"></span>

## Radiometric

Relating to, using, or measured by a [radiometer](#radiometer). The measurement of radiation.

<span id="raster"></span>

## Raster data

An abstraction of the real world where spatial data is expressed as a matrix of cells or [pixels](#pixel), with spatial 
position implicit in the ordering of the pixels. With the raster data model, spatial data is not continuous but divided 
into discrete units. This makes raster data particularly suitable for certain types of spatial operations 
(e.g. overlays or area calculations). Unlike [vector data](#vector), there are no implicit topological relationships.

<span id="raw-data"></span>

## Raw data

Numerical values representing the direct observations output by a measuring instrument. The values are transmitted as 
a bit stream in the order they were obtained.

<span id="real-time"></span>

## Real time

The time in which reporting on events or recording of events is simultaneous with the events. For example, the real 
time of a satellite is the time in which it simultaneously reports its environment as it encounters it.

<span id="reflectance"></span>

## Reflectance

The measure of the proportion of light or other radiation striking a surface which is reflected off it.

<span id="relative-azimuth"></span>

## Relative azimuth (degrees)

The relative [azimuth](#azimuth) angle between the sun and view directions.

<span id="relative-slope"></span>

## Relative slope (degrees)

The relative [azimuth](#azimuth) angle between the incident and exiting directions in the slope geometry.

<span id="remote-sensing"></span>

## Remote sensing

The measurement or acquisition of information about some property of an object or phenomenon, by a recording device 
that is not in physical or intimate contact with the object or phenomenon under study.

<span id="resampling"></span>

## Resampling

Modifying the geometry of an image, which may be from either a remotely sensed or map data source. This process 
usually involves rectification and/or registration.

<span id="resolution"></span>

## Resolution

A measure of the amount of detail that can be seen in an image; i.e. the size of the smallest object recognisable using
the detector. In remotely sensed imagery, resolution is significant in four measurement dimensions: spectral, spatial,
radiometric and temporal.

<span id="satellite-azimuth"></span>

## Satellite azimuth (degrees)

The angle of the satellite’s position from true north; i.e. the angle between true north and a vertical circle passing 
through the satellite and the point being imaged on Earth.

<span id="satellite-zenith"></span>

## Satellite view or satellite zenith (degrees)

The angle between the zenith and the satellite.

<span id="saturation"></span>

## Saturation

The intensity of a colour. A highly saturated colour is vivid and brilliant. To dull a colour and decrease its 
saturation, add small amounts of its complement, making it closer to grey.

<span id="scene"></span>

## Scene

Each satellite data [swath](#swath) can be divided into a series of scenes to enable the data to be handled and catalogued more easily.
A scene is a defined portion of the continuous strips of data collected by satellites.
Scenes are primarily used for LANDSAT satellite data.

<span id="ssh"></span>

## Secure Shell (SSH)

SSH is a technology that enables accessing remote computers using a text based terminal interface. It comes build in 
with Linux, but requires additional software to use it from Windows computers.

<span id="sentinel"></span>

## Sentinel

A program of satellites from Europe that collect publicly available Earth observation data. Each satellite has a 
different purpose or capability, and together, they address six thematic areas: land, marine, atmosphere, climate 
change, emergency management and security. Learn more:
[Copernicus: Discover our satellites](https://www.copernicus.eu/en/about-copernicus/infrastructure-overview/discover-our-satellites).

<span id="swir"></span>

## Short-Wave Infrared (SWIR)

Radiation beyond the visible light spectrum. In Landsat and Sentinel 2 Earth observation satellites, it refers to 
radiation in the range of 1.5 to 2.4 micrometers.

<span id="solar-azimuth"></span>

## Solar azimuth (degrees)

The angle of the sun’s position from true north; i.e. the angle between true north and a vertical circle passing 
through the sun and the point being imaged on Earth.

<span id="solar-irradiance"></span>

## Solar irradiance

The solar irradiance is the output of light energy from the entire disk of the Sun, measured at the Earth.

<span id="solar-zenith"></span>

## Solar zenith (degrees)

The angle between the [zenith](#zenith) and the centre of the sun’s disc.

<span id="solar-zenith-angle"></span>

## Solar Zenith Angle (SZA)

The angle between the local [zenith](#zenith) (i.e. directly above the point on the ground) and the line of sight from 
that point to the sun.

<span id="spatial-res"></span>

## Spatial resolution

The area on the ground that an imaging system, such as a satellite sensor, can distinguish. Also see [resolution](#resolution).

<span id="spectral-response"></span>

## Spectral response

The ratio of the relative amplitude of the response of a detector and the frequency of incident electromagnetic radiation.

<span id="spectrometer"></span>

## Spectrometer

An optical instrument that splits the light received from an object into its component wavelengths by means of a 
diffraction grating, and then measures the amplitudes of the individual wavelengths.

<span id="stacking"></span>

## Stacking

A process that combines all data for a [tile](#tile) across a specific time range into a single file. 

<span id="sun-sync-orbit"></span>

## Sun-synchronous orbit

An orbit in which a satellite is always in the same position with respect to the rotating Earth at the same time of day.

<span id="surface-reflectance"></span>

## Surface reflectance

The fraction of incoming solar radiation that is reflected from Earth's surface for specific incident or viewing 
cases (directional, conical, and hemispherical cases).

<span id="swath"></span>

## Swath

As a satellite moves around the Earth, it observes a long strip of the Earth's surface called a swath. Each swath is divided into a series of [scenes](#scene).

<span id="sar"></span>

## Synthetic Aperture Radar (SAR)

An imaging radar mounted on an instant moving platform. The signal is responsive to surface characteristics like 
structure and moisture. Learn more:
[NASA - What is Synthetic Aperture Radar?](https://www.earthdata.nasa.gov/learn/backgrounders/what-is-sar).

<span id="telemetry"></span>

## Telemetry

The science and technology of automatic measurement and transmission of data by wire, radio or other means from 
remote sources (e.g. space vehicles) to receiving stations for recording and analysis.

<span id="tm"></span>

## Thematic Mapper (TM)

An advanced, multispectral-scanning, Earth resources sensor featured on Landsat 4 and 5. TM is designed to acquire 
data to categorise the Earth's surface and is particularly useful for agricultural applications and identification of 
land use. It continuously scans the surface of the Earth, simultaneously acquiring data in seven spectral channels.
Learn more: [NASA Thematic Mapper Plus](https://landsat.gsfc.nasa.gov/thematic-mapper/).

<span id="thredds"></span>

## Thematic Real-time Environmental Distributed Data Services (THREDDS)

A National Computational Infrastructure ([NCI](#nci)) server, which is a high-performance and high-availability 
installation of Unidata's Thematic Real-time Environmental Distributed Data Services (THREDDS).
THREDDS serves many of NCI’s open data collections at the file level, as well as some aggregations. It provides many 
different types of services to allow individual files to be selected, as well as more advanced services such as OpenDAP, 
NetCDF subsetting, OGC WCS and WMS. Learn more: [NCI: Data ](https://nci.org.au/our-services/data-services).

<span id="tile"></span>

## Tile

Tiles are a way of dividing data products into smaller pieces to enable the data to be handled and analysed more easily. 
Each tile represents a specific geographic area and multiple tiles can be combined into a grid to cover larger regions.
For instance, the [DEA GeoMAD](https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) product is provided using 96 &times; 96 km grid tiles, characteristic of DEA Summary Products.

<span id="timedelta"></span>

## Timedelta (seconds)

The time in seconds from satellite apogee (the point of orbit at which the satellite is furthest from the Earth).

<span id="usgs"></span>

## United States Geological Survey (USGS)

A scientific agency of the United States government. The scientists of the USGS study the landscape of the United 
States, its natural resources, and the natural hazards that threaten it. The USGS and [NASA](#nasa) jointly run the 
Landsat program of earth observation satellites. Learn more: [USGS](https://www.usgs.gov/).

<span id="vector"></span>

## Vector data

Vector data, when used in the context of spatial or map information, refers to a format where all map data is stored as 
points, lines, and areas rather than as an image or continuous tone picture. These vector data have location and 
attribute information associated with them.

<span id="vdi"></span>

## Virtual Desktop Infrastructure (VDI)

The Virtual Desktop Infrastructure was a service offered by the [NCI](#nci) that provided a linux desktop environment 
for scientific computing. It has been replaced by [ARE](#are).

<span id="viirs"></span>

## Visible Infrared Imaging Radiometer Suite (VIIRS)

The Visible Infrared Imaging Radiometer Suite (VIIRS) is one of the key instruments onboard the NOAA-20 spacecraft, as 
well as the Suomi-NPP satellite. It collects visible and infrared imagery and global observations of land, atmosphere, 
cryosphere and oceans. Learn more:
[Joint Polar Satellite System](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system).

<span id="wofl"></span>

## Water Observation Feature Layer (WOFL)

A [WO](#wo) observation for one point in time

<span id="wo"></span>

## Water Observations (WO)

Previously called Water Observations from Space. A Digital Earth Australia product that classifies satellite pixels 
into 'wet', 'dry', or 'invalid' (e.g. cloudy or a poor quality observation). Learn more:
[DEA Water Observations](/data/category/dea-water-observations/).

<span id="wavelength"></span>

## Wavelength

The distance from crest to crest, or trough to trough, of an electromagnetic or other wave. The longer the wavelength, 
the lower the frequency.

<span id="wms"></span>

## Web Map Service (WMS)

A HTTP interface for requesting geo-registered map images that can be displayed in a browser application or 
[GIS](#gis) software system.

<span id="wfs"></span>

## Web Feature Service (WFS)

An interface for querying, modifying and exchanging features or values in a database and retrieving features for use.

<span id="wrs"></span>

## Worldwide Reference System (WRS)

Landsat scenes are arranged into a worldwide grid called the World Reference System which uses 'path' and 'row'
numbers to identify the location of each scene. It is a global indexing scheme based on nominal scene centres.
Learn more:
[Worldwide Reference System from NASA](https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/).

<span id="xarray"></span>

## Xarray

An open source project and [Python](#python) package (`xarray`) for working with labelled multidimensional arrays such as those 
returned by the [Open Data Cube](#odc).

<span id="yaml"></span>

## YAML

A human-readable data storage format (with .yaml file extension). It is used throughout [DEA](#dea) for metadata files, product definitions and 
other configuration files.

<span id="zenith"></span>

## Zenith

The point on the celestial sphere directly above the observer, and directly opposite to [nadir](#nadir).
