## Background

The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies. In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time. We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time. Unfortunately, products with such corrections are generally not immediately suitable for applications over persistent water bodies. Aquatic based applications such as water quality and benthic cover, require additional corrections that are not included in the standard DEA Surface Reflectance (Landsat 8 OLI-TIRS) product.

## What this product offers

This product takes Landsat 8 imagery captured over the Australian continent and is atmospherically corrected in the same manner as the DEA Surface Reflectance (Landsat 8 OLI-TIRS) product, without the BRDF and terrain illumination effects. Instead, water bodies are corrected for atmospheric adjacency and regional sky radiation effects. Removal for sun glint effects is being investigated for suitability in broadly applying a single methodology, or leave it up to the user to apply their methodology of choice. The result is accurate and can be combined with the DEA Surface Reflectance (Landsat 8 OLI-TIRS) product for time series analysis and generation of mosaics. The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

% ## Data description

## Applications
* 
* The development of derivative products to monitor inland waterways and coastal features, such as:
* coastal habitats
* water quality
* benthic cover
* sediment transport
* erosion
* shallow water bathymetry
* The development of refined information products, such as: {TODO; populate with aquatic related items areal units of detected surface water areal units of deforestation yield predictions of agricultural parcels}
* The development of management practices such as:
* Compliance surveys
* Emergency management of water ways, water courses, town supply

## Technical information

### Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS)

OLI is a push-broom sensor with a four-mirror telescope and 12-bit quantisation. OLI collects data for visible, near infrared, and short wave infrared spectral bands as well as a panchromatic band.

TIRS measures land surface temperature in two thermal bands with new technology that applies quantum physics to detect heat.

### The Analysis Ready Data concept

The Analysis Ready Data (ARD) package allows you to get up and running with your analysis as quickly as possible with minimal data preparation and additional input. This makes it simpler for you to develop applications and for the database to execute queries.

The satellite data has been processed to a minimum set of requirements and organised into a form that allows immediate analysis and interoperability through time and with other datasets. It has been adapted from CEOS Analysis Ready Data (\[CARD4L\](http://ceos.org/ard/)).

The Aquatic Analysis Ready Data concept is an enhancement to the standard ARD concept and specific to aquatic-based applications, where the surface reflectance algorithm is adjusted to correct for atmospheric adjacency effects.  Additional corrections such as sun and sky glint are still being considered and evaluated.

### ARD sub-products

1) Aquatic Surface Reflectance 3 (\_Landsat 8 OLI-TIRS)\_

This sub-product produces optical surface reflectance data which includes robust physical models which correct for variations and inconsistencies in image radiance values.  Corrections include sky glint, and atmospheric adjacency (Sun-Glint no go at this stage).  A water detection method is used to set non-water pixels to null (-999).

2) Aquatic Surface Reflectance OA 3 (\_Landsat 8 OLI-TIRS)\_

The Aquatic SR sibling product depends upon the OA product to provide accurate and reliable contextual information about the Landsat data. This ‘data provenance’ provides a chain of information which allows the data to be replicated or utilised by derivative applications. It takes a number of different forms, including satellite, solar and surface geometry and classification attribution labels.

## Lineage

This product is derived from the USGS Landsat Collection 1 archive.
* The ozone data was provided by Environment Canada.  See \[Environment Canada: Global Ozone Maps\](https://exp-studies.tor.ec.gc.ca/e/ozone/Curr\_allmap\_g.htm)
* The Aerosol Optical Thickness data was provided by the Commonwealth Scientific and Industrial Research Organisation (CSIRO).  See \[Qin et al. (2015)\](https://doi.org/10.1109/TGRS.2015.2433911)
* The Precipitable Water for Entire Atmosphere data was provided by the National Oceanic and Atmospheric Administration (NOAA) / Earth System Research Laboratory (ESRL) / Physical Sciences Division (PSD). See \[Kalnay et al. (1996)\](https://doi.org/10.1175/1520-0477(1996)077%3c0437:tnyrp%3e2.0.co;2)
* The baseline Digital Surface Model (DSM) data produced from the Shuttle Radar Topography Mission (SRTM) was provided by the National Geospatial-Intelligence Agency (NGA).  See \[NGA: SRTM\](https://www.nga.mil/About/History/NGAinHistory/Pages/SRTM.aspx), \[NASA: SRTM\](https://www2.jpl.nasa.gov/srtm/index.html)
* Level 1 Collection 1 data was provided by the United States Geological Survey (USGS)'s Earth Resources Observation and Science (EROS) Center. See \[USGS: EROS\](https://www.usgs.gov/centers/eros), \[USGS: Landsat Collection 1\](https://www.usgs.gov/land-resources/nli/landsat/landsat-collection-1?qt-science\_support\_page\_related\_con=1#qt-science\_support\_page\_related\_con)
* Point Spread Function (Developed by Spectral Sciences)

## Processing steps

1. Longitude and Latitude Calculation
For a given acquisition's spatial extent and pixel resolution, create full dimension arrays/images whose pixel/cell contents contain the longitude and latitude values based on the WGS84 datum. 

The values at each pixel represent either the longitude or latitude for the upper left-hand corner of the pixel. The Coordinate Reference System (CRS) of the spatial extent isn't required to be in Geographics WGS84, nor do the units of the pixel resolution required to be in decimal degrees. 

The algorithm outputs spatial grids in the native CRS and pixel resolution, just the array/image contents at the pixel level contain either a longitude or latitude value. 

2. Satellite and Solar Geometry Calculation

3. Aerosol Optical Thickness Retrieval
For a given acquisition, retrieve the aerosol optical thickness estimate for input into the radiative transfer evaluation. 

The supplied aerosol optical thickness data is a geospatially sparse point cloud and only exists for the years 2002 to 2008, supplemented by monthly composites. 

Essentially the spatial extent of the acquisition in longitude and latitude for the WGS84 datum is intersected with the geospatial extent of the aerosol data, and a mean value extracted. 

If the year of acquisition falls within 2002-2008, then select the points that have a timestamp of within 0.5 days of the acquisition, and fall within the geospatial intersection area of interest. If no data are found, fallback to a monthly aggregate for that year. If this also fails, then fall back to an all-time monthly aggregate. If this also fails then return a nominal value of 0.06. 

4. Ozone Retrieval
Retrieval of ozone data for the acquisition of interest at a given (longitude, latitude) location for a given month. 

The ozone data consists of 12 global datasets, 1 for each month of the year. The month that the acquisition was taken in, is used as a basis for selecting the appropriate month containing the relevant ozone data. 

As the source ozone data is of a very low resolution, the acquisition's central coordinate in longitude and latitude degrees, based on the WGS84 datum, is used as a sole point to retrieve an ozone value to be used as a value for the entire acquisition's spatial extent. 

5. MODTRAN

6. Derivation of the Point Spread Function
The Point Spread Function is derived for each spectral band using the latest MODTRAN software developed by Spectral Sciences. 

7. Atmospheric Correction Coefficients Calculation
Using the modelled output of the radiative transfer, calculate the atmospheric correction coefficients. 

The atmospheric correction coefficients are required for computing Lambertian reflectance. The coefficients are given as follows: 

S = Atmospheric albedo 
TV = Total transmittance in the view (observer) direction 
TS = Total transmittance in the solar diection 
fV = Direct fraction in the view (observer) direction 
fS = Direct fraction in the solar direction 
A = (Dir + Dif) / Pi * TV 
B = Path radiance 
Dir = Direct irradiance at the surface 
Dif = Diffuse irradiance at the surface 

8. Bilinear Interpolation of Atmospheric Correction Coefficients
The atmospheric correction coefficients are interpolated across the entire spatial extents of the 2D image. 

Bilinear interpolation is the method used to interpolate across the entire image for each of the following atmospheric correction coefficients: 

S = Atmospheric albedo 
fV = Direct fraction in the view (observer) direction 
fS = Direct fraction in the solar direction 
A = (Dir + Dif) / Pi * TV 
B = Path radiance 
Dir = Direct irradiance at the surface 
Dif = Diffuse irradiance at the surface 

Note: TV = Total transmittance in the view (observer) direction

9. Atmospheric Adjacency Correction
The lambertian reflectance from each spectal band is corrected for atmospheric adjacency. 

The correction is applied using a 2D kernel created from the point spread function. Rather than use traditional convolution, the procedure uses the Fourier transform to apply convolution resulting in a significantly faster computational process, which is desired for a production scale processing pipeline. 

Prior to applying convolution, the input array replaces any nulls within a given row, with the row-length average. The array is also checked for rows that are comprising entirely of null's. Any rows at the start and end of the array that are entirely null, are ignored. However, if there are any rows of all null data, that have valid data in previous or following rows, then an Exception is raised and processing stops. 

Following on from filling nulls with row-length averages, the array is buffered by at least half the kernel size, in both dimensions, and buffered again to get the nearest power of 2 to optimise the Fourier transform as much as possible, whilst minimising spectral leakage. 

The buffering, or padding as it is called in numpy, uses "symmetric" for the input array, and "constant" for the input kernel. See https://numpy.org/doc/stable/reference/generated/numpy.pad.html for more information. 

Whilst the process might tighten the geospatial extents of the array in order to consecutive rows of valid data, the convolved result is inserted back into the full dimensions of the array ensure no loss of geospatial extent. 

10. MNDWI
The final packaged product was requested to be masked via a water mask derived from the Modified Normalised Difference Water Index. i.e. Any pixel that is not identified as water is to be set to null (-999). A minor investigation into what type of reflectance should be used for the MNDWI derivation resulted in negligible differences. As such, the lambertian reflectance with atmospheric adjacency correction was selected as the basis from which MNDWI is to be derived. Further information can be found here: https://gajira.atlassian.net/secure/RapidBoard.jspa?rapidView=422&projectKey=ARD&modal=detail&selectedIssue=ARD-1667 The following formulae yields MNDWI: MNDWI = (Green - SWIR) / (Green + SWIR) Where: Sentinel-2 Green corresponds to Band-3 (0.5425μm, 0.5775?m) SWIR corresponds to Band-11 (1.565μm, 1.655?m) Landsat-8 Green corresponds to Band-3 (0.525μm, 0.60μm) SWIR corresponds to Band-6 (1.56μm, 1.66μm) The water mask itself is derived using a simple single threshold: mask = MNDWI

11. Sky Glint Correction
The atmospheric adjacency corrected lambertian reflectance is refined further by applying a sky glint correction. The basis is assuming a fresnel reflectance on a water body. A default value of 1.34 is used for the refractive index of water. theta = satellite_view theta_prime = "arcsin(sin(theta) / refractive_index)" tolerance = "abs(theta + theta_prime) 

% ## Software

% ## References

