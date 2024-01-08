# How to access data on the CMI

Our data products can be accessed through various web services, catalogues and mapping services.

:::{contents} In this guide
:local:
:backlinks: none
:::

## Catalogues and web services

### AWS S3

**What it is**

DEA hosts data on Amazon Web Service (AWS)'s Simple Storage Service (S3) to facilitate direct data access. Most of the data that is stored on S3 is Cloud Optimised GeoTIFFs, which can be accessed directly without downloading the files.

**How to use it**

You can access the S3 bucket directly at `s3://dea-public-data` or browse files through a web interface at [Digital Earth Australia - Public Data](https://data.dea.ga.gov.au/).

**More information**

[AWS S3 documentation](https://docs.aws.amazon.com/s3/index.html)

### DEA Access (coming soon)

**What it is**

DEA Access serves an online spatial catalogue of priority Geoscience Australia data collections that are hosted at the NCI. This is a complementary service to THREDDS, providing open WebMap access to DEA datasets.

The DEA Access portal offers search and discovery tools to make it simple and easy to access the DEA collections that are hosted on the NCI file servers. Most importantly, this allows the user community to download DEA base data and derivative products for specialised processing and further analysis.

### Geoscience Australia eCat

**What it is**

eCat, or the Data and Publications Search, is Geoscience Australia's organisation-wide metadata catalogue, which sits parallel to the CMI. It contains records for various types of products, including data products, services, portals, documents, software, maps and models. eCat is also Geoscience Australia's Intellectual Property register.

Some data products have downloadable files contained on the eCat record, as listed under 'Download and Links'.

All eCat records are available to the general public free of charge.

**How to use it**

Every data product on the CMI links to its eCat record. Click on the link and it will take you to the eCat record.

**More information**

[eCat home page](https://ecat.ga.gov.au/geonetwork/)

### GSKY

**What it is**

GSKY is an open web service that accesses and analyses the big geospatial data on NCI's cloud and high-performance computing systems, and then delivers it to a user device or website.

For example, hundreds of time series and geospatially overlapping data can be seamlessly merged together, allowing researchers to focus on the information rather than dealing with data files.

Furthermore, using GSKY's processing capability, that data can be analysed on the fly using user-provided algorithms to extract new information over both space and time.

**How to use it**

See [GSKY: Getting started.](https://opus.nci.org.au/display/Help/Getting+Started)

**More information**

[About GSKY](https://nci.org.au/our-services/data-services#GSKY)

[GSKY User Guide](https://opus.nci.org.au/display/Help/GSKY+User+Guide)

### Open Data Cube

**What it is**

The Open Data Cube (ODC) is an open source solution for accessing, managing, and analyzing large quantities of Geographic Information System (GIS) data - namely Earth observation data. It is a global initiative to increase the value and use of satellite data by providing users with access to free and open data management technologies and analysis platforms.

At its core, ODC is a set of Python libraries and a PostgreSQL database that allows you to work with geospatial raster data.  

**How to use it**

See [Open Data Cube Sandbox introduction](https://www.opendatacube.org/sandbox)

**More information**

[Open Data Cube](https://www.opendatacube.org/)

### THREDDS

**What it is**

The THREDDS server is the National Computational Infrastructure (NCI)'s high-performance and high-availability installation of Unidata's Thematic Real-time Environmental Distributed Data Services (THREDDS).

THREDDS serves many of NCI's open data collections at the file level, as well as some aggregations. It provides many different types of services to allow individual files to be selected, as well as more advanced services such as OpenDAP, NetCDF subsetting, OGC WCS and WMS.

The THREDDS server is programmatically accessible, which is how many advanced tools and portals use the service.

**How to use it**

If the data product features a THREDDS link, you can access the data in the following way:

1) Open [DEA Explorer](https://explorer.dea.ga.gov.au/). Select the product of interest from the menu at the top. This will give you a tile map. The data in THREDDS is indexed according to this tile map.

2) Once you have located the tile that covers your region of interest, note the path and row numbers.

3) Open the THREDDS link for the data product.

4) The folders follow the sequence: product > path > row > year > month > day. Open each folder corresponding to the product, tile and date of interest.

**More information**

[About THREDDS](https://nci.org.au/our-services/data-services)

## Maps

### AusSeabed Marine Data Portal

**What it is**

The AusSeaBed Portal provides access to publicly available acoustic datasets such as bathymetry, backscatter, side scan sonar data and other marine-related products. It also provides a suite of analytical assessment tools to maximise the value of the data.

This interface allows users to explore seafloor mapping products across Australia's marine jurisdiction prior to downloading.

**How to use it**

Visit the [AusSeabed Portal](https://portal.ga.gov.au/persona/marine) and select 'About'.

**More information**

[AusSeabed](http://www.ausseabed.gov.au/)

### DEA Maps

**What it is**

Digital Earth Australia (DEA) Maps is a website for map-based access to DEA's products. It was developed by Data61 CSIRO for Geoscience Australia.

DEA uses satellite data to detect physical changes across Australia in unprecedented detail. It identifies soil and coastal erosion, crop growth, water quality and changes to cities and regions.

DEA Maps aims to provide easy access to DEA's products to help users to make more informed decisions.

**How to use it**

To launch DEA Map and display basic data:

-   Visit [DEA Maps](https://maps.dea.ga.gov.au/).

-   On the left-hand panel, click 'Add data' to launch the data catalogue.

-   Browse through the data catalogue to find a data set of interest.

-   Click on the title of your preferred dataset to get a preview of that data, along with a description.

-   To view your selected data set on the map, click 'Add to the Map'.\
    The spatial data will be immediately displayed in the map view, and a visual legend for that data will appear in the Data Workbench, located on the left.

**More information**

[Example: Fractional Cover on DEA Maps](https://maps.dea.ga.gov.au/#share=s-uCPjd1cM8bOxwNYFVeOeswPQmkd)

[DEA Maps - Help and FAQ](https://maps.dea.ga.gov.au/help/help.html)
