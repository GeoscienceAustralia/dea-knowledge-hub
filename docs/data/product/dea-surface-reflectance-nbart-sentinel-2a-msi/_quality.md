## Accuracy

Atmospheric correction accuracy depends on the quality of aerosol data and total column water vapour available to determine the atmospheric profile at the time of image acquisition (Wang et al., 2009).

BRDF correction is based on low resolution imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS), which is assumed to be relevant to medium resolution imagery such as that captured by Sentinel-2A MSI. A single BRDF shape is applied to each Sentinel-2A tile and it does not account for changes in land cover. 

The algorithm assumes that BRDF effect for inclined surfaces is modelled by the surface slope and does not account for land cover orientation relative to gravity (as occurs for some broadleaf vegetation with vertical leaf orientation).

The accuracy of the terrain correction also depend on the quality, scale and spatial resolution of the DSM data used and the co-registration between the DSM and the satellite image (Li et al., 2013). At present, 30 m resolution SRTM DSM data were used for the correction.

The algorithm depends on several auxiliary data sources:
* Availability of relevant MODIS BRDF data
* Availability of relevant aerosol data
* Availability of relevant water vapour data
* Availability of relevant DSM data
* Availability of relevant ozone data

Improved or more accurate sources for any of the above listed auxiliary dependencies will also improve the surface reflectance result.

## Quality assurance

Results from the DEA Cal/Val workflow over 17 data takes from 9 field sites were created based on both BRDF Collections 5 and 6.

The results for each collection were averaged and then compared. The comparison showed small changes in individual field sites, but overall there was no significant difference in the average results over all field sites to within 1% at most.

The technical report containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available: [DEA Analysis Ready Data Phase 1 Validation Project: Data Summary](http://pid.geoscience.gov.au/dataset/ga/145101)

## Known Issues

:::{dropdown} 26 Sep 2024: 's2cloudless' ARD reprocessing underway
:open:

We have begun reprocessing the older Sentinel-2 ARD data that was impacted by a bug in the s2cloudless cloud masking layer. The bug is '[24 May 2024: Misclassification issue with Sentinel-2 ‘s2cloudless’ cloud masking from 2022](#may-2024-misclassification-issue-with-sentinel-2-s2cloudless-cloud-masking-from-2022)'.

The addition of an offset factor in ESA's Sentinel-2 L1C Processing Baseline 4.0.0 [on January 25 2022](https://sentiwiki.copernicus.eu/web/s2-processing) led to the generation of incorrect `s2cloudless` cloud classifications in our systems. This resulted in an over-classification of cloud, particularly over bare and agricultural regions.

Sentinel-2 `s2cloudless` data from 25 January 2022 to 7 June 2024 is affected, and we expect to replace these datasets over the next several months.

In the meantime, we advise the users to avoid using `s2cloudless` for cloud masking on data between these two dates, and consider using the `Fmask` cloud mask as a temporary alternative during this period.
:::

:::{dropdown} 24 May 2024: Misclassification issue with Sentinel-2 's2cloudless' cloud masking from 2022
:open:

An issue has been identified that is causing widespread misclassification of clouds in DEA's Sentinel-2 `s2cloudless` cloud mask data generated since January 2022. 

We recommend that you avoid using `s2cloudless` cloud mask data from 2022 onwards until this issue is investigated. 
:::

:::{dropdown} 25 Oct 2023: Removing Sentinel-2 Level 1 and ARD duplicates (Resolved)

Duplicate Sentinel-2 Level 1 (s2 l1) and Analysis Ready Data (ARD) has been discovered. The duplicate groups have the same region code and datetime attribute.

**Background**

Remediation will require archiving the duplicate scenes of our Sentinel-2 Level 1 (s2 l1) and Analysis Ready Data (ARD) products.

Which Products are affected?

* S2b
* S2a

**What does this mean for DEA Users?**

This is expected to have minimal impact on users.

If you have any further questions or encounter issues, please contact <earth.observation@ga.gov.au>

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz65384bbe2a28c901Pzzzz61de67bd94bfe861/page.html)
:::

:::{dropdown} Aug 2023: Sentinel-2 ARD GQA coastal scenes error; DEA Burnt Area (S2 NRT, Provisional) decommissioning (Resolved)

**Sentinel-2 ARD error &mdash; GQA failing over coastal scenes**

Many Sentinel-2 Analysis Ready Data (ARD) coastal scenes up until March 2023 were produced without geometric quality assessment (GQA) information.

This error was found and fixed in the ARD processing code, however there are data errors present within existing coastal ARD produced prior to March 2023.

**Background**

GQA (Geometric Quality Assessment) metadata provides information about the georeferencing accuracy of each satellite observation.

Sentinel-2 ARD coastal scenes produced before March 2023 are missing GQA information, leading to low quality ARD outputs.

To correct the issue, we plan to archive and remove 26,037 Sentinel-2 ARD coastal scenes that have no GQA data.

Archiving and removing the scenes with no GQA will lead to good ARD being produced.

**Which Products are affected?**

* 'ga_s2am_ard_3'
* 'ga_s2bm_ard_3'
* Affected scene regions: '56JNR', '53HMC', '52HDK', '50KQD', '50HQG', '52LEL', '55GDM', '54HUE', '56HLG', '51HWC', '53HKE', '52HCK', '56JNP', '50HLG', '52LCK', '53LQG', '52LFM', '52HGK', '55GBQ', '54HVC', '56JNQ', '55HFU', '49KHS', '55HGU', '50HNG', '50HPG', '53LLH', '56HLH', '55GEM', '50HMG', '52LEK', '54HUD'

**What does this mean for DEA Users?**

Coastal ARD scenes before March 2023 that have no GQA data will be temporarily unavailable. They will be replaced with new ARD scenes with GQA data.

Users who have previously accessed Sentinel-2 ARD over coastal areas and filtered by GQA may wish to re-run their workflows to account for the updated data.

If you have any questions about the above, please email us at <earth.observation@ga.gov.au>

[View the Tech Alert](https://communication.ga.gov.au/pub/pubType/EO/pubID/zzzz64dc2b594744b162/interface.html)

:::

