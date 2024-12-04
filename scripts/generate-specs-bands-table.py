# This script can be used to generate the 'Bands table' metadata that is displayed in the Specifications tab of product pages. Data is fetched from the Datacube and then is outputted in the correct YAML format which can be copy-pasted into the product's '_specifications.yaml' file. The resulting YAML output will require additional manual editing, e.g. replacing "placeholder" text with correct band descriptions.
# Note: This script is designed to be run in the DEA Sandbox environment.

import sys
from ruamel.yaml import YAML
import datacube
import numpy as np
import pandas as pd

# Important: Configure these values depending on the product
CONFIGURATION = {
    "product_name": "ga_s2ls_intertidal_cyear_3",
    "resolution": "10 m"
}

# Connect to datacube and return measurements
dc = datacube.Datacube()
products_df = dc.list_measurements()

# Select specific product and prepare data
product_df = (
    products_df.loc[CONFIGURATION["product_name"]]
    .drop(["flags_definition"], axis=1)
    .assign(resolution=CONFIGURATION["resolution"], description=None)
    .rename({"dtype": "type"}, axis=1)
    .reset_index(drop=True)
)[["name", "aliases", "resolution", "nodata", "units", "type", "description"]]

# Customise column formats/nodata
product_df["nodata"] = product_df["nodata"].fillna("NaN")
product_df["aliases"] = product_df["aliases"].fillna("").apply(list)
product_df["units"] = (
    product_df["units"].str.upper().str[0] + product_df["units"].str[1:]
)

# Convert to a dictionary
bands_table = product_df.to_dict("records")
data = {"bands_table": bands_table}

# Convert dictionary to YAML
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.dump(data, sys.stdout)

