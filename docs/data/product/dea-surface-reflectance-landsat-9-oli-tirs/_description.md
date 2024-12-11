## Background

The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies.

In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These are reduced or removed to ensure the data is consistent and can be compared over time.

## What this product offers

This product takes Landsat 9 imagery captured over the Australian continent and corrects for inconsistencies caused by atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 9. Only the OLI data is included in this product, while the TIRS data is used in processing, particularly in identification of clouds.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections. 

It contains three sub-products that provide corrections or attribution information:
* [DEA Surface Reflectance NBAR (Landsat 9)](/data/product/dea-surface-reflectance-nbar-landsat-9-oli-tirs) \*
* [DEA Surface Reflectance NBART (Landsat 9)](/data/product/dea-surface-reflectance-nbart-landsat-9-oli-tirs) \*\*
* [DEA Surface Reflectance OA (Landsat 9)](/data/product/dea-surface-reflectance-oa-landsat-9-oli-tirs) \*\*\*

*Note: DEA produces NBAR as part of the Landsat ARD, this is available in the National Computing Infrastructure environment only. This product is not produced as part of the Sentinel-2 ARD.*

The resolution is a 30 m grid based on the USGS Landsat Collection 2 archive, or 15 m for the panchromatic band. This data forms part of the DEA Collection 3 archive. 

\* Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR)

\*\* Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance with terrain illumination correction (NBART)

\*\*\* Observation Attributes (OA)

**The introduction of a maturity concept.**

DEA Collection 3 products are comprised of data produced to varying degrees of maturity. The maturity of a dataset is dictated by the quality of the ancillary information, such as Bidirectional Reflectance Distribution Function (BRDF) and atmospheric data, used to generate the product. The maturity levels are Near Real Time (NRT), Interim and Final. The maturity level is designated in the filename and in the metadata.

* Near Real Time (NRT) is a rapid ARD product produced within 48 hours after image capture, using existing long term climatology data that is of slightly lower quality, allowing NRT data to be published quickly.   
* Interim ARD is produced if high quality ancillaries required for the final ARD model don’t become available within 23 days of image capture. Interim maturity data is produced as a *stand-in* until the full ancillaries are available to produce the final version. This is our fall-back until the issue is resolved.    
* Final ARD is DEA’s best quality ARD, produced using high quality ancillary datasets derived from observed data. These ancillary datasets are slower to produce but are observational datasets of the conditions at the time of image capture and so provide our most accurate dataset corrections. 

You can read more about dataset maturity in this page: [DEA dataset maturity explained](/guides/reference/dataset_maturity_guide/).

% ## Data description

## Applications

* The development of derivative products to monitor land, inland waterways and coastal features, such as:
  * urban growth
  * coastal habitats
  * mining activities
  * agricultural activity (e.g. pastoral, irrigated cropping, rain-fed cropping)
  * water extent
* The development of refined information products, such as:
  * areal units of detected surface water
  * areal units of deforestation
  * yield predictions of agricultural parcels.
* Compliance surveys
* Emergency management

## Technical information

### Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS)

OLI is a push-broom sensor with a four-mirror telescope and 14-bit quantisation. OLI collects data for visible, near infrared, and short wave infrared spectral bands as well as a panchromatic band.

TIRS measures land surface temperature in two thermal bands with new technology that applies quantum physics to detect heat.

### The Analysis Ready Data concept

The Analysis Ready Data (ARD) package allows you to get up and running with your analysis as quickly as possible with minimal data preparation and additional input. This makes it simpler for you to develop applications and for the database to execute queries.

The satellite data has been processed to a minimum set of requirements and organised into a form that allows immediate analysis and interoperability through time and with other datasets. It has been adapted from CEOS Analysis Ready Data ([CARD4L](http://ceos.org/ard/)).

The [technical report](https://pid.geoscience.gov.au/dataset/ga/145101) containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available.

### ARD sub-products

1) [DEA Surface Reflectance NBAR (Landsat 9 OLI-TIRS)](/data/product/dea-surface-reflectance-nbar-landsat-9-oli-tirs)

This sub-product produces standardised optical surface reflectance data using robust physical models which correct for variations and inconsistencies in image radiance values. Corrections are performed using Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR).

2) [DEA Surface Reflectance NBART (Landsat 9 OLI-TIRS)](/data/product/dea-surface-reflectance-nbart-landsat-9-oli-tirs)

This sub-product performs the same function as Surface Reflectance (Landsat 9 OLI-TIRS NBAR), but also applies terrain illumination correction.

3) [DEA Surface Reflectance OA (Landsat 9 OLI-TIRS)](/data/product/dea-surface-reflectance-oa-landsat-9-oli-tirs)

The NBAR and NBART sibling products depend upon the Observation Attributes (OA) product to provide accurate and reliable contextual information about the Landsat data. This ‘data provenance’ provides a chain of information which allows the data to be replicated or utilised by derivative applications. It takes a number of different forms, including satellite, solar and surface geometry and classification attribution labels.

## Lineage

This product is derived from the USGS Landsat Level 1 Collection 2 archive.

* The Moderate Resolution Imaging Spectroradiometer (MODIS) MCD43A1 Version 6 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameters dataset was provided by the National Aeronautics and Space Administration (NASA). It was produced daily using 16 days of Terra and Aqua MODIS data at 500 m resolution.   
 See [USGS: MCD43A1](https://lpdaac.usgs.gov/products/mcd43a1v006/), [NASA: MODIS BRDF / Albedo Parameter](https://modis.gsfc.nasa.gov/data/dataprod/mod43.php), [Schaaf et al. (2002)](https://www.doi.org/10.1016/s0034-4257(02)00091-3)

* The ozone data was provided by Environment Canada.   
 See [Environment Canada: Global Ozone Maps](https://exp-studies.tor.ec.gc.ca/e/ozone/Curr_allmap_g.htm)

* The Aerosol Optical Thickness data was provided by the Commonwealth Scientific and Industrial Research Organisation (CSIRO).   
 See [Qin et al. (2015)](https://doi.org/10.1109/TGRS.2015.2433911)

* The Precipitable Water for Entire Atmosphere data was provided by the National Oceanic and Atmospheric Administration (NOAA) / Earth System Research Laboratory (ESRL) / Physical Sciences Division (PSD).  
 See [Kalnay et al. (1996)](https://doi.org/10.1175/1520-0477(1996)077%3c0437:tnyrp%3e2.0.co;2)

* The baseline Digital Surface Model (DSM) data produced from the Shuttle Radar Topography Mission (SRTM) was provided by the National Geospatial-Intelligence Agency (NGA).   
 See [NGA: SRTM](https://www.nga.mil/about/history.html), [NASA: SRTM](https://www2.jpl.nasa.gov/srtm/index.html)

* Level 1 Collection 2 data was provided by the United States Geological Survey (USGS)'s Earth Resources Observation and Science (EROS) Center.  
 See [USGS: EROS](https://www.usgs.gov/centers/eros), [USGS: Landsat Collection 2](https://www.usgs.gov/landsat-missions/landsat-collection-2?qt-science_support_page_related_con=1#qt-science_support_page_related_con)

## Processing steps

1. [Longitude and Latitude Calculation](/guides/reference/analysis_ready_data_corrections/#lon-lat-calculation)
2. [Satellite and Solar Geometry Calculation](/guides/reference/analysis_ready_data_corrections/#sat-sol-geom-calculation)
3. [Aerosol Optical Thickness Retrieval](/guides/reference/analysis_ready_data_corrections/#aero-opt-thick-retr)
4. [BRDF Shape Function Retrieval](/guides/reference/analysis_ready_data_corrections/#brdf-shp-fnc-retr)
5. [Ozone Retrieval](/guides/reference/analysis_ready_data_corrections/#o3-retr)
6. [Elevation Retrieval and Smoothing](/guides/reference/analysis_ready_data_corrections/#elev-retr-smth)
7. [Slope and Aspect Calculation](/guides/reference/analysis_ready_data_corrections/#slp-asp-calc)
8. [Incidence and Azimuthal Incident Angles Calculation](/guides/reference/analysis_ready_data_corrections/#inc-azm-ang-calc)
9. [Exiting and Azimuthal Exiting Angles Calculation](/guides/reference/analysis_ready_data_corrections/#ext-azm-ang-calc)
10. [Relative Slope Calculation](/guides/reference/analysis_ready_data_corrections/#rel-slp-calc)
11. [Terrain Occlusion Mask](/guides/reference/analysis_ready_data_corrections/#terr-occ-msk)
12. [MODTRAN](/guides/reference/analysis_ready_data_corrections/#modtran)
13. [Atmospheric Correction Coefficients Calculation](/guides/reference/analysis_ready_data_corrections/#atm-corr-coef-calc)
14. [Bilinear Interpolation of Atmospheric Correction Coefficients](/guides/reference/analysis_ready_data_corrections/#bil-int-atm-corr-coef)
15. [Surface Reflectance Calculation (NBAR)](/guides/reference/analysis_ready_data_corrections/#nbar)
16. [Surface Reflectance Calculation (NBAR + Terrain Illumination Correction)](/guides/reference/analysis_ready_data_corrections/#nbart)
17. [Function of Mask (Fmask)](/guides/reference/analysis_ready_data_corrections/#fmask)
18. [Contiguous Spectral Data Mask Calculation](/guides/reference/analysis_ready_data_corrections/#cont-spec-data-mask-calc)

## Software

* [MODTRAN](http://modtran.spectral.com/)
* [wagl](https://github.com/GeoscienceAustralia/wagl)
* [eugl](https://github.com/OpenDataCubePipelines/eugl)
* [tesp](https://github.com/OpenDataCubePipelines/tesp)
* [eodatasets](https://github.com/OpenDataCubePipelines/eo-datasets)
* [pythonfmask](http://www.pythonfmask.org/en/latest/)

## References

Berk, A., Conforti, P., Kennett, R., Perkins, T., Hawes, F., & van den Bosch, J. (2014, June 13). *MODTRAN6: A major upgrade of the MODTRAN radiative transfer code* (M. Velez-Reyes & F. A. Kruse, Eds.). [https://doi.org/10.1117/12.2050433](https://doi.org/10.1117/12.2050433)

Dymond, J. R., & Shepherd, J. D. (1999). Correction of the topographic effect in remote sensing. IEEE Transactions on Geoscience and Remote Sensing, 37(5), 2618–2619. [https://doi.org/10.1109/36.789656](https://doi.org/10.1109/36.789656)

Hudson, S. R., Warren, S. G., Brandt, R. E., Grenfell, T. C., & Six, D. (2006). Spectral bidirectional reflectance of Antarctic snow: Measurements and parameterization. Journal of Geophysical Research, 111(D18), D18106. [https://doi.org/10.1029/2006JD007290](https://doi.org/10.1029/2006JD007290)

Kalnay, E., Kanamitsu, M., Kistler, R., Collins, W., Deaven, D., & Gandin, L. et al. (1996). The NCEP/NCAR 40-Year Reanalysis Project. Bulletin Of The American Meteorological Society, 77(3), 437-471. [https://doi.org/10.1175/1520-0477(1996)077<0437:tnyrp>2.0.co;2](https://doi.org/10.1175/1520-0477(1996)077<0437:tnyrp>2.0.co;2)

Li, F., Jupp, D. L. B., Reddy, S., Lymburner, L., Mueller, N., Tan, P., & Islam, A. (2010). An evaluation of the use of atmospheric and brdf correction to standardize landsat data. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, *3*(3), 257–270. [https://doi.org/10.1109/JSTARS.2010.2042281](https://doi.org/10.1109/JSTARS.2010.2042281)

Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. Remote Sensing of Environment, 124, 756–770. [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

Qin, Y., Mitchell, R., & Forgan, B. W. (2015). Characterizing the aerosol and surface reflectance over Australia using AATSR. IEEE Transactions on Geoscience and Remote Sensing, 53(11), 6163–6182. [https://doi.org/10.1109/TGRS.2015.2433911](https://doi.org/10.1109/TGRS.2015.2433911 )

Schaaf, C., Gao, F., Strahler, A., Lucht, W., Li, X., & Tsang, T. et al. (2002). First operational BRDF, albedo nadir reflectance products from MODIS. Remote Sensing Of Environment, 83(1-2), 135-148. [https://www.doi.org/10.1016/s0034-4257(02)00091-3](https://www.doi.org/10.1016/s0034-4257(02)00091-3)

SZA. (2011). Retrieved May 2019, from [http://sacs.aeronomie.be/info/sza.php](http://sacs.aeronomie.be/info/sza.php)

Zhu, Z., Wang, S., & Woodcock, C. (2015). Improvement and expansion of the Fmask algorithm: cloud, cloud shadow, and snow detection for Landsats 4–7, 8, and Sentinel 2 images. Remote Sensing Of Environment, 159, 269-277. [https://doi.org/10.1016/j.rse.2014.12.014](https://doi.org/10.1016/j.rse.2014.12.014)

Zhu, Z., & Woodcock, C. E. (2012). Object-based cloud and cloud shadow detection in Landsat imagery. Remote Sensing of Environment, 118, 83–94. [https://doi.org/10.1016/j.rse.2011.10.028](https://doi.org/10.1016/j.rse.2011.10.028)

