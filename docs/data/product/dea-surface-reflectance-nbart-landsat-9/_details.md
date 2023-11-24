## Background

*This is a sub-product of [DEA Surface Reflectance (Landsat 9)](/data/product/dea-surface-reflectance-landsat-9-oli-tirs). See the parent product for more information.*

Radiance data collected by Landsat 9 sensors can be affected by atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect.

Surfaces with varying terrain can introduce inconsistencies to optical satellite images through irradiance and bidirectional reflectance distribution function (BRDF) effects. For example, slopes facing the sun appear brighter compared with those facing away from the sun. Likewise, many surfaces on Earth are anisotropic in nature, so the signal picked up by a satellite sensor may differ depending on the sensor’s position.

These need to be reduced or removed to ensure the data is consistent and can be compared over time.

## What this product offers

This product takes Landsat 9 imagery captured over the Australian continent and corrects the inconsistencies across land and coastal fringe. It achieves this using Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR).

However, in addition, this product applies terrain illumination correction to correct for varying terrain.

The resolution is a 30 m grid based on the USGS Landsat Collection 2 archive, or a 15 m grid for the panchromatic band.

% ## Data description

% ## Applications

## Technical information

### Radiance measurements

Landsat’s Earth Observation (EO) sensors measure radiance (brightness of light), which is a composite of:
* surface reflectance
* atmospheric condition
* interaction between surface land cover, solar radiation and sensor view angle
* land surface orientation relative to the imaging sensor

It has been traditionally assumed that Landsat imagery displays negligible variation in sun and sensor view angles. However, these can vary significantly both within and between scenes, especially in different seasons and geographic regions (Li et al. 2012).

### Surface reflectance correction models

This product represents standardised optical surface reflectance using robust physical models to correct for variations and inconsistencies in image radiance values.

It delivers modelled surface reflectance from Landsat 9 OLI-TIRS data using physical rather than empirical models. This ensures that the reflective value differences between imagery acquired at different times by different sensors will be primarily due to on-ground changes in biophysical parameters rather than artefacts of the imaging environment.

This product is created using a physics-based, coupled Bidirectional Reflectance Distribution Function (BRDF) and atmospheric correction model that can be applied to both flat and inclined surfaces (Li et al. 2012). The resulting surface reflectance values are comparable both within individual images and between images acquired at different times.

For more information on the BRDF/Albedo Model Parameters product, see [NASA MODIS BRDF/Albedo parameter](https://modis.gsfc.nasa.gov/data/dataprod/mod43.php) and [MCD43A1 BRDF/Albedo Model Parameters Product](https://www.umb.edu/spectralmass/v006/mcd43a1-brdf-albedo-model-parameters-product/).

This product also corrects for differences in terrain using a Digital Elevation Model (DEM).

### Landsat archive

To improve access to Australia’s archive of Landsat TM/ETM+/OLI data, several collaborative projects have been undertaken in conjunction with industry, government and academic partners. These projects have enabled implementation of a more integrated approach to image data correction that incorporates normalising models to account for atmospheric effects, BRDF and topographic shading (Li et al. 2012). The approach has been applied to Landsat TM/ETM+ and OLI imagery to create baseline surface reflectance products.

The advanced supercomputing facilities provided by the National Computational Infrastructure (NCI) at the Australian National University (ANU) have been instrumental in handling the considerable data volumes and processing complexities involved with the production of this product.

**Bands Included in the Analysis Ready Data**

The product contains 8 bands

| Band number | Band name          | Wave length    | Resolution |
|-------------|--------------------|----------------|------------|
| Band 1      | Visible            | 0.43 - 0.45 µm | 30 m       |
| Band 2      | Visible            | 0.45 - 0.51 µm | 30 m       |
| Band 3      | Visible            | 0.53 - 0.59 µm | 30 m       |
| Band 4      | Red                | 0.64 - 0.67 µm | 30 m       |
| Band 5      | Near-Infrared      | 0.85 - 0.88 µm | 30 m       | 
| Band 6      | SWIR 1             | 1.57 - 1.65 µm | 30 m       | 
| Band 7      | SWIR 2             | 2.11 - 2.29 µm | 30 m       |
| Band 8      | Panchromatic (PAN) | 0.50 - 0.68 µm | 15 m       |

### Image format specifications

#### band01, band02, band03, band04, band05, band06, band07

|                                |                                                                                                                                   |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Format                         | GeoTIFF                                                                                                                           |
| Resolution                     | 30m                                                                                                                               |
| Datatype                       | Int16                                                                                                                             |
| No data value                  | -999                                                                                                                              |
| Valid data range               | [1,10000]                                                                                                                         |
| Tiled with X and Y block sizes | 512x512                                                                                                                           |
| Compression                    | Deflate, Level 6, Predictor 2                                                                                                     |
| Pyramids                       | Levels: [8,16,32] <br /> Compression: deflate <br /> Resampling: GDAL default (nearest) <br /> Overview X&Y block sizes: 512x512  |
| Contrast stretch               | None                                                                                                                              |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum                                                             |

#### band08

|                                |                                                                       |
|--------------------------------|-----------------------------------------------------------------------|
| Format                         | GeoTIFF                                                               |
| Resolution                     | 15m                                                                   |
| Datatype                       | Int16                                                                 |
| No data value                  | -999                                                                  |
| Valid data range               | [1,10000]                                                             |
| Tiled with X and Y block sizes | 512x512                                                               |
| Compression                    | Deflate, Level 6, Predictor 2                                         |
| Pyramids                       | None                                                                  |
| Contrast stretch               | None                                                                  |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum |

### thumbnail

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Format           | JPEG                                                                                                           |
| RGB combination  | Red: band 4 <br /> Green: band 3 <br /> Blue: band 2                                                           |
| Resolution       | X and Y directions each resampled to 10% of the original size                                                  |
| Compression      | JPEG, Quality 75 (GDAL default) <br /> PHOTOMETRIC colour model: YCBCR                                         |
| Contrast stretch | Linear <br /> Input minimum: 10 <br /> Input maximum: 3500 <br /> Output minimum: 0 <br /> Output maximum: 255 |
| Output CRS       | Geographics (Latitude/Longitude) WGS84                                                                         |

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

1. [Longitude and Latitude Calculation](/guides/reference/analysis_ready_data_corrections#lon-lat-calculation)
2. [Satellite and Solar Geometry Calculation](/guides/reference/analysis_ready_data_corrections#sat-sol-geom-calculation)
3. [Aerosol Optical Thickness Retrieval](/guides/reference/analysis_ready_data_corrections#aero-opt-thick-retr)
4. [BRDF Shape Function Retrieval](/guides/reference/analysis_ready_data_corrections#brdf-shp-fnc-retr)
5. [Ozone Retrieval](/guides/reference/analysis_ready_data_corrections#o3-retr)
6. [Elevation Retrieval and Smoothing](/guides/reference/analysis_ready_data_corrections#elev-retr-smth)
7. [Slope and Aspect Calculation](/guides/reference/analysis_ready_data_corrections#slp-asp-calc)
8. [Incidence and Azimuthal Incident Angles Calculation](/guides/reference/analysis_ready_data_corrections#inc-azm-ang-calc)
9. [Exiting and Azimuthal Exiting Angles Calculation](/guides/reference/analysis_ready_data_corrections#ext-azm-ang-calc)
10. [Relative Slope Calculation](/guides/reference/analysis_ready_data_corrections#rel-slp-calc)
11. [Terrain Occlusion Mask](/guides/reference/analysis_ready_data_corrections#terr-occ-msk)
12. [MODTRAN](/guides/reference/analysis_ready_data_corrections#modtran)
13. [Atmospheric Correction Coefficients Calculation](/guides/reference/analysis_ready_data_corrections#atm-corr-coef-calc)
14. [Bilinear Interpolation of Atmospheric Correction Coefficients](/guides/reference/analysis_ready_data_corrections#bil-int-atm-corr-coef)
15. [Surface Reflectance Calculation (NBAR + Terrain Illumination Correction)](/guides/reference/analysis_ready_data_corrections#nbart)

% ## Software

## References

* Li, F., Jupp, D. L. B., Reddy, S., Lymburner, L., Mueller, N., Tan, P., & Islam, A. (2010). An evaluation of the use of atmospheric and BRDF correction to standardize Landsat data. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 3(3), 257–270. [https://doi.org/10.1109/JSTARS.2010.2042281](https://doi.org/10.1109/JSTARS.2010.2042281)  
  
* Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. Remote Sensing of Environment, 124, 756–770. [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

