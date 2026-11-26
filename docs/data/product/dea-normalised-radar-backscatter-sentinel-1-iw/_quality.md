## Accuracy 

The accuracy of the product is influenced by the Sentinel-1 observations, orbit information, digital elevation model and radar viewing geometry. Terrain correction is only as accurate as the digital elevation model. Changing ice surfaces, including calving fronts, ice-shelf edges and surging glaciers, may not be represented by the DEM and can produce radiometric or geometric artefacts. The impact of these artefacts can be reduced by applying the associated conversion layers, such as converting to sigma-nought (σ0) referenced to the ellipsoid, which is independent of the underlying terrain. 

Backscatter in layover and shadow is not reliable. These pixels are identified in the mask band. Thermal noise is removed, however smooth surfaces such as calm water, some ice and snow, and cross-polarised channels can approach or fall below the sensor noise floor. No speckle filter is applied. 

*The Accuracy values in the following sections are indicative results from test products made before production when evaluating which software to use. The analysis should be updated using actual products from the GA Sentinel-1 NRB IW.* 

## Geolocation accuracy 

Geolocation accuracy is estimated using the known location of corner reflectors (CRs). A CR is a metal target with a surveyed position. It shows as a bright point in the image. The absolute location error (ALE) is the distance between the surveyed position and the measured position of that point. The primary test site is the Surat Basin CR array in Queensland: 39 CRs (1.5–2.5 m), 7 scenes from July 2023 to January 2024, and 243 measurements. The production product applies the bistatic delay and static tropospheric corrections in ISCE3. Table 1 shows the results with these corrections applied. 

Table 1 - Geolocation error at the Surat Basin CR array (10 m test products) 

|Surat Basin           | ISCE3 v0.24.4 | 
|                      | (atmospheric corrections enabled) |
|:----------------------:|:-----------------------------------:|
|Orbit (relative orbit)| Ascending (111) |
|Scenes |	7 |
|CR measurements| 243 |
|Mean ALE ± SD | 2.94 ± 0.92 m |
|Easting bias ± SD | 1.14 ± 1.19 m | 
|Northing bias ± SD | 2.25 ± 1.30 m |
|Range bias ± SD | 1.70 ± 0.99 m |
|Azimuth bias ± SD | 1.87 ± 1.46 m | 
|CR measurements with ALE ≤ 4 m | 88% | 
|Scene means with ALE ≤ 4 m | 100% (7 of 7) |
|SD of scene mean ALE through time | 0.26 m |

*Positive range bias is away from the sensor. Positive azimuth bias is in the flight direction. The requirement is 4 m (20% of the 20 m pixel).* 

* Requirement. All 7 scene means meet the 4 m requirement. 88% of the individual CR measurements meet it. 

* Stability. Geolocation is stable through time. The scene mean ALE changes by 0.26 m (SD) during the 6 months. 

* NASA JPL OPERA values. The NASA JPL OPERA RTC-S1 production configuration uses bias −0.72 m (x) and −0.67 m (y), SD 0.70 m (x) and 0.62 m (y) (NASA JPL, 2026). The GA values are larger. The sign convention of the OPERA bias is not confirmed, so compare the sizes only. 

Three other sites each have one CR (Table 2). They include both orbit directions. The Antarctic CRs were temporary 0.9 m reflectors (2019). These results are indicative only, and the summary values above do not include them. The larger error at Bharati Station is not yet explained but may be due to a reprojection error in the code generating the results (see caveats for current results). 

Table 2 - Indicative results at single-CR sites (production, ISCE3 0.24.4) 

|Site (one CR) | Orbit (rel. orbit) |Scenes |CR size | Mean ALE | Range bias | Azimuth bias |
|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|Maitri Station, Antarctica |Ascending (118) |3 |0.9 m |3.30 m |3.07 m |0.52 m |
|Bharati Station, Antarctica |Descending (3) |2 |0.9 m |4.53 m |−1.02 m |−4.10 m |
|Yarragadee, Western Australia |Descending (61) |3 |1.5 m |2.13 m |1.96 m |0.84 m |

## Radiometric and terrain accuracy 

This was going to be a part of the paper published with CSIRO. Once the code is updated, the analysis will be repeated. 
* **Flat forest.** Over flat, dense forest in Queensland, γ⁰ agrees with published values for similar land cover, and with the other workflows that we tested. 
* **Incidence angle.** Over flat terrain, backscatter has only a small trend with incidence angle. This trend is smaller than for the other workflows that we tested. 
* **Steep terrain.** Use the layover and shadow mask. Between local incidence angles of approximately 20° and 70°, terrain effects are small. Above approximately 70°, bright artefacts can occur along ridgelines where the DEM and the radar geometry do not align. 
* **Image quality.** Adaptive multilooking (Shiroma et al., 2022) gives sharper images than fixed-window multilooking, but more speckle at fine pixel spacing. 

## Quality assurance 

* **CEOS ARD.** The product was assessed against the CEOS ARD Normalised Radar Backscatter Product Family Specification (v1.3.1). 
* **Workflow evaluation.** GA and CSIRO compared five open workflows over Australia and Antarctica for geolocation, radiometric, terrain and image quality. OPERA-ISCE3 gave the best geolocation and image quality, and GA selected it. The report is in preparation. 
* **Corner reflector validation.** The results in this document. GA will repeat this validation on 20 m production products. 
* **‘Gold tile comparisons’.** Each software change processes reference scenes and compares the outputs with accepted benchmark products. The test must pass before a change is released. 
* **Metadata and operations.** STAC metadata is validated before publication. A dashboard monitors processing success, and failed jobs are kept for review. 
* **Upstream validation.** NASA JPL calibration and validation of OPERA RTC-S1 supports the algorithm. 

## Caveats for the current results 

* **Pixel spacing and DEM.** Test products have 10 m pixels and use Copernicus GLO-30 everywhere. Production has 20 m pixels and uses REMA v2 in Antarctica. 
* **Sample size.** Surat Basin has 7 scenes from one ascending track. The Antarctic and Yarragadee sites have one CR and 2–3 scenes each. 
* **Antarctic positions.** The CRs are measured in the native EPSG:3031 grid. The analysis code converts the positions to UTM with the axes in the wrong order. The values in this document are calculated again from the native positions, in the UTM zone of each CR. 
* **CR reference positions.** The survey reference (apex or ground), epoch and height datum are not yet confirmed. The Australian plate moves approximately 7 cm per year. 
* **Radiometric results.** Radiometric and terrain results are qualitative until we correct the analysis (statistics calculated in dB). 



% :::{dropdown} 1 Jan 2020: Example issue
% :open:
%
% This uses the `:open:` option because it is an open issue.
% :::

