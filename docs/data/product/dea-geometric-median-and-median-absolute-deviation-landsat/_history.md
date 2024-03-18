## Changelog

<span id="v4.0.0"></span>

### Version 4.0.0

An enhancement to cloud masking has reduced cloud and shadow noise. Cloud masks have been cleaned using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows. Unlike previous versions which did not use cloud buffering. Note that some areas of very high surface reflectance (e.g. sand dunes and ocean glint) may exhibit higher levels of noise or data gaps, but this has limited impact.

The south-west origin point of the DEA Summary Product Grid has been shifted 20 tiles west and 17 tiles south. This will lead to an update of all tile grid references for all derivative product generated from now on (e.g. a tile reference of x42y17 will become x62y34). Analysis Ready Data products will remain unchanged.

A single combined product for Landsat 8 and 9 is provided. This has better performance than the standalone Landsat 8 product due to an increased number of available observations. A standalone Landsat 8 product will no longer be provided from calendar year 2022 onwards.

Band measurement names were updated for consistency with DEA's Analysis Ready Data products by adding the 'nbart' prefix (e.g. the ‘red’ band has become ‘nbart_red’).

<img src="/_static/geomedian/Geomedian_2020_Tasmania_v4_0_vs_v3_1.gif" alt="A comparison of the Geomedian Tasmania: v4.0 vs v3.1." style="max-width: 600px;">
