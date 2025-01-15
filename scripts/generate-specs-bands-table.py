# This script can save you time by generating the 'Bands table' metadata that is displayed in the Specifications tab of product pages on the DEA Knowledge Hub. E.g. https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/?tab=specifications

# How to use this script:

# 1. In the 'CONFIGURATION' dictionary, change the 'product_id' to the Product ID of the relevant product. Ensure that this is correct, as it will be used to select metadata from the Datacube.
# 2. Run this script in the DEA Sandbox and it will print YAML output.
# 3. Copy the output and paste it into the '_tables.yaml' file of the relevant product. E.g. https://github.com/GeoscienceAustralia/dea-knowledge-hub/blob/main/docs/data/product/dea-intertidal/_tables.yaml
# 4. Edit the YAML as needed. It is recommended to write a brief description for each band.

import sys
import yaml
import datacube
import numpy as np
import pandas as pd

# Configure these values before running the script

CONFIGURATION = {
    "product_id": "ga_ls5t_gm_cyear_3",
}

# Fetch measurements of all products from the Datacube

dc = datacube.Datacube()

products_df = dc.list_measurements()

# Select specific product and format data

try:
    products_df.loc[CONFIGURATION["product_id"]]
except Exception as e:
    print(f"The product {CONFIGURATION['product_id']} was not found in the Datacube.")
    exit(1)

product_df = (
    products_df.loc[CONFIGURATION["product_id"]]
    .drop(["flags_definition"], axis=1)
    .assign(resolution=None, description=None)
    .rename({"dtype": "type"}, axis=1)
    .reset_index(drop=True)
)[["name", "aliases", "resolution", "nodata", "units", "type", "description"]]

# Change the format of certain columns and the 'no data' values

product_df["nodata"] = product_df["nodata"].fillna("NaN").infer_objects(copy=False)

product_df["aliases"] = product_df["aliases"].fillna("").infer_objects(copy=False).apply(list)

product_df["units"] = (
    product_df["units"].str.upper().str[0] + product_df["units"].str[1:]
)

product_df.loc[product_df["units"] == "1", "units"] = None

# Load a single dataset

dss = dc.find_datasets(product=CONFIGURATION['product_id'], limit=1)[0]

# Extract grids used across dataset, and resolution from grid transform

grid_dict = {k:int(v["transform"][0]) for k, v in dss.metadata_doc["grids"].items()}

# For each band, cross-reference to grid dataset, using "default" grid if not available 

band_resolutions = []
for band_name in product_df.name:
    grid_name = dss.measurements[band_name].get("grid", "default")
    band_resolutions.append(grid_dict[grid_name])

# Add resolutions back into dataframe

product_df["resolution"] = band_resolutions
product_df 

# Convert to a dictionary

bands_table = product_df.to_dict("records")

data = {"bands_table": bands_table}

# Print as YAML

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

yaml_data = yaml.dump(data, Dumper=IndentDumper, default_flow_style=False, sort_keys=False)

print(yaml_data)
