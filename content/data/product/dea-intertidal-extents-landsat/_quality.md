## Accuracy

Due the sun-synchronous nature of the various Landsat sensor observations; it is unlikely that the full physical extents of the tidal range in any cell will be observed. Hence, terminology has been adopted for the product to reflect the highest modelled tide observed in a given cell (HOT) and the lowest modelled tide observed (LOT) (Figure 2). These measures are relative to Mean Sea Level, and have no consistent relationship to Lowest (LAT) and Highest Astronomical Tide (HAT).

The inclusion of the lowest (LMT) and highest (HMT) modelled tide values for each tidal polygon in the ITEMv2\_tidalmodel dataset indicates the highest and lowest tides modelled for that location across the full time series by the OTPS model. The relative difference between the LOT and LMT (and HOT and HMT) heights gives an indication of the extent of the tidal range represented in the Relative Extents Model.

As in ITEM v1.0, v2.0 contains some false positive land detection in open ocean regions. These are a function of the lack of data at the extremes of the observed tidal range, and features like glint and undetected cloud in these data poor regions/intervals. Methods to isolate and remove these features are in development for future versions.

Issues in the DEA archive and data noise in the Esperance, WA region off Cape Le Grande and Cape Arid (Polygons 236,201,301) has resulted in significant artefacts in the model, and use of the model in this area is not recommended.

## Quality assurance

The Confidence layer is designed to assess the reliability of the Relative Extent Model. Within each tidal range percentile interval, the pixel-based standard deviation of the NDWI values for all observations in the interval subset is calculated. The average standard deviation across all tidal range intervals is then calculated and retained as a quality indicator in this product layer.

The Confidence Layer reflects the pixel based consistency of the NDWI values within each subset of observations, based on the tidal range. Higher standard deviation values indicate water classification changes not based on the tidal cycle, and hence lower confidence in the extent model. Possible drivers of these changes include:

* Inadequacies of the tidal model, due perhaps to complex coastal bathymetry or estuarine structures not captured in the model. These effects have been reduced in ITEM v2.0 compared to previous versions, through the use of an improved tidal modelling framework (see Sagar et al. 2018)
* Change in the structure and exposure of water/non-water features NOT driven by tidal variation. For example, movement of sand banks in estuaries, construction of man-made features (ports etc.).
* Terrestrial/Inland water features not influenced by the tidal cycle.

