## Accuracy

Atmospheric correction accuracy depends on the quality of aerosol data available to determine the atmospheric profile at the time of image acquisition.

BRDF correction is based on low resolution imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS), which is assumed to be relevant to medium resolution imagery such as that captured by Landsat 5 TM. BRDF correction is applied to each whole Landsat 5 TM scene and does not account for changes in land cover. It also excludes effects due to topographic shading and local BRDF.

The algorithm assumes that BRDF effect for inclined surfaces is modelled by the surface slope and does not account for land cover orientation relative to gravity (as occurs for some broadleaf vegetation with vertical leaf orientation).

The algorithm also depends on several auxiliary data sources:

* Availability of relevant MODIS BRDF data
* Availability of relevant aerosol data
* Availability of relevant water vapour data
* Availability of relevant DEM data
* Availability of relevant ozone data

Improved or more accurate sources for any of the above listed auxiliary dependencies will also improve the surface reflectance result.

## Quality assurance

Results were compared with data gathered at two field sites, Lake Frome and Gwydir. The average RMSD was found to be 0.027 reflectance units.

The technical report containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available: [DEA Analysis Ready Data Phase 1 Validation Project : Data Summary](http://pid.geoscience.gov.au/dataset/ga/14510)

