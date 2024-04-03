# DEA ARD processing extent

DEA produces surface reflectance products from Landsat and Sentinel-2 satellite observations which cover the continent and some near-shore islands of Australia. This data is used to produce derivative products such as DEA Coastlines, Water Observations, and Fractional Cover.

We are extending our baseline satellite data to include Christmas Island, Cocos (Keeling) Islands, Coral Sea Islands, Heard and McDonald Islands, Norfolk Island and Islands in the Torres Strait. Additionally, we are processing imagery over shallow Ocean to support bathymetry and oceanography science.

The new data was requested by and will support Indigenous Communities in the Torres Straits in addition to Government agencies who seek to report on Ocean Ecosystem Accounts and manage the full extent of our Marine Parks. 

The update will support the expansion of [DEA's Summary Product Grid](https://knowledge.dea.ga.gov.au/guides/reference/collection_3_summary_grid/), including a shift in the origin point to the south-west of its current position. The expanded Area of Interest will support several DEA product releases and version updates throughout 2024.

## List of locations

Here is the new full list of locations that are supported.

:::{list-table}
:header-rows: 1

* - Region
  - Scenes / Tiles
* - Heard Island and MacDonald Islands
  - 134-097, 135-097, 136-097, 43FDA, 43FDB, 43FCB, 43FCA 
* - Lord Howe Island
  - 084-082, 085-082, 59JKJ, 58JGP, 59JKH, 58JGN 
* - MacQuarie Island
  - 080-098, 079-098, 079-099, 57FWU, 57FWV, 57FVV, 57FWA, 57FVA, 57FVU 
* - Norfolk Island
  - 079-080, 080-080, 57JWF, 57JVF, 57HVE, 57HWE 
* - Chirstmas Island
  - 122-067, 123-067, 48LWP, 48LXP 
* - Cocos (Keeling) Island
  - 128-068, 128-069, 47LKG, 47LKH, 46LHN, 46LHM 
* - Talbot Islands, Dauan Island, Saibai Island and Boigu Island
  - 099-066 
* - Daru, Western Province Papua New Guinea and Northern Warrior Reefs
  - 098-066, 54LZR
* - Elizabeth Reef
  - 085-081, 57JVG, 57JWG 
* - Middleton Reef
  - 085-080, 57JVH, 57JWH 
* - Frederick Reef, Queensland
  - 088-075, 56KQB, 57KTS, 56KQA 
* - Coral Sea – Scenes with Ocean depth less than 200m
  - 089-072, 088-074, 088-076, 54LZL, 55KEA, 55KFV, 55KGA, 55KGV, 55KHA, 55KHT, 55KHU, 55LBF, 55LBJ, 55LBK, 55LCJ, 55LDC, 55LDE, 56KKC, 55KKD, 56KKF, 56KLC, 56KMV, 56KNU, 56KQA, 56KQB, 56KQF, 56KQG, 56KQV, 56KRB, 56KRF, 56KRG, 57KTA, 57KTB, 57KTS, 57KTS 
* - Gulf of Carpentaria
  - 101-069, 53LRC, 54LTH 
* - Arafura Sea
  - 102-067, 104-067, 106-067, 107-068, 107-069, 52LEM, 52LEN, 52LFP, 52LHP, 53LLJ, 53LPJ, 53LQH, 53LQJ 
* - Timor Sea
  - 51LVD, 51LWD, 51LWF, 51LXE, 51LXF, 51LYF, 51LZF, 52LBL, 52LCL, 52LDK 
* - Indian Ocean
  - 116-075, 49HGB, 49HGC, 49JFL, 49KGS, 49KHT, 50HKG, 50HKH, 50HKJ, 50HMF, 50HNF, 50JKL, 50KKC 
* - Great Australian Bight
  - 52HBI, 52HEK, 52HFK, 53HKD, 53HLC, 53HNA 
* - Augusta, Western Australia
  - 113-084 
* - Tasman Sea
  - 089-088, 089-091, 090-091, 55GFM 
* - Bass Strait
  - 54HXB 

:::

## Quality and metadata 

The quality of ancillary inputs used in ARD generation in offshore locations is limited in comparison to the higher quality ancillary inputs used on continental Australia. Quality information for ancillary inputs is found in the `proc-info` (processing information) YAML metadata file within the dataset. The tier list is `USER`, `FALLBACK`, and `DEFINITIVE`, with the latter being the highest level of quality. Unfortunately, this information is not available to users via the datacube, so we have added an additional metadata tag to delineate data delivered in this update: `final_ancillaries = "nonstandard"`


```python
dc.find_datasets(product="ga_ls8c_ard_3", limit=10, final_ancillaries="nonstandard")
```

## Geometric quality assessment issues 

[ARD](/guides/about/glossary/#ard) is a Surface Reflectance product which is derived from USGS or ESA Level 1 products. The Level 1 product is geometrically corrected such that the product is 'ortho-rectified' which results in enabling acquisitions from different dates to be spatially overlaid for assessment through time. The ARD product provides a comprehensive quality assurance of geometric correction known as GQA, which is found in the dataset and processing information metadata.


This update features the addition of Landsat scenes and Sentinel 2 tiles over islands and reefs. Some of these islands, such as Christmas Island or islands south of Papua New Guinea, are at extreme high or low latitudes and are affected by persistent cloud. This presents challenges when correlating the reference image against source images to provide statistical geometric comparisons.


## BRDF quality issues 

[BRDF](/guides/about/glossary/#brdf) is a solar illumination correction which adjusts reflectance intensity in differing amounts in differing directions. The light that comes from the Sun, reflects off the Earth and is received by the sensor is adjusted based on viewing/solar angle geometries of MODIS data.

Sometimes over offshore locations we have found BRDF values to be unphysical. We have implemented a BRDF solution over the offshore locations, which screens out unphysical BRDF values and excludes them from the solar illumination correction.

## Water vapor 

No ancillary source dataset difference between mainland and offshore locations.

## Aerosol 

A constant value of 0.06 Aerosol Optical Depth (AOD) is used as ancillary input as we do not have aerosol data for these extended locations. This constant value is based on the assumption that the average AOD data in Australian continental is around the 0.05, but islands are surrounded by the sea and impacted by salt water particles, so setting AOD as 0.06 is reasonable.


## Ozone  

The Ozone constant value for ancillary input is set to 0.275 ATM-CM. Typically in the extended offshore locations, Ozone is around 0.25 to 0.3. Ozone does not impact radiometric values in bands (wavelengths) by a significant amount. 
