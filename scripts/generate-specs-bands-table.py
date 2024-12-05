# This script can save you time by generating the 'Bands table' metadata that is displayed in the Specifications tab of product pages on the DEA Knowledge Hub. E.g. https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/?tab=specifications

# How to use this script:

# 1. In the 'CONFIGURATION' dictionary, change the 'product_id' to the Product ID of the relevant product. Ensure that this is correct, as it will be used to select metadata from the Datacube.
# 2. In the 'CONFIGURATION' dictionary, edit the 'resolution' according to the resolution of the product. This will be copied to all bands in the YAML output, but it can be edited manually in the YAML.
# 3. Run this script in the DEA Sandbox and it will print YAML output.
# 4. Copy the output and paste it into the '_tables.yaml' file of the relevant product. E.g. https://github.com/GeoscienceAustralia/dea-knowledge-hub/blob/main/docs/data/product/dea-intertidal/_tables.yaml
# 5. Edit the YAML as needed. It is recommended to write a brief description for each band.

import sys
import yaml
import datacube
import numpy as np
import pandas as pd

# Configure these values before running the script

CONFIGURATION = {
    "product_id": "ga_s2ls_intertidal_cyear_3",
    "resolution": "10 m"
}

# Fetch measurements of all products from the Datacube

dc = datacube.Datacube()

products_df = dc.list_measurements()

# Select specific product and format data

product_df = (
    products_df.loc[CONFIGURATION["product_id"]]
    .drop(["flags_definition"], axis=1)
    .assign(resolution=CONFIGURATION["resolution"], description=None)
    .rename({"dtype": "type"}, axis=1)
    .reset_index(drop=True)
)[["name", "aliases", "resolution", "nodata", "units", "type", "description"]]

# Change the format of certain columns and the 'no data' values

product_df["nodata"] = product_df["nodata"].fillna("NaN")

product_df["aliases"] = product_df["aliases"].fillna("").apply(list)

product_df["units"] = (
    product_df["units"].str.upper().str[0] + product_df["units"].str[1:]
)

# Convert to a dictionary

bands_table = product_df.to_dict("records")

data = {"bands_table": bands_table}

# Convert to YAML

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

yaml_data = yaml.dump(data, Dumper=IndentDumper, default_flow_style=False, sort_keys=False)

print(yaml_data)
