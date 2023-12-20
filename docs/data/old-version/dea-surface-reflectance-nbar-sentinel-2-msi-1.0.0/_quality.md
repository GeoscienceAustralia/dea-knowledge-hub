## Accuracy

Atmospheric correction accuracy is dependent on the quality of aerosol data available to determine the atmospheric profile at time of image acquisition.

BRDF correction is based on low resolution imagery (MODIS) which is assumed to be relevant to medium resolution imagery such as Sentinel 2 MSI. BRDF correction is applied to each whole Sentinel 2 MSI tiles and does not account for changes in land cover. It also excludes effects due to topographic shading and local BRDF. This algorithm is dependent on the availability of relevant MODIS BRDF data.

Topographic shading correction algorithm is designed for medium resolution imagery and assumes that hill slopes are resolved by the sensor system (Li et al., 2012). The algorithm assumes that: a. BRDF effect for inclined surfaces is modelled by the surface slope and does not account for land cover orientation relative to gravity (as occurs for some broad leaf vegetation with vertical leaf orientation).

## Quality assurance

### Atmospheric and BRDF Correction

The algorithm was validated using Landsat data. As detailed in Li et al. (2010), the atmospheric and BRDF correction algorithm was validated in three parts:

1) Validate combined atmospheric and surface BRDF correction using field reflectance measurements at two very different sites, Gwydir, NSW, and Lake Frome, SA - correlation (measured as r) between corrected image values and field data was >0.95.
2) Validate surface BRDF correction using data from image overlap areas of adjacent paths acquired one week apart in northeast Queensland - normalised reflectance factor was very close in corrected images, but not in original images, and difference in reflectance factor values between corrected and uncorrected images can be >0.05.
3) Cross-validate Landsat TM data for accuracy of spectral reflectance using the MODIS reflectance product for Lake Frome correlation (measured as r2) between correctedÂ Landsat TM image values and MODIS reflectance product was 0.93-0.97 in all bands except Landsat TM band 5, which was 0.90.

The results clearly show that the algorithm can remove most of the BRDF effect without empirical adjustment and that cross-calibration between the Landsat ETM+ and MODIS sensors is achievable.

