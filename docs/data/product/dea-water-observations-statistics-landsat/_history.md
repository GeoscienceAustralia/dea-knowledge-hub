## Changelog

### Latest updates

1. Water Observation Statistics (Annual) – This product was updated with the 2024 calendar year data in April 2025. 
2. Water Observation Statistics (Apr – Oct) – This product was updated with seasonal data (period: April 2024 to October 2024) in April 2025. 
3. Water Observation Statistics (Nov – Mar) – This product was updated with seasonal data (period: November 2024 to March 2025) in June 2025.

### Version 2.0.0 released

* **Breaking change: Shift in grid origin point** &mdash; The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south. Therefore, all tile grid references have been changed. For instance, a tile reference of `x10y10` has changed to `x28y25`. The tile grid references of all derivative products generated from 2024 onwards will also be changed; however, Analysis Ready Data products will not be affected.
* **Enhanced cloud masking to reduce noise** &mdash; An enhancement to cloud masking has reduced cloud and shadow noise. This enhancement (known as 'cloud buffering') involved cleaning cloud masks using a 6-pixel dilation on cloud and shadows. Note that some areas of very high surface reflectance (e.g. sand dunes and ocean areas) may exhibit worsened noise or data gaps, but these are infrequent occurrences with low impact.
* **Landsat 9 product** &mdash; Landsat 9 is processed from 2022 onwards.

### 2024-01-24: Water Observations 2023 annual summary released

Product id: `ga_ls_wo_fq_cyear_3`

To access the updated product, see the [Access tab](./?tab=access).

