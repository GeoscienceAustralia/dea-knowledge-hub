% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

## 5 Dec 2018: DEA Public Data Changes

* Added Land/Sea mask GeoTIFFs to `/projects/geodata_coast_100k/`
* Updated CSV files in `/projects/WaterBodies/feature_info` with latest data, ISO timestamps, and changed column order.

## 12 Nov 2018: DEA Public Data Changes

* Update website components to match DEA styling.
* Change time to more readable format.
* Replace images.

## 6 Nov 2018: DEA Public Data Changes

- Updated CSV files in `/projects/WaterBodies/feature_info`

## 5 Nov 2018: DEA Public Data Changes

- Added `/Website`
- Updated `index.html` to improve user interface and experience.

## 11 Oct 2018: DEA Public Data Changes

- Added `/CHANGELOG.txt`
- Replaced `/geomedian-australia/v2.1.0/albers_grid.geojson` with a version using WGS84 coordinates, as per the GeoJSON specification.

## 28 Feb 2018: Update to 'dea' environment module

* Rename module to `dea`. Most people should now run the following commands from the terminal.
    ```bash
    module use /g/data/v10/public/modules
    module load dea
    ```
* Include [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) as an alternative to Jupyter Notebooks. To use, run this command from the terminal.
    ```bash
    jupyter-lab
    ```
* Include pre-release version 1.6 of Open Data Cube.
* Drop support for Python 2.

