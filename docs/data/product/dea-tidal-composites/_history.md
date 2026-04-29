## Changelog

:::{include} ../../../_components/tech-alert-coastal-2024-2025-annual-product-update-summary.md
:::

### DEA Tidal Composites 1.1.0

In April 2026, DEA Tidal Composites was updated to version 1.1.0, and 2024 data was added to all layers. This update also includes the following changes:

* DEA Tidal Composites data is now provided natively as continental Cloud Optimised GeoTIFF mosaics. Visit the [Continental Cloud-Optimised GeoTIFF Mosaics page](/guides/continental-cogs-geotiff-mosaics/) for further details.
* All annual datasets updated with minor improvements to the ensemble tide modelling functionality used to filter satellite data by tide height.


### DEA Tidal Composites 1.0.0

In May 2025, DEA Tidal Composites version 1.0.0, was released. This release involved deprecating the [High and Low Tide Composites (HLTC)](/data/version-history/dea-high-and-low-tide-imagery-landsat-2.0.0/) product. Data from this legacy product will still be accessible; however, users are advised to transition to using DEA Tidal Composites instead, where possible.

The DEA Tidal Composites product suite extends the concepts developed in the Landsat-derived [High and Low Tide Composites (HLTC)](/data/version-history/dea-high-and-low-tide-imagery-landsat-2.0.0/) product, but instead uses 10 m Sentinel-2 data and tide modelling is completed at the pixel scale. Additionally, a rolling 3-year epoch is used to calculate the product on an annual time scale.

This shift to a more dynamic product suite is achieved through a pixel-based tide-modelling algorithm, improved data resolution and density through the use of Sentinel-2 data, and pre-processing improvements that include cloud, cloud-shadow, and glint-angle filtering to remove contaminated pixels.
