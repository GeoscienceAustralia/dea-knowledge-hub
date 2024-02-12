% ## Accuracy

## Quality assurance

### QA enumeration 

To assist with the downstream calculation of the [DEA Mangrove Canopy Cover](/data/product/dea-mangrove-canopy-cover-landsat/) product, each pixel has an additional enumeration associated with it: 

* **0** - Not enough observations to calculate percentiles (less than 3 clear and dry observations), and there is at least one observation that has been identified as wet. Defined in ODC configuration as: insufficient observations wet. 
* **1** \- Not enough observations to calculate percentiles (less than 3 clear and dry observations), but never identified as wet. Defined in ODC configuration as: insufficient observations dry. 
* **2** \- There are sufficient observations to compute percentiles (3 or more clear and dry observations). Defined in ODC configuration as: sufficient observations 

This enumeration assists in quantifying uncertainty within the [DEA Mangrove Canopy Cover](/data/product/dea-mangrove-canopy-cover-landsat/) (see Mangrove Canopy Cover definition). 

### Side car files 

Collection 3 Fractional Cover Percentiles will be accompanied by the following metadata, presentation and quality assurance side car files: 

* `*.odc-metadata.yaml`: EODatasets 3 compatible ODC dataset definition
* `*.odc-proc-info.yaml`: Listing of python libraries and versions used by software to generate
* `*.sha1`: Cryptographic hash of data to validate distributed data
* `*.thumbnail.jpg`: Quick look thumbnail of a scaled RGB rendering of R = `bs_pc_50`, G= `pv_pc_50` and B = `npv_pc_50`
* `*.stac-item.json`: STAC 1.0.0 STAC document 
