% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

## Nov 2023: Release of version 0.3.0 of DEA Tools

Major update to the [DEA Tools Python package](https://knowledge.dea.ga.gov.au/notebooks/Tools/), including new tools for:

* [pansharpening Landsat data](https://knowledge.dea.ga.gov.au/notebooks/How_to_guides/Pansharpening.html)
* [tide modelling](https://knowledge.dea.ga.gov.au/notebooks/How_to_guides/Tidal_modelling.html)
* [sunglint masking](https://knowledge.dea.ga.gov.au/notebooks/How_to_guides/Sunglint_masking.html)
* [interactive mapping](https://knowledge.dea.ga.gov.au/notebooks/Interactive_apps/README.html)
* [spatial operations](https://knowledge.dea.ga.gov.au/notebooks/Tools/gen/dea_tools.spatial.html)

In addition, this update includes 14 new and updated Jupyter notebooks. See [version 0.3.0 release notes](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/0.3.0) for more detail.

## 25 Oct 2023: Removing Sentinel-2 Level 1 and ARD duplicates (Resolved)

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

## 11 Aug 2023: Small systems updates

Technical DEA internals which have changed in the last week.

* Some tweaks to DEA Sandbox DNS resolution last Friday.
* The URL [https://explorer.dea.ga.gov.au/](https://explorer.dea.ga.gov.au/) will be changed to show data in the DEA AWS data holdings instead of the NCI holdings.
* Some data gap filling of Landsat 8 ARD, Landsat 8 FC and Landsat 8 WO for 2023.
* Reduced the delay between Sentinel 2 ARD data being produced (on the NCI), and being delivered to AWS. It was *up to 48 hours* and should now be *up to 24 hours*.

## Aug 2023: New notebooks, features and documentation

* Added a new [DEA Wetlands Insight Tool notebook](https://knowledge.dea.ga.gov.au/notebooks/DEA_products/DEA_Wetlands_Insight_Tool.html)
* Notebooks for [loading data from Microsoft Planetary Computer](https://knowledge.dea.ga.gov.au/notebooks/How_to_guides/Planetary_computer.html)
* Enhanced [DEA Tools Python Package API documentation](https://knowledge.dea.ga.gov.au/notebooks/Tools/)
* Improved interactive widget functionality for satellite image export and animations

## Aug 2023: DEA Coastlines 2022 &mdash; New release

An updated version of DEA Coastlines is now available and includes the 2022 continental-wide data for Australia’s coastlines. This latest annual dataset builds on the Coastlines 2.0 release which included data for several offshore islands and exposed reefs not covered by previous versions.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz64dc26d23b947590Pzzzz61de67bd94bfe861/page.html)

## Mar 2023: Sentinel-2 ARD GQA coastal scenes error; DEA Burnt Area (S2 NRT, Provisional) decommissioning (Resolved)

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
