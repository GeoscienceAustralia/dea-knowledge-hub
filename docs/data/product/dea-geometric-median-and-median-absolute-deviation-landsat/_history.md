## Changelog

<span id="v4.0.0"></span>

### 16 Feb 2026: Issue notification removed

A potential issue was identified in September 2024 affecting the [DEA Geometric Median and Median Absolute Deviation (Landsat)](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) product. A bug in the processing code related to multithreading with `numexpr` may have caused a 400 × 400 pixel data block to be misplaced (effectively, duplicated) within a small number of tiles.
Initial estimates suggested that approximately 8–12 tiles across the full GeoMAD archive could have been affected; however, the specific tiles were unknown. 
The underlying cause was subsequently identified and fixed in the codebase.
In late 2025, the entire GeoMAD data repository was programmatically reviewed to detect any duplicated 400 × 400 pixel data blocks within each tile, excluding blocks that were fully no‑data. No evidence of affected tiles was found.
Based on this investigation, the issue is now considered resolved, and the notification has been moved to the change log.

### 30 Apr 2025: The 2024 annual data is now available

The 2024 annual data for this product was published on 30 April 2025. You are now able to [access the latest data](./?tab=access) via DEA Maps and other methods. [View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz6811775c5a24b812Pzzzz6567c8b713b5b826/page.html).

### Version 4.0.0

* **Breaking change: Shift in grid origin point** &mdash; The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south. Therefore, all tile grid references have been changed. For instance, a tile reference of `x10y10` has changed to `x28y25`. The tile grid references of all derivative products generated from 2024 onwards will also be changed; however, Analysis Ready Data products will not be affected.
* **Enhanced cloud masking to reduce noise** &mdash; An enhancement to cloud masking has reduced cloud and shadow noise. This enhancement (known as 'cloud buffering') involved cleaning cloud masks 
 using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows. Note that some areas of very high surface reflectance (e.g. sand dunes and ocean areas) may exhibit worsened noise or data gaps, but these are infrequent occurrences with low impact.
* **Combined Landsat 8 and 9 product** &mdash; A single combined product for Landsat 8 and Landsat 9 is provided. It achieves better performance than the standalone Landsat 8 product due to using a larger number of available observations. A standalone Landsat 8 product will no longer be provided from calendar year 2022 onwards.
* **Prefixed band measurement names** &mdash; An 'nbart' prefix was added to band measurement names for consistency with our Analysis Ready Data products. For example, the `red` band has been renamed to `nbart_red`.

<img src="/_static/geomedian/Geomedian_2020_Tasmania_v4_0_vs_v3_1.gif" alt="A comparison of the Geomedian Tasmania: v4.0 vs v3.1." style="max-width: 600px;">
