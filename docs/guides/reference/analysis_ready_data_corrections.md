# Analysis Ready Data production

## Processing steps

<h3 id="lon-lat-calculation"> Longitude and Latitude Calculation </h3>
For a given acquisition's spatial extent and pixel resolution, create full dimension arrays/images whose pixel/cell contents contain the longitude and latitude values based on the WGS84 datum.

The values at each pixel represent either the longitude or latitude for the upper left-hand corner of the pixel.  The Coordinate Reference System (CRS) of the spatial extent isn't required to be in Geographics WGS84, nor do the units of the pixel resolution required to be in decimal degrees.

The algorithm outputs spatial grids in the native CRS and pixel resolution, just the array/image contents at the pixel level contain either a longitude or latitude value.

<h3 id="sat-sol-geom-calculation"> Satellite and Solar Geometry Calculation </h3>
Accurate positional geometry of the sun and observer are required in order to standardise a surface reflectance measurement so that it is consistent across time and space.

The process calculates at full acquisition resolution and spatial extent in native CRS, the following datasets:

|                       |                                                               |
|-----------------------|---------------------------------------------------------------|
| **Solar zenith**      | The angle between the zenith and the centre of the Sun's disc | 
| **Solar azimuth**     | The angle of the sun's position from true north               |
| **Satellite view**    | The angle between the zenith and the satellite                |
| **Satellite azimuth** | The angle of the satellite's position from true north         |
| **Relative azimuth**  | The relative azimuth between the sun and view directions      |
| **Time Delta**        | The time in seconds from satellite apogee                     |

<h3 id="aero-opt-thick-retr"> Aerosol Optical Thickness Retrieval </h3>
For a given acquisition, retrieve the aerosol optical thickness estimate for input into the radiative transfer evaluation.

The supplied aerosol optical thickness data is a geospatially sparse point cloud and only exists for the years 2002 to 2008, supplemented by monthly composites.

Essentially the spatial extent of the acquisition in longitude and latitude for the WGS84 datum is intersected with the geospatial extent of the aerosol data, and a mean value extracted.

If the year of acquisition falls within 2002-2008, then select the points that have a timestamp of within 0.5 days of the acquisition, and fall within the geospatial intersection area of interest.  If no data are found, fallback to a monthly aggregate for that year.  If this also fails, then fall back to an all-time monthly aggregate.  If this also fails then return a nominal value of 0.06.

<h3 id="brdf-shp-fnc-retr"> BRDF Shape Function Retrieval </h3>
Retrieve the BRDF shape function parameters for each supported spectral band within the acquisition.

For each supported spectral band within an acquisition to be processed, retrieve the BRDF shape function parameters, Alpha-1 and Alpha-2.

The spatial extent of the acquisition in native Coordinate Reference System (CRS) units is projected into the Sinusoidal CRS of the MCD43A1 data.  Once projected, the Isometric, Volumetric and Geometric albedo parameters are retrieved for the area of interest, for each of the acquisitions supported spectral bands, from the relevant spectral bands of the MCD43A1 data and aggregated.

The results are then transformed into the BRDF Shape function, labelled as Alpha-1 and Alpha-2, by the following ratio's:

> **Alpha-1** = $Volumetric / Isometric$
>
> **Alpha-2** = $Geometric / Isometric$

If the spectral band for the acquisition has a wavelength broad enough to cover multiple MODIS spectral bands, then averages are taken from all derived Alpha-1 and Alpha-2 parameters, before returning single pair of Alpha-1 and Alpha-2 BRDF shape function parameters.

<h3 id="o3-retr"> Ozone Retrieval </h3>
Retrieval of ozone data for the acquisition of interest at a given (longitude, latitude) location for a given month.

The ozone data consists of 12 global datasets, 1 for each month of the year.  The month that the acquisition was taken in, is used as a basis for selecting the appropriate month containing the relevant ozone data.

As the source ozone data is of a very low resolution, the acquisition's central coordinate in longitude and latitude degrees, based on the WGS84 datum, is used as a sole point to retrieve an ozone value to be used as a value for the entire acquisition's spatial extent.

<h3 id="elev-retr-smth"> Elevation Retrieval and Smoothing </h3>
For a given acquisition, retrieve the Digital Surface Model (DSM) that covers the full spatial extent with an additional buffer which by default is 8km.  The DSM is resampled to the required CRS and pixel resolution using Bi-Linear interpolation, then smoothed with a 3 by 3 Gaussian kernel to remove extraneous noise.

The algorithm defaults to retrieving the elevation data with a buffer of 8km on all edges of an acquisition's spatial extents.

<h3 id="slp-asp-calc"> Slope and Aspect Calculation </h3>
For a given Digital Elevation Model (DSM) calculate at a pixel level the slope and aspect.

The following steps dictate the method for determining slope and aspect.

1. A sobel filter is used to determine the rate of change at a pixel level for both the horizontal and vertical directions ($d_z/d_x$ and $d_z/d_y$)
2. Slope in radians = ATAN ( √ ([dz/dx]^2 + [dz/dy]^2) )
3. Aspect in radians = atan2 ([dz/dy], -[dz/dx])

4. Both arrays are then converted to degrees.

<h3 id="inc-azm-ang-calc"> Incidence and Azimuthal Incident Angles Calculation </h3>
For a given acquisition calculate the incident and azimuthal incident angles for the full spatial extent in the native Coordinate Reference System (CRS) and at the full/native pixel resolution.

The incident (angle between a ray incident on a surface and the line perpendicular to the surface at the point of incidence) and azimuthal incident (azimuth angle for incident direction in the slope geometry) angles are calculated at a pixel level for the entire spatial extent and pixel resolution for a given acquisition.

The two arrays/images are returned with the values expressed in degrees.

<h3 id="ext-azm-ang-calc"> Exiting and Azimuthal Exiting Angles Calculation </h3>
For a given acquisition calculate the exiting and azimuthal exiting angles for the full spatial extent in the native Coordinate Reference System (CRS) and at the full/native pixel resolution.

The exiting (angle between a ray reflected on a surface and the line perpendicular to the surface at the point of emergence) and azimuthal exiting (azimuth angle for exiting direction in the slope geometry) angles are calculated at a pixel level for the entire spatial extent and pixel resolution for a given acquisition.

The two arrays/images are returned with the values expressed in degrees.

<h3 id="rel-slp-calc"> Relative Slope Calculation </h3>
Calculate the relative azimuth slope given the azimuthal incident and azimuthal exiting angles on a sloping surface.

<h3 id="terr-occ-msk"> Terrain Occlusion Mask </h3>
For a given elevation dataset, create a terrain occlusion mask.

The terrain occlusion mask is a multi-step process that identifies pixel occlusion by the surrounding terrain (cast shadow) from two different viewing sources (solar and satellite/observer), as well as pixels that exhibit shadow unto itself (self shadow).

A pixel is determined to be shaded if it is not viewable by:
* The satellite (observer)
* The sun 

The pixel doesn't receive direct radiation as the surface faces away from the sun. 

The algorithm is based on:
Giles, P.T.. (2001). Remote sensing and cast shadows in mountainous terrain. Photogrammetric Engineering and Remote Sensing. 67. 833-839.

<h3 id="modtran"> MODTRAN </h3>
MODerate resolution atmospheric TRANsmission is used for the prediction and analysis of optical measurements through the atmosphere.

MODTRAN was developed and continues to be maintained through a longstanding collaboration between Spectral Sciences, Inc. (SSI) and the Air Force Research Laboratory (AFRL). The code is embedded in many operational and research sensor and data processing systems, particularly those involving the removal of atmospheric effects, commonly referred to as atmospheric correction, in remotely sensed multi- and hyperspectral imaging (MSI and HSI).

The MODTRAN software computes line-of-sight (LOS) atmospheric spectral transmittances and radiances over the ultraviolet through long wavelength infrared spectral regime (0 - 50,000 cm-1; > 0.2 μm). The radiation transport (RT) physics within MODTRAN provides accurate and fast methods for modelling stratified, horizontally homogeneous atmospheres. The core of the MODTRAN RT is an atmospheric "narrow band model" algorithm. The atmosphere is modelled via constituent vertical profiles, both molecular and particulate, defined either using built-in models or by user-specified radiosonde or climatology data. The band model provides resolution as fine as 0.2 cm-1 from its 0.1 cm-1 band model. MODTRAN solves the radiative transfer equation including the effects of molecular and particulate absorption/emission and scattering, surface reflections and emission, solar/lunar illumination, and spherical refraction.

[http://modtran.spectral.com/modtran_about](http://modtran.spectral.com/modtran_about)

[http://modtran.spectral.com/](http://modtran.spectral.com/)

<h3 id="atm-corr-coef-calc"> Atmospheric Correction Coefficients Calculation </h3>
Using the modelled output of the radiative transfer, calculate the atmospheric correction coefficients.

The atmospheric correction coefficients are required for computing Lambertian reflectance.  The coefficients are given as follows:

> **S** = Atmospheric albedo
>
> **TV** = Total transmittance in the view (observer) direction
>
> **TS** = Total transmittance in the solar diection
>
> **fV** = Direct fraction in the view (observer) direction
>
> **fS** = Direct fraction in the solar direction
>
> **A** = $(Dir + Dif) / Pi \times TV$
>
> **B** = Path radiance
>
> **Dir** = Direct irradiance at the surface
>
> **Dif** = Diffuse irradiance at the surface


<h3 id="bil-int-atm-corr-coef"> Bilinear Interpolation of Atmospheric Correction Coefficients </h3>
The atmospheric correction coefficients are interpolated across the entire spatial extents of the 2D image.

Bilinear interpolation is the method used to interpolate across the entire image for each of the following atmospheric correction coefficients:

> **S** = Atmospheric albedo
>
> **fV** = Direct fraction in the view (observer) direction
>
> **fS** = Direct fraction in the solar direction
>
> **A** = $(Dir + Dif) / Pi \times TV$
>
> **B** = Path radiance
>
> **Dir** = Direct irradiance at the surface
>
> **Dif** = Diffuse irradiance at the surface

Note: **TV** = Total transmittance in the view (observer) direction

<h3 id="nbar"> Surface Reflectance Calculation (NBAR) </h3>
Calculate a standardised optical surface reflectance using robust physical models to correct for variations in image radiance values due to atmospheric properties, sun and sensor geometry as well as the directional reflectance properties of the surface being observed.

The process of producing standardised optical surface reflectance is known as Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR).

This enables comparison of imagery acquired at different times, in different seasons and in different geographic locations.

Algorithm details can be found here: [https://doi.org/10.1109/JSTARS.2010.2042281](https://doi.org/10.1109/JSTARS.2010.2042281)

<h3 id="nbart"> Surface Reflectance Calculation (NBAR + Terrain Illumination Correction) </h3>
Calculate a standardised optical surface reflectance using robust physical models to correct for variations in image radiance values due to atmospheric properties, sun and sensor geometry and accounts for the directional reflectance properties of the surface.  The process also accounts for the underlying surface topography via a process known as terrain illumination correction.

The process of producing standardised optical surface reflectance is known as Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR) coupled with a Terrain illumination correction.

This enables comparison of imagery acquired at different times, in different seasons, in different geographic locations over varying surface topography.

Algorithm details can be found here: [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

<h3 id="fmask"> Function of Mask (Fmask) </h3>
Function of Mask (Fmask), is a classification process that categorises pixels into mutually exclusive classes.  The classes are defined as an enumerator with values 0 -> 5.

The Fmask algorithm works across Landsat's 4, 5, 7 and 8, as well as Sentinel-2 A & B.  The algorithms may differ per sensor, but the classification schema is standardised across all platform's/sensors.

The classes/categories are:

> **Unclassified** -> 0
>
> **Clear** -> 1
>
> **Cloud** -> 2
>
> **Cloud Shadow** -> 3
>
> **Snow** -> 4
>
> **Water** -> 5

Further details on the algorithm can be found here:
* [https://doi.org/10.1016/j.rse.2011.10.028](https://doi.org/10.1016/j.rse.2011.10.028)
* [https://doi.org/10.1016/j.rse.2014.12.014](https://doi.org/10.1016/j.rse.2014.12.014)

A Python implementation of the algorithm written by Neil Flood, can be found here:
* [http://www.pythonfmask.org/en/latest/](http://www.pythonfmask.org/en/latest/)
* [https://github.com/ubarsc/python-fmask](https://github.com/ubarsc/python-fmask)

<h3 id="cont-spec-data-mask-calc"> Contiguous Spectral Data Mask Calculation </h3>
Given a 3D block/stack of imagery spectra, calculate a 2D mask indicating where pixels have valid data at each individual 2D image slice.  The resulting 2D mask will have 0 for non-contiguous spectra across the 3D domain, and 1 for contiguous spectra across the 3D domain.  The idea of this dataset is for users doing band math across the spectral domain, to mask out pixels that don't have valid data across each of the spectral bands.

<h3 id="sent-hub-cloud-detec"> Sentinel Hub's cloud detector for Sentinel-2 imagery </h3>
The s2cloudless classification is based on a single-scene pixel-based cloud detector developed by Sentinel Hub's research team and is described in more detail in this blog.

The s2cloudless algorithm was part of an international collaborative effort aimed at intercomparing cloud detection algorithms. The s2cloudless algorithm was validated together with 9 other algorithms on 4 different test datasets and in all cases found to be on the Pareto front. See the [paper](https://doi.org/10.1016/j.rse.2022.112990).
