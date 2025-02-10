## Accuracy

For information on the accuracy of the algorithms for test locations, see Zhu and Woodcock (2012) and Zhu, Wang and Woodcock (2015).

## Limitations

### Fmask

Fmask has limitations due to the complex nature of detecting natural phenomena, such as cloud. For example, bright targets, such as beaches, buildings and salt lakes often get mistaken for clouds.

Fmask is designed to be used as an immediate/rapid source of information screening. The idea is that over a temporal period enough observations will be made to form a temporal likelihood. For example, if a feature is consistently being masked as cloud, it is highly probable that it is not cloud. As such, derivative processes can be created to form an information layer containing feature probabilities.

Edges and fringes of clouds tend to be more opaque and can be missed by the cloud detection algorithm. In this instance, applying a morphological dilation will grow the original cloud object and capture edges and fringes of clouds. However, it is important to note that other cloud objects could also be dilated. Be mindful of single-pixel objects that could grow to become large objects. Consider filtering out these small objects prior to analysis.

### s2cloudless

Compared to Fmask, one limitation of the s2cloudless algorithm is the lack of cloud shadow detection. Cloud detection without a thermal band in the Sentinel-2 MSI is difficult, so most of the caveats around the interpretation of the Fmask classification also applies here. However, the machine-learning approach offers some advantages over the traditional physics-based approach here, and the cloud probability layer may be utilized to tune the cloud mask to specific applications.

### Angular measurement and shadow classification

The Digital Elevation Model (DEM) is used for identifying terrain shadow, as well as producing incident and exiting angles. It is derived from the Shuttle Radar Topography Mission (SRTM) and produced with approximately 30 m resolution. As such, any angular measurements and shadow classifications are limited to the precision of the DEM itself. The DEM is known to be noisy across various locations, so to reduce any potential extrema, a Gaussian smooth is applied prior to analysis.

## Quality assurance

The first Cloud Mask Intercomparison eXercise (CMIX) validated the Fmask and the s2cloudless algorithms together with 8 other algorithms on 4 different test datasets. Both performed well (>85% average accuracy) among the single-scene cloud detection algorithms.

The calculation of the satellite and solar positional geometry datasets are largely influenced by the publicly available ephemeris data and whether the satellite has an on-board GPS, as well as the geographical information that resides with the imagery data and the metadata published by the data providers. The code to generate the geometry grids is routinely tested and evaluated for accuracy at >6 decimal places of precision.

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

