# Digital Earth Australia Tech Alerts and Changelog

% If status = green, class = tip
% All DEA systems are working as expected. There are no outstanding incidents or errors to report.
% See the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/). 
% If status = yellow, class = caution
% If status = red, class = danger

:::{admonition} DEA system status: green
:class: tip
The [DEA Hotspots historical file - "all-data"](https://hotspots.dea.ga.gov.au/files/historic) is currently not being updated. 
We are working on a resolution and the data will be backdated once a fix has been put in place.

All other DEA systems are working as expected. See the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/). 
:::

:::{admonition} DEA Sentinel-2 contiguity fix: ongoing
:class: note

See [alert dated 2024-01-10](./#20240110) for more details.
:::

## 2024-01-24: Water Observations and Fractional Cover Percentiles 2023 annual summaries released

See [DEA Water Observations Statistics (Landsat)](/data/product/dea-water-observations-statistics-landsat/?tab=history) 
and [DEA Fractional Cover Percentiles (Landsat)](/data/product/dea-fractional-cover-percentiles-landsat/) for more information. 

{#20240110}
## 2024-01-10: Sentinel-2 contiguity fix - Reprocessing commenced

Reprocessing to fix the Sentinel-2 contiguity issue has commenced with expected completion in early 2024. The issue 
was caused by anomalies in ESA Level 1 source data.

A [known Sentinel-2 contiguity issue](https://communication.ga.gov.au/link/id/zzzz659dea46b27d5565Pzzzz61de67bd94bfe861/page.html) 
created by ESA Level 1 anomalies (“[Striping due to lost source packets](https://communication.ga.gov.au/link/id/zzzz659dea46b3858302Pzzzz61de67bd94bfe861/page.html)”) 
is impacting approximately 0.5% of our Sentinel-2 Analysis Ready Data (S2 ARD) between 2015 and 2023. 

Affected products: 
* ARD Sentinel-2 products (ga_s2am_ard_3, ga_s2bm_ard_3)  

See [DEA Tech alert email](https://communication.ga.gov.au/link/id/zzzz659df9f7f306b556Pzzzz61de67bd94bfe861/page.html) for more information. 
Click [here](https://communication.ga.gov.au/link/id/zzzz659de7f165049054Pzzzz61de67bd94bfe861/page.html) to subscribe to DEA Tech alert emails.

## 2023-11: Release of version 0.3.0 of DEA Tools

Major update to the [DEA Tools Python package](https://docs.dea.ga.gov.au/notebooks/Tools/), including new tools for:
* [pansharpening Landsat data](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Pansharpening.html)
* [tide modelling](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Tidal_modelling.html)
* [sunglint masking](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Sunglint_masking.html)
* [interactive mapping](https://docs.dea.ga.gov.au/notebooks/Interactive_apps/README.html)
* [spatial operations](https://docs.dea.ga.gov.au/notebooks/Tools/gen/dea_tools.spatial.html)

... in addition to 14 new and updated Jupyter notebooks. See [version 0.3.0 release notes](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/0.3.0) for more detail.

## 2023-08: New notebooks, features and documentation

* Added a new [DEA Wetlands Insight Tool notebook](https://docs.dea.ga.gov.au/notebooks/DEA_products/DEA_Wetlands_Insight_Tool.html)
* Notebooks for [loading data from Microsoft Planetary Computer](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Planetary_computer.html)
* Enhanced [DEA Tools Python Package API documentation](https://docs.dea.ga.gov.au/notebooks/Tools/)
* Improved interactive widget functionality for satellite image export and animations

