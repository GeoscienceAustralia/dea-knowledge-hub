# Digital Earth Australia Tech Alerts and Changelog

% If status = green, class = tip
% If status = yellow, class = caution
% If status = red, class = danger

:::{admonition} DEA system status: green
:class: tip

All DEA systems are working as expected. There are no outstanding incidents or errors to report.
:::


:::{admonition} DEA Sentinel-2 continguity fix: ongoing
:class: note

See [alert dated 2024-01-10](#Jan102024) for more details.
:::

(Jan102024)=
## 2024-01-10 Sentinel-2 contiguity fix - Reprocessing commenced

Reprocessing to fix the Sentinel-2 contiguity issue has commenced with expected completion in early 2024. The issue 
was caused by anomalies in ESA Level 1 source data.

A [known Sentinel-2 contiguity issue](https://communication.ga.gov.au/link/id/zzzz659dea46b27d5565Pzzzz61de67bd94bfe861/page.html) 
created by ESA Level 1 anomalies (“[Striping due to lost source packets](https://communication.ga.gov.au/link/id/zzzz659dea46b3858302Pzzzz61de67bd94bfe861/page.html)”) 
is impacting approximately 0.5% of our Sentinel-2 Analysis Ready Data (S2 ARD) between 2015 and 2023. 

Affected products: 
* ARD Sentinel-2 products (ga_s2am_ard_3, ga_s2bm_ard_3)  

See [DEA Tech alert email](https://communication.ga.gov.au/link/id/zzzz659df9f7f306b556Pzzzz61de67bd94bfe861/page.html) for more information. 
Click [here](https://communication.ga.gov.au/link/id/zzzz659de7f165049054Pzzzz61de67bd94bfe861/page.html) to subscribe to DEA Tech alert emails.

## 2023-11 Release of version 0.3.0 of DEA Tools

Major update to the [DEA Tools Python package](https://docs.dea.ga.gov.au/notebooks/Tools/index.html), including new tools for:
* [pansharpening Landsat data](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Pansharpening.html)
* [tide modelling](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Tidal_modelling.html)
* [sunglint masking](https://docs.dea.ga.gov.au/notebooks/How_to_guides/Sunglint_masking.html)
* [interactive mapping](https://docs.dea.ga.gov.au/notebooks/Interactive_apps/README.html)
* [spatial operations](https://docs.dea.ga.gov.au/notebooks/Tools/gen/dea_tools.spatial.html)

... in addition to 14 new and updated Jupyter notebooks. See [version 0.3.0 release notes](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/0.3.0) for more detail.

:::{dropdown} 2023-08-11 Small systems updates

Technical DEA internals which have changed in the last week.
* Some tweaks to DEA Sandbox DNS resolution last Friday.
* The URL https://explorer.dea.ga.gov.au/ will be changed to show data in the DEA AWS data holdings instead of the NCI holdings.
* Some data gap filling of Landsat 8 ARD, Landsat 8 FC and Landsat 8 WO for 2023.
* Reduced the delay between Sentinel 2 ARD data being produced (on the NCI), and being delivered to AWS. It was *up to 48 hours* and should now be *up to 24 hours*.
:::

:::{dropdown} 2021-07-16 Collection 3 Landsat data now available

Thanks to the [Geoscience Australia Landsat Collection Upgrade (video)](https://www.youtube.com/watch?v=BNEIG91lu44), 
our data catalogue now includes Collection 3 data for DEA Surface Reflectance, also available through [OWS](https://ows.dea.ga.gov.au/). 
Other Collection 3 products will soon follow, including DEA Water Observations (WOfS), and DEA Fractional Cover.
 
[DEA Notebooks](https://github.com/GeoscienceAustralia/dea-notebooks/) and the [User Guide](/notebooks/Beginners_guide/README/) 
have been updated with Collection 3 code examples to reflect the upgrade, and our Content Management Interface and 
[DEA Maps platforms](https://maps.dea.ga.gov.au/) are also being updated.
 
Users of Collection 2 are encouraged to use Collection 3 data.
A staged decommissioning of Collection 2 is underway and will continue into 2022.
Questions can be raised to dea@ga.gov.au.
:::

:::{dropdown} 2021-04-15 New user guide: accessing data via AWS

Added a new guide to accessing DEA data via [Amazon Web Services](/guides/setup/AWS/data_and_metadata/).
:::

:::{dropdown} 2020-01-09 DEA Notebooks updates

The [DEA Notebooks repository](https://github.com/GeoscienceAustralia/dea-notebooks/) and the DEA user guide received a 
[major update](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/notebooks_refresh) which includes a 
simplified directory structure and set of improved and easier to use Jupyter notebooks.

These updated notebooks include a new Beginner's Guide aimed at introducing users to DEA and the Open Data Cube. To view these
new notebooks, navigate to the [Beginner's Guide](/notebooks/Beginners_guide/README/) section of the User Guide.
:::

:::{dropdown} 2019-03-12 Changes to NCI project codes

Users are now required to join all projects containing data they wish to use. Before this change
all the DEA data was public to NCI users without any further steps.
:::

:::{dropdown} 2018-02-28 Update to `dea` environment module
* Rename module to `dea`. Most people should now run

```bash

     module use /g/data/v10/public/modules
     module load dea
```
* Include [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) as an alternative to Jupyter Notebooks. To use, from a shell run

```bash

     jupyter-lab
```
* Include pre-release version 1.6 of Open Data Cube
* Drop support for Python 2
:::
