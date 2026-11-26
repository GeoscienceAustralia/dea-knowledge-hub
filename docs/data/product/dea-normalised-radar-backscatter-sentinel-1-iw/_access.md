% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/services/dea-knowledge-hub/operating-procedures/product-metadata-fields/#kh-product-metadata-fields

% :::{dropdown} How to access the data
%
% Example content
% :::

## Accessing this data

This product is available through the DEA public data store. Use the collection that matches the polarisation required for your analysis. 

* [ga_s1_nrb_iw_vv_1/](https://data.dea.ga.gov.au/?prefix=baseline/ga_s1_nrb_iw_vv_1/) 
* [ga_s1_nrb_iw_vv_vh_1/](https://data.dea.ga.gov.au/?prefix=baseline/ga_s1_nrb_iw_vv_vh_1/) 
* [ga_s1_nrb_iw_hh_1/](https://data.dea.ga.gov.au/?prefix=baseline/ga_s1_nrb_iw_hh_1/) 
* [ga_s1_nrb_iw_hh_hv_1/](https://data.dea.ga.gov.au/?prefix=baseline/ga_s1_nrb_iw_hh_hv_1/) 
* [ga_s1_nrb_iw_static_1/](https://data.dea.ga.gov.au/?prefix=baseline/ga_s1_nrb_iw_static_1/) 

## Using the data 

Backscatter is supplied in linear power. To convert valid positive values to decibels, use `10 × log10(backscatter)`. Apply the layover/shadow mask before analysis. Static layers can be used to convert `gamma0` to `beta0` or `sigma0`. 

All acquisitions of the same burst are placed on the same grid. This allows a time series to be created without additional image-to-image alignment. Regional analyses may require multiple bursts to be selected and mosaicked. 

*Under construction*
We have notebooks [here](https://github.com/eloise-b/de-sar-sample-data).
