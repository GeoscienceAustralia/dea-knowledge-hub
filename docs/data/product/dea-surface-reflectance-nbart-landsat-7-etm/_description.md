## Background

:::{admonition} Sub-product
:class: note
This is a sub-product of [DEA Surface Reflectance (Landsat 7 ETM+)](/data/product/dea-surface-reflectance-landsat-7-etm). See the parent product for more information.
:::

Radiance data collected by Landsat 7 Enhanced Thematic Mapper Plus (ETM+) sensors can be affected by atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect.

Surfaces with varying terrain can introduce inconsistencies to optical satellite images through irradiance and bidirectional reflectance distribution function (BRDF) effects. For example, slopes facing the sun appear brighter compared with those facing away from the sun. Likewise, many surfaces on Earth are anisotropic in nature, so the signal picked up by a satellite sensor may differ depending on the sensor’s position.

These need to be reduced or removed to ensure the data is consistent and can be compared over time.

## What this product offers

This product takes Landsat 7 ETM+ imagery captured over the Australian continent and corrects the inconsistencies across land and coastal fringe. It achieves this using Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR).

However, in addition, this product applies terrain illumination correction to correct for varying terrain.

The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

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

It delivers modelled surface reflectance from Landsat 7 ETM+ data using physical rather than empirical models. This ensures that the reflective value differences between imagery acquired at different times by different sensors will be primarily due to on-ground changes in biophysical parameters rather than artefacts of the imaging environment.

This product is created using a physics-based, coupled Bidirectional Reflectance Distribution Function (BRDF) and atmospheric correction model that can be applied to both flat and inclined surfaces (Li et al. 2012). The resulting surface reflectance values are comparable both within individual images and between images acquired at different times.

For more information on the BRDF/Albedo Model Parameters product, see [NASA MODIS BRDF/Albedo parameter](https://modis.gsfc.nasa.gov/data/dataprod/mod43.php) and [MCD43A1 BRDF/Albedo Model Parameters Product](https://www.umb.edu/spectralmass/v006/mcd43a1-brdf-albedo-model-parameters-product/).

### Landsat archive

To improve access to Australia’s archive of Landsat TM/ETM+/OLI data, several collaborative projects have been undertaken in conjunction with industry, government and academic partners. These projects have enabled implementation of a more integrated approach to image data correction that incorporates normalising models to account for atmospheric effects, BRDF and topographic shading (Li et al. 2012). The approach has been applied to Landsat TM/ETM+ and OLI imagery to create baseline surface reflectance products.

The advanced supercomputing facilities provided by the National Computational Infrastructure (NCI) at the Australian National University (ANU) have been instrumental in handling the considerable data volumes and processing complexities involved with the production of this product.

### Image format specifications

#### band01, band02, band03, band04, band05, band07

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

#### thumbnail

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Format           | JPEG                                                                                                           |
| RGB combination  | Red: band 3 <br /> Green: band 2 <br /> Blue: band 1                                                           |
| Resolution       | X and Y directions each resampled to 10% of the original size                                                  |
| Compression      | JPEG, Quality 75 (GDAL default) <br /> PHOTOMETRIC colour model: YCBCR                                         |
| Contrast stretch | Linear <br /> Input minimum: 10 <br /> Input maximum: 3500 <br /> Output minimum: 0 <br /> Output maximum: 255 |
| Output CRS       | Geographics (Latitude/Longitude) WGS84                                                                         |

% ## Lineage

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

% ## Software

% ## References

