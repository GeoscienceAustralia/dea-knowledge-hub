## Changelog

### 30 Apr 2025: The 2024 annual data is now available

The 2024 annual data for this product was published on 30 April 2025. You are now able to [access the latest data](./?tab=access) via DEA Maps and other methods. [View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz6811775c5a24b812Pzzzz6567c8b713b5b826/page.html).

### Version 4.0.0

- **Breaking change: Shift in grid origin point** — The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south. All tile grid references have changed (e.g., `x10y10` is now `x28y25`). This affects all summary derivative products, but baseline and scene derivative products remain unaffected.
- **Enhanced cloud masking to reduce noise** — Cloud masking improvements use 6-pixel dilation on cloud and shadows to reduce noise in source datasets. Some high-reflectance areas (sand dunes, ocean) may show increased noise or data gaps, but these occurrences are infrequent with minimal impact.
- **Additional inputs from Landsat 9** — Landsat 9 data incorporated from 2022 onwards.
