# This script can be used to generate the 'Bands table' metadata that is displayed in the Specifications tab of product pages. Data is fetched from the Datacube and then is outputted in the correct YAML format which can be copy-pasted into the product's '_specifications.yaml' file. The resulting YAML output will require additional manual editing, e.g. replacing "placeholder" text with correct band descriptions.
# Note: This script is designed to be run in the DEA Sandbox environment.

import sys
import ruamel.yaml
import datacube
import numpy as np
import pandas as pd

# Connect to datacube and return measurements
dc = datacube.Datacube()
products_df = dc.list_measurements()

# Product and product-level values
product_name = "ga_s2ls_intertidal_cyear_3"
resolution = "10 m"
crs = "EPSG:3577"
description = "placeholder"

# Select specific product and prepare data
product_df = (
    products_df.loc[product_name]
    .drop(["flags_definition"], axis=1)
    .assign(resolution=resolution, crs=crs, description=description)
    .rename({"dtype": "type"}, axis=1)
    .reset_index(drop=True)
)[["name", "aliases", "resolution", "crs", "nodata", "units", "type", "description"]]

# Customise column formats/nodata
product_df["nodata"] = product_df["nodata"].fillna("NaN")
product_df["aliases"] = product_df["aliases"].fillna("").apply(list)
product_df["units"] = (
    product_df["units"].str.upper().str[0] + product_df["units"].str[1:]
)
product_df["description"] = (
    product_df["description"].str[0].str.upper() + product_df["description"].str[1:]
)

# Convert to a dictionary
bands_table = product_df.to_dict("records")
data = {"bands_table": bands_table}

# Convert dictionary to YAML
yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml_data = yaml.dump(data, sys.stdout)
print(yaml_data)
