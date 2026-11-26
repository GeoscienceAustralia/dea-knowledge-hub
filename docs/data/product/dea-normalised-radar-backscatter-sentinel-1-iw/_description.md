
## Background 

The European Space Agency (ESA) has operated the Sentinel-1C-band Synthetic Aperture Radar satellite series since 2014. Unlike optical satellites, Sentinel-1 transmits microwave energy and measures the signal returned from the Earth’s surface. This allows observations to be captured by day or night and through cloud, smoke and haze. 

However, raw radar measurements do not directly characterise the surface. The signal is affected by viewing geometry, topography, sensor calibration, thermal noise, and the area of ground represented by each radar sample. To make accurate comparisons of imagery acquired at different times and geographic locations, it is necessary to correct these effects so the data are consistent and can be compared over time. 

This product takes Sentinel-1 imagery captured over the Australian continent and the Antarctic coastal zone and corrects for radiometric and geometric effects. The result is calibrated and standardised radar backscatter data, which is useful for identifying and quantifying environmental change, particularly where cloud, smoke or darkness limits optical imagery. 

## What this product offers 

The imagery is captured using the C-band Synthetic Aperture Radar instrument aboard the Sentinel-1 satellites in Interferometric Wide swath mode. 

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of radar backscatter data with minimal additional correction. It provides calibrated, noise-corrected backscatter at 20 m pixel spacing, with radiometric and geometric terrain corrections applied using a region-specific digital elevation model (DEM). Values are provided on a linear scale using the gamma-nought (γ<sub>0</sub>, `gamma0`) convention, which reduces variation caused by differing observation geometries and is recommended for most land applications. Ancillary layers are also provided so users can easily convert to other conventions, such as sigma-nought (σ<sub>0</sub>, `sigma0`), which is commonly used in sea ice and ice sheet studies in the Antarctic region. The product has been assessed as meeting the Committee on Earth Observation Satellites (CEOS) ARD requirements for NRB. 

Sentinel 1 can collect data in single-polarisation and dual-polarisation modes: 
* In single-polarisation mode, the transmitted and received signal is either VV or HH. 
* In dual-polarisation mode, the system transmits in one polarisation (VV or HH) and records both the co-polarised and cross-polarised returns: VV+VH or HH+HV. 

Based on these acquisition modes, four NRB product variants are generated from Sentinel 1 data. The trailing number in each product name is the collection number: 
* ga_s1_nrb_iw_vv_1 
* ga_s1_nrb_iw_vv_vh_1 
* ga_s1_nrb_iw_hh_1 
* ga_s1_nrb_iw_hh_hv_1 

## Applications 

This product can be used for: 
* flood extent and surface-water dynamics 
* wetlands and coastal change 
* soil moisture and post-fire landscape condition 
* vegetation structure and agricultural activity 
* infrastructure and surface change 
* ice-sheet, ice-shelf, glacier and iceberg change 
* emergency management and environmental monitoring 

% ## Access constraints

% ## Use constraints

## Technical information

### Synthetic Aperture Radar 

Sentinel-1 is a side-looking C-band radar system. Backscatter is influenced by surface roughness, structure, moisture and the orientation of the surface relative to the sensor. Co-polarised channels such as VV and HH and cross-polarised channels such as VH and HV provide complementary information about surface and volume scattering. 

### The Analysis Ready Data concept 

The Analysis Ready Data (ARD) package allows you to get up and running with your analysis as quickly as possible with minimal data preparation and additional input. This makes it simpler for you to develop applications and for the database to execute queries. 

The satellite data has been processed to a minimum set of requirements and organised into a form that allows immediate analysis and interoperability through time and with other datasets. This dataset has been peer-reviewed and satisfies the SAR NRB [CEOS Analysis Ready Data Requirements](https://ceos.org/ard/) according to the SAR Product Family Specifications version 1.2. 

### Conversions between backscatter conventions 

Normalised Radar Backscatter (NRB) is `gamma0` backscatter, a convention that minimises the effects of terrain by using a reference area that is perpendicular to the line of sight. Other backscatter conventions can be used, depending on the application, and can be reached using the following calculations.  

* `beta_0 = gamma0 * gamma0_to_beta0` (this convention is what is directly observed by the radar sensor and uses no terrain model for radiometry) 
* `sigma_0_T = gamma0 * gamma0_to_sigma0` (this convention removes some terrain effects and is commonly used for calibration purposes and has been extensively used older work) 

`Sigma_0` and `gamma0` can also be calculated with reference to the ellipsoid. These conventions still have terrain effects but have been corrected for sensor geometry and the ellipsoid. 

* `sigma_0_E = gamma0 * gamma0_to_beta0 * sin(incidence_angle)` 
* `gamma_0_E = gamma0 * gamma0_to_beta0 * tan(incidence_angle)` 

Note, the use of static layers gives an approximation and can yield slightly different values of `beta_0` and `sigma_0` compared to when calculated directly. These differences are very small and may only become larger over dramatic terrain.  

### Layover and shadow masking 

Three key terrain distortions can occur in SAR beta_0 backscatter imagery; foreshortening, layover and shadow. Foreshortening is the brightening of the sensor-facing terrain slope (foreslope) and can be corrected easily when converted to gamma0 with an accurate DEM. Shadow is the area behind a mountain which is unobserved by the sensor and will appear as no data (nan) within the NRB product. Layover occurs when different parts of the mountain (part of the ground, foreslope and backslope) are equal distances from the sensor. This layover causes the signals to merge together to yield very bright areas in beta_0, which are impossible to fully correct for in the NRB product. The NRB product includes a mask layer which users can use to remove layover and shadow affected pixels (1 = *shadow*, 2 = *layover*, 3 = *shadow and layover*). 

### Speckle Filtering 

Speckle is inherent to SAR imagery, caused by the interference of different microwaves as they bounce off surfaces within a resolution cell. This speckle is not random noise and is related to the amplitude of the backscatter returns and the number of looks. The number of looks is the number of radar grids that have been averaged into a geocoded resolution grid, and is available in the NRB product in a `number_of_looks` layer.  

There are many speckle filtering methods which can be applied to the NRB product to reduce the speckle noise, and some of them make use of the number of looks to statistically model speckle noise to aid in its correction. Below is a list of widely used speckle filters: 
* (Recommended) Lee-enhanced (adaptive number of looks) 
* Simple Lee filter 
* Lee-enhanced (fixed number of looks) 
* Frost 
* Gamma MAP 
* Total Variation Bregman 
* Non-local means 
* Temporal denoising 
* Gaussian filtering 

### Artifacts introduced by DEMs 

Digital Elevation Models approximate the terrain and may not reflect the exact conditions that the SAR sensor is responding to. This can lead to some artifacts in the imagery which end-users should be aware of, fortunately these artifacts remain consistent through time. 

There can be bright artifacts in NRB along ridgelines in Australia and Antarctica which are likely attributed to remnant, uncorrected layover effects. Over Australia, these artifacts appear to be about 3-5 pixels in width. Over Antarctica they can be larger. 

Over Antarctica, the terrain is dynamic and the DEM can quickly become out of date. This means that artifacts or inconsistencies can be introduced into the NRB product when the terrain does not match observation conditions. This is particularly true with large elevations changes over small horizontal distances, like crevasses. Users should consult the beta_0 backscatter convention to discern the origin of bright returns. 


## Lineage

This product is derived from the ESA Sentinel-1 Interferometric Wide Level-1 Single Look Complex archive. 

### Source data 

* Sentinel-1 IW Single Look Complex scenes from the Copernicus Australasia Regional Data Hub, Alaska Satellite Facility or Copernicus Data Space Ecosystem. 
* Precise Orbit Ephemerides for back processing, or Restituted Orbit files for ongoing processing. 
* Reference Elevation Model of Antarctica (REMA) v2 at 32 m mosaics over Antarctica and any covered sub-Antarctic islands 
* Copernicus GLO 30 DEM (Copernicus DEM 2021 release) at 30 m over Australian continent and sub-Antarctic islands outside REMA coverage. 
* Sentinel-1 burst database derived from the ESA burst ID map, which fixes the coordinate reference system, extent and pixel alignment for each burst. 

### Processing steps (SEE Appendix to be linked as separate page) 

Processing is run per Sentinel-1 scene by the workflow script `run_isce3_rtc_pipeline.sh` in the `sar-pipeline` Docker image. The radar processing follows the NASA JPL OPERA RTC-S1 workflow (blocks B1–B6 in the [OPERA RTC-S1 Product Specification](https://d2pn8kiwq2w21t.cloudfront.net/documents/ProductSpec_RTC-S1.pdf), JPL D-108758 Rev B, Section 2.1), with GA-specific steps for data access, DEM preparation, metadata and publishing. 

The following processing steps are applied to convert the Level-1 source data into the DE Sentinel-1 IW Normalised Radar Backscatter product: 
1. Scene and burst identification 
2. Existing product check 
3. Input download 
4. Run configuration 
5. Radiometric terrain correction and geocoding 
6. Metadata and publishing (`sar-pipeline`) 

### Methods and Software 

* **Area-projection RTC and geocoding**. Radiometric terrain correction and geocoding use the area-based projection algorithm of Shiroma, G. H. X., Lavalle, M. and Buckley, S. M. (2022), ‘An Area-Based Projection Algorithm for SAR Radiometric Terrain Correction and Geocoding’, IEEE Transactions on Geoscience and Remote Sensing, 60, 1–23. The algorithm is implemented in ISCE3 and described in the OPERA RTC-S1 ATBD (JPL D-107393). 

* **ISCE3 v0.24.4** (InSAR Scientific Computing Environment, 3rd generation) is the radar processing back end. GA uses v0.24.4 instead of the v0.15.0 pinned by upstream OPERA, to include fixes for the atmospheric (geolocation) corrections identified by GA. 

* **OPERA RTC Science Application Software**: the GA fork [`GeoscienceAustralia/RTC`](https://github.com/GeoscienceAustralia/RTC), release v1.0.7-GA-prod, of NASA JPL [`opera-adt/RTC`](https://github.com/opera-adt/RTC). The fork updates ISCE3 and sets GA processing settings and contact metadata. 

* **s1-reader v0.2.6** (OPERA) reads the SAFE files, burst metadata, burst IDs, and the calibration and noise look-up tables. - [https://github.com/isce-framework/s1-reader](https://github.com/isce-framework/s1-reader)  

* **dem-handler v0.2.6** (GA) mosaics the DEM tiles, handles the antimeridian, and converts the DEM to ellipsoidal heights. - [https://github.com/GeoscienceAustralia/dem-handler](https://github.com/GeoscienceAustralia/dem-handler)  

* **sar-pipeline** (GA) handles orchestration, data search and download, run-configuration generation, STAC metadata, and upload to S3. - [https://github.com/GeoscienceAustralia/sar-pipeline](https://github.com/GeoscienceAustralia/sar-pipeline) 

* **Burst database v0.18.0** is derived from ESA’s Sentinel-1 burst ID map using the OPERA burst database tools. It fixes the CRS and the 20 m grid for each burst. 

* **Workflow selection**. OPERA-ISCE3 was selected after an evaluation of five open workflows (OPERA-ISCE3, pyroSAR-SNAP, pyroSAR-GAMMA, HyP3-GAMMA and s1ard-SNAP) over Australia and Antarctica. It gave the best geolocation and image quality, it supports reusable static layers, and it can support InSAR in future. 

* **Production at scale**. Production runs on AWS: CDSE push subscriptions and an API Gateway feed SQS, then Step Functions, then AWS Batch on EC2. Daily completeness reports compare processed products with the CDSE catalogue. 

## References 

Shiroma, G. H., Lavalle, M., & Buckley, S. M. (2022). An area-based projection algorithm for SAR radiometric terrain correction and geocoding. *IEEE Transactions on Geoscience and Remote Sensing*, 60, 1-23. 

### Processing steps

### Software

% ## References

