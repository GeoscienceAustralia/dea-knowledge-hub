## Changelog

**This Collection 3 (C3) product** and has been created by reprocessing Collection 1 (C1) and making improvements to the processing pipeline and packaging.

Packaging updates include:  
* Open Data Cube (ODC) eo3 metadata  
* metadata includes STAC fields to enable users to filter by fields such as tile ID or cloud cover percentage in applications such as ODC  
* additional STAC metadata file in JSON format  
* directory structure and file names that are consistent with Geoscience Australia’s Landsat C3 products.  

Additional updates include:
* upgrading the spectral response function to result in a more accurate product. These new versions include minor updates, slight changes of the central wavelengths for band B02 of S2A and S2B, and band B01 of S2B, along with slight changes of the Full Width Half Maximum (FMWH) for most of the bands  
* correction of solar constant errors in the conversion between reflectance and radiance as well as in the atmospheric correction  
* an additional cloud mask layer (s2cloudless)  
* removal of NBAR layers  
* reduced spatial resolution of observation attribute layers to 20m resolution, with the contiguity layer being maintained at 10m  
* additional of GQA information to dataset metadata  
* removal of buffering from fmask layer  
* BRDF ancillary upgraded from MODIS BRDF C5 to MODIS BRDF C6  
* Upgrading from MODTRAN 5.2 to MODTRAN 6.


