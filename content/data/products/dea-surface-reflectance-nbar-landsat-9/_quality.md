## Accuracy

Atmospheric correction accuracy depends on the quality of aerosol data available to determine the atmospheric profile at the time of image acquisition.

BRDF correction is based on low resolution imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS), which is assumed to be relevant to medium resolution imagery such as that captured by Landsat 9 OLI-TIRS. BRDF correction is applied to each whole Landsat 9 OLI-TIRS scene and does not account for changes in land cover. It also excludes effects due to topographic shading and local BRDF.

The algorithm assumes that BRDF effect for inclined surfaces is modelled by the surface slope and does not account for land cover orientation relative to gravity (as occurs for some broadleaf vegetation with vertical leaf orientation).

The algorithm also depends on several auxiliary data sources:

*   Availability of relevant MODIS BRDF data
*   Availability of relevant aerosol data
*   Availability of relevant water vapour data
*   Availability of relevant DEM data
*   Availability of relevant ozone data

Improved or more accurate sources for any of the above listed auxiliary dependencies will also improve the surface reflectance result.

## Quality assurance

Results from the DEA Cal/Val workflow over 17 data takes from 9 field sites were created based on both BRDF Collections 5 and 6.

The results for each collection were averaged and then compared. The comparison showed small changes in individual field sites, but overall there was no significant difference in the average results over all field sites to within 1% at most.

The technical report containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available: [DEA Analysis Ready Data Phase 1 Validation Project : Data Summary](https://doi.org/10.26186/145101)

