DEA Naming Conventions (Collection 3) 
=====================================

.. contents:: In this guide
   :local:
   :backlinks: none

Introduction
------------

This page explains the naming convention of files/datasets found within Digital 
Earth Australia's (DEA)science data products as well as the 
Open Data Cube (ODC) science data product naming convention. 

DEA maintains and distributes collections of satellite-derived information 
sourced from a growing number of different satellite missions. The DEA Naming 
Conventions aim to make naming of data collections consistent across science 
data products and platforms. 

Diffterent types of Science Data Products
-----------------------------------------

Depending on the type of science data product, or from which satellite mission 
the data was sourced, science data products published by DEA come in three 
principle forms: 

- Baseline Analysis Ready Data (ARD) or surface reflectance. This can use the 
World Reference System (WRS-2) as its spatial reference if sourced from 
Landsat, or the Military Grid Reference System (MGRS) if sourced from 
Sentinel-2. 
- Derivative (of ARD) data that has a one-to-one correspondence of pixels and 
datasets to its parent ARD. This can use WRS-2 as its spatial reference if 
sourced from Landsat, or MGRS if sourced from Sentinel-2. 
- Derivative summary data, or a summary of a time period (monthly, seasonal, 
calendar year, financial year, all of available time). These will use the 
Collection 3 grid specification for its spatial reference. 

Science Data Product naming principles
--------------------------------------

Science data product names meet the following principles: 

1. Unique names/identifiers. 
2. Human readable.
3. Ease of navigation to enable spatio-temporal navigation and minimise number 
of directory levels.
4. Consistency terminology between different representations of the data.
5. Concise directory structure that provides logical context for each step.
6. Informative base filenames that provide what, when and where.
7. No redundant information in the filename.
8. Provides distinction between other providers of similar data.
9. Provides distinction between different instances of data (i.e. maturity levels. 
10. Provides distinction between different versions of a science data product.
11. Correct level of science data product abstraction.
12. Understand limitations on filesystems.
13. Works consistently between different platforms.
14. Directories must have less than 1000 items contained within.

Science Data Product versioning and naming
------------------------------------------

The product name consists of the organisation, platform/sensor, data science 
product code, collection number and version.  

ga_s2_fmc_3_v1  

The collection number is inherited from the base product that the data science 
product was derived from. For examples, derivative products which are produced 
using an Analysis Ready Data (ARD) science data product with a baseline of '3' 
will have a collection '3' in the product name.  

Major updates are represented by a version number being appended to the end of 
the science data product with a 'v'. These updates represent major changes and 
are backwards incompatible. The purpose of appending the version to the end of 
the science data product name is to prevent collisions in data management 
systems such as Open Data Cube (ODC).  

ga_s2_fmc_3_v1 
ga_s2_fmc_3_v2 
ga_s2_fmc_3_v3 

Path, Dataset versioning and naming
-----------------------------------

Dataset versioning will be included in the base part of the filename only, 
providing explicit clarity about its makeup, enabling a datafile to be 
standalone and self-describing. For example: 
• ga_s2_fmc_3_v1/55/HEC/2024/12/07/20241207T011213/ga_s2_fmc_3_v1-0-0_55HEC_2024-12-07_final_fmc.tif 
• ga_s2_fmc_3_v1 science data product name 
• 55/HEC spatial identifier (x then y) 
• 2024-12-07 acquisition date 
• 20241207T011213 datatake sensing start time 
• 0-0 dataset version identifier 

The dataset versioning identifier permits appending to an existing product when 
there’s a minor or patch increment due to an update in the algorithmic 
methodology and/or the compute environment. 

Science Data Products requiring a one-to-one relationship with data acquisitions
--------------------------------------------------------------------------------

An additional directory layer for including the DATATAKE_SENSING_START_TIME 
that enables more than one acquisition over a given region in a single solar 
day to be stored without collision. 

For future roll-outs, this DATATAKE_SENSING_START_TIME, or BURST_TIME for the 
SAR case, will also include this information in the base filename itself. 

Science Data Products not requiring a one-to-one relationship with data acquisitions
------------------------------------------------------------------------------------ 

Updates (whether that be compute environment, algorithmic, methodology etc) to 
a science data product that result in a significant difference given the same 
input, will result in a new science data product. This is considered a breaking 
change, and a bump in the major version identifier that is also carried across 
into the new science data product name. 

This enables concurrent access for any users/systems requiring use of the 
previous instance of the science data product. 

If the updated components of the algorithm and/or the compute environment 
produce an equivalent dataset (within tolerance) given the same input, there 
is no need to produce a new science data product, and appending to the existing 
data product can take place, albeit with a bump in the minor or patch 
increments of the dataset versioning. 


References
----------

-  `The Worldwide Reference 
   System <https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/>`__
-  `Wikipedia's article on the Military Grid Refrence
   System <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>`__
-  `DEA Summary Product Grid (Collection 3) </guides/reference/collection_3_summary_grid/>`__


