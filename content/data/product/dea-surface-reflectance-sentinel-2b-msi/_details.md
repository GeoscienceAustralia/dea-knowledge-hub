## Background

The European Space Agency (*ESA*) has operated medium resolution satellites - Sentinel-2 series (Sentinel-2A and Sentinel-2B) since 2015. The spectral bands and spatial resolution of Sentinel-2 are similar to those of the Landsat series, but Sentinel-2 has a higher revisit frequency and spatial coverage. A combination of Sentinel-2 and Landsat data can provide good spatial and temporal coverage of the Earth's surface and provide useful information to monitor environmental resources over time, such as agricultural production and mining activities. However, the raw remotely sensed data received by these satellites in the solar spectral range do not directly characterise the underlying reflectance of surface objects. The data are modified by the atmosphere, variation of solar and sensor positions as well as surface anisotropic conditions. To make accurate comparisons of imagery acquired at different times, seasons and geographic locations, and detect the change of surface, it is necessary to remove/reduce these effects to ensure the data are consistent and can be compared over time.

## What this product offers

This product takes Sentinel-2B imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2B.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

It contains two sub-products that provide corrections or attribution information:

* [DEA Surface Reflectance NBART (Sentinel-2B MSI)](https://cmi.ga.gov.au/data-products/dea/824/dea-surface-reflectance-nbart-sentinel-2b-msi)
* [DEA Surface Reflectance OA (Sentinel-2B MSI)](https://cmi.ga.gov.au/data-products/dea/823/dea-surface-reflectance-oa-sentinel-2b-msi)

The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

**This Collection 3 (C3) product** and has been created by reprocessing Collection 1 (C1) and making improvements to the processing pipeline and packaging.

**Packaging updates include:**  

\- Open Data Cube (ODC) eo3 metadata  
\- metadata includes STAC fields to enable users to filter by fields such as tile ID or cloud cover percentage in applications such as ODC  
\- additional STAC metadata file in JSON format  
\- directory structure and file names that are consistent with Geoscience Australia’s Landsat C3 products.  

**Additional updates include:**

\- upgrading the spectral response function to result in a more accurate product. These new versions include minor updates, slight changes of the central wavelengths for band B02 of S2A and S2B, and band B01 of S2B, along with slight changes of the Full Width Half Maximum (FMWH) for most of the bands  
\- correction of solar constant errors in the conversion between reflectance and radiance as well as in the atmospheric correction  
\- an additional cloud mask layer (s2cloudless)  
\- removal of NBAR layers  
\- reduced spatial resolution of observation attribute layers to 20m resolution, with the contiguity layer being maintained at 10m  
\- additional of GQA information to dataset metadata  
\- removal of buffering from fmask layer  
\- BRDF ancillary upgraded from MODIS BRDF C5 to MODIS BRDF C6  
\- Upgrading from MODTRAN 5.2 to MODTRAN 6.

**The introduction of a maturity concept.**

The Collection 3 product is comprised of data produced to varying degrees of maturity. The maturity of a dataset is dictated by the quality of the ancillary information, such as BRDF and atmospheric correction data, used to generate the product. The maturity levels are Near Real Time (NRT), Interim and Final. The maturity level is designated in the filename and in the metadata.

\- Near Real Time (NRT) is a rapid ARD product produced < 48 hours after image capture.   
\- Interim ARD – If there are extended delays (>18 days) in delivery of inputs to the ARD model, interim production is utilised until the issue is resolved.    
\- Final ARD - As the higher quality ancillary datasets become available, a “Final” version of the Sentinel 2 ARD data is produced, which replaces the NRT or interim product.

% ## Data description

## Applications

This product can be used for:

* The development of derivative products to monitor land, inland waterways and coastal features, such as:

               -  urban growth  
               -  coastal habitats  
               -  mining activities  
               -  agricultural activity (e.g. pastoral, irrigated cropping, rain-fed cropping)  
               -  water extent.

* The development of refined information products, such as:

               -  areal units of detected surface water  
               -  areal units of deforestation  
               -  yield predictions of agricultural parcels.

* Compliance surveys.
* Emergency management.

## Technical information

#### Multispectral Instrument (MSI)

MSI is a push-broom sensor with a Three-Mirror Anastigmat (TMA) telescope with a pupil diameter equivalent to 150 mm, isostatically mounted on the platform to minimise thermo-elastic distortions. Surface Reflectance values range between 0 and 10000. MSI collects data for visible, near infrared, and shortwave infrared spectral bands. 

#### The Analysis Ready Data concept

The Analysis Ready Data (ARD) package allows you to get up and running with your analysis as quickly as possible with minimal data preparation and additional input. This makes it simpler for you to develop applications and for the database to execute queries.

The satellite data has been processed to a minimum set of requirements and organised into a form that allows immediate analysis and interoperability through time and with other datasets. It has been adapted from CEOS Analysis Ready Data ([CARD4L](http://ceos.org/ard/)).

The [technical report](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/145101) containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available.

#### ARD sub-products

*1) [DEA Surface Reflectance NBART (Sentinel-2B MSI)](https://cmi.ga.gov.au/data-products/dea/824/dea-surface-reflectance-nbart-sentinel-2b-msi)*

The sub-product produces standardised optical surface reflectance data using robust physical models which correct for variations and inconsistencies in the image of top atmospheric reflectance values. Corrections are performed using Nadir corrected Bidirectional reflectance distribution function Adjusted Reflectance (NBAR) with an additional terrain illumination correction applied (NBART).

*2) [DEA Surface Reflectance OA (Sentinel-2B MSI)](https://cmi.ga.gov.au/data-products/dea/823/dea-surface-reflectance-oa-sentinel-2b-msi)*

The NBART product depends upon the Observation Attributes (OA) product to provide accurate and reliable contextual information about the Sentinel-2B data. This ‘data provenance’ provides a chain of information which allows the data to be replicated or utilised by derivative applications. The OA takes a number of different forms, including satellite, solar and surface geometry and classification attribution labels.

## Lineage

This product is derived from the ESA Sentinel-2B level 1C archive.

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

* Level 1C Collection 1 data was provided by the European Space  agency's Copernicus data hub, see [https://scihub.copernicus.eu/](https://scihub.copernicus.eu/)

## Processing steps

1. Longitude and Latitude Calculation

1. Satellite and Solar Geometry Calculation

1. Aerosol Optical Thickness Retrieval

1. BRDF Shape Function Retrieval

1. Ozone Retrieval

1. Elevation Retrieval and Smoothing

1. Slope and Aspect Calculation

1. Incidence and Azimuthal Incident Angles Calculation

1. Exiting and Azimuthal Exiting Angles Calculation

1. Relative Slope Calculation

1. Terrain Occlusion Mask

1. MODTRAN

1. Atmospheric Correction Coefficients Calculation

1. Bilinear Interpolation of Atmospheric Correction Coefficients

1. Surface Reflectance Calculation (NBAR + Terrain Illumination Correction)

1. Function of Mask (Fmask)

1. Contiguous Spectral Data Mask Calculation

## Software

* [MODTRAN](http://modtran.spectral.com/)
* [wagl](https://github.com/GeoscienceAustralia/wagl)
* [eugl](https://github.com/OpenDataCubePipelines/eugl)
* [tesp](https://github.com/OpenDataCubePipelines/tesp)
* [eodatasets](https://github.com/OpenDataCubePipelines/eo-datasets)
* [pythonfmask](http://www.pythonfmask.org/en/latest/)
* [s2cloudless](https://pypi.org/project/s2cloudless/)

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

