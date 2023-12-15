## Background

The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies. In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time. We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time. Unfortunately, products with such corrections are generally not immediately suitable for applications over persistent water bodies. Aquatic based applications such as water quality and benthic cover, require additional corrections that are not included in the standard DEA Surface Reflectance (Landsat 8 OLI-TIRS) product.

## What this product offers

This product takes Landsat 8 imagery captured over the Australian continent and is atmospherically corrected in the same manner as the DEA Surface Reflectance (Landsat 8 OLI-TIRS) product, without the BRDF and terrain illumination effects. Instead, water bodies are corrected for atmospheric adjacency and regional sky radiation effects. Removal for sun glint effects is being investigated for suitability in broadly applying a single methodology, or leave it up to the user to apply their methodology of choice. The result is accurate and can be combined with the DEA Surface Reflectance (Landsat 8 OLI-TIRS) product for time series analysis and generation of mosaics. The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

% ## Data description

## Applications

\* The development of derivative products to monitor inland waterways and coastal features, such as:

  \* coastal habitats

  \* water quality

  \* benthic cover

  \* sediment transport

  \* erosion

  \* shallow water bathymetry

\* The development of refined information products, such as: {TODO; populate with aquatic related items areal units of detected surface water areal units of deforestation yield predictions of agricultural parcels}

\* The development of management practices such as:

  \* Compliance surveys

  \* Emergency management of water ways, water courses, town supply

## Technical information

\#### Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS)

OLI is a push-broom sensor with a four-mirror telescope and 12-bit quantisation. OLI collects data for visible, near infrared, and short wave infrared spectral bands as well as a panchromatic band.

TIRS measures land surface temperature in two thermal bands with new technology that applies quantum physics to detect heat.

\#### The Analysis Ready Data concept

The Analysis Ready Data (ARD) package allows you to get up and running with your analysis as quickly as possible with minimal data preparation and additional input. This makes it simpler for you to develop applications and for the database to execute queries.

The satellite data has been processed to a minimum set of requirements and organised into a form that allows immediate analysis and interoperability through time and with other datasets. It has been adapted from CEOS Analysis Ready Data (\[CARD4L\](http://ceos.org/ard/)).

The Aquatic Analysis Ready Data concept is an enhancement to the standard ARD concept and specific to aquatic-based applications, where the surface reflectance algorithm is adjusted to correct for atmospheric adjacency effects.  Additional corrections such as sun and sky glint are still being considered and evaluated.

\#### ARD sub-products

1) Aquatic Surface Reflectance 3 (\_Landsat 8 OLI-TIRS)\_

This sub-product produces optical surface reflectance data which includes robust physical models which correct for variations and inconsistencies in image radiance values.  Corrections include sky glint, and atmospheric adjacency (Sun-Glint no go at this stage).  A water detection method is used to set non-water pixels to null (-999).

2) Aquatic Surface Reflectance OA 3 (\_Landsat 8 OLI-TIRS)\_

The Aquatic SR sibling product depends upon the OA product to provide accurate and reliable contextual information about the Landsat data. This ‘data provenance’ provides a chain of information which allows the data to be replicated or utilised by derivative applications. It takes a number of different forms, including satellite, solar and surface geometry and classification attribution labels.

## Lineage

This product is derived from the USGS Landsat Collection 1 archive.

\* The ozone data was provided by Environment Canada.  See \[Environment Canada: Global Ozone Maps\](https://exp-studies.tor.ec.gc.ca/e/ozone/Curr\_allmap\_g.htm)

\* The Aerosol Optical Thickness data was provided by the Commonwealth Scientific and Industrial Research Organisation (CSIRO).  See \[Qin et al. (2015)\](https://doi.org/10.1109/TGRS.2015.2433911)

\* The Precipitable Water for Entire Atmosphere data was provided by the National Oceanic and Atmospheric Administration (NOAA) / Earth System Research Laboratory (ESRL) / Physical Sciences Division (PSD). See \[Kalnay et al. (1996)\](https://doi.org/10.1175/1520-0477(1996)077%3c0437:tnyrp%3e2.0.co;2)

\* The baseline Digital Surface Model (DSM) data produced from the Shuttle Radar Topography Mission (SRTM) was provided by the National Geospatial-Intelligence Agency (NGA).  See \[NGA: SRTM\](https://www.nga.mil/About/History/NGAinHistory/Pages/SRTM.aspx), \[NASA: SRTM\](https://www2.jpl.nasa.gov/srtm/index.html)

\* Level 1 Collection 1 data was provided by the United States Geological Survey (USGS)'s Earth Resources Observation and Science (EROS) Center. See \[USGS: EROS\](https://www.usgs.gov/centers/eros), \[USGS: Landsat Collection 1\](https://www.usgs.gov/land-resources/nli/landsat/landsat-collection-1?qt-science\_support\_page\_related\_con=1#qt-science\_support\_page\_related\_con)

\* Point Spread Function (Developed by Spectral Sciences)

## Processing steps

1. Longitude and Latitude Calculation

1. Satellite and Solar Geometry Calculation

1. Aerosol Optical Thickness Retrieval

1. Ozone Retrieval

1. MODTRAN

1. Derivation of the Point Spread Function

1. Atmospheric Correction Coefficients Calculation

1. Bilinear Interpolation of Atmospheric Correction Coefficients

1. Atmospheric Adjacency Correction

1. MNDWI

1. Sky Glint Correction

% ## Software

% ## References

