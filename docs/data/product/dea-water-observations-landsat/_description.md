## Background

It is important to know where water is normally present in a landscape, where water is rarely observed, and where inundation has occasionally occurred.

These observations tell us where flooding has occurred in the past, and allows us to understand wetlands, water connectivity and surface-groundwater relationships. This can lead to more effective emergency management and risk assessment.

This is the principal Digital Earth Australia (DEA) Water product (previously known as Water Observations from Space (WOfS)), providing the individual water observations per satellite image that are subsequently used in the following DEA Water suite and related water bodies products: DEA Waterbodies (Landsat), DEA Water Observations Statistics (Landsat), DEA Water Observations Filtered Statistics (Landsat).

This product shows where surface water was observed by the Landsat satellites on any particular day since mid 1986. These daily data layers are termed Water Observations (WOs).

## What this product offers

DEA Water Observations provides surface water observations derived from Landsat satellite imagery for all of Australia from 1986 to present.

The Water Observations show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows or where sensor problems cause parts of a scene to not be observable.

% ## Data description

## Applications

The DEA Water Observations (WOs) are used to determine the area of surface water present in the corresponding satellite scene, and can be used for several water monitoring applications. Uses of the individual WOs include:
* flood extent
* amount of water in water bodies, major rivers and the coastal zone.

As the WOs are separated from the derived statistics of the associated DEA Water statistical products, the WOs are most useful for performing analyses requiring the investigation of surface water extent for particular times rather than over long term time series.

## Technical information

Digital Earth Australia (DEA) Water Observations (WOs) is a gridded dataset indicating areas where surface water has been observed using the Geoscience Australia (GA) Earth observation satellite data holdings. The current product (version 2.0.0) includes observations taken between 1986 and the present (inclusive) from the Landsat 5, 7, 8 and 9 satellites. WOs cover all of mainland Australia and Tasmania but exclude off-shore Territories. The dataset is updated automatically as each new Landsat scene is acquired and processed to Analysis Ready Data (ARD) state. 

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The meaning of each bit in the WOFLs is given in the table below. Prior to version 1.6.0, only one bit could be set per pixel, therefore the value of a pixel in an observation could be X OR Y OR Z. Hence in previous versions the WOs values could only be 0 or 1 or 2 or 4 or ... or 128. From version 1.6.0 onward the data type has been changed to a bit field, where multiple bits can be set simultaneously. Hence the value of a pixel in an observation can be X AND Y AND Z, etc, hence values can range from 0 to 255.

Version 1.6.0 was updated with changes to the way different factors impeding water detection are dealt with. These changes result in improved detection rates and allow discrimination of different factors impeding water observations. Masking of the ocean with a pre-defined mask has been removed, and the extent of the ocean is now defined by the algorithm. Masking for terrain and solar incident angle have been de-coupled in order to provide better visibility about the reason for masking. The solar incident angle threshold used to remove poor quality observations collected when the sun is at a very low angle has been reduced from 30 degrees to 10 degrees. This change increases the number of observations included in the dataset during winter months while still removing those that are most badly impacted by shadowing caused by low solar incident angle. 

Version 2.0.0 introduces the integration of Landsat 9, providing an increase in available observations from November 2021 onwards.

The table below describes the meaning of each bit set per pixel in each WOFL.

:::{list-table} Classification bit sets
:header-rows: 1

* - Classification
  - Bit
  - Decimal
  - Description

* - **No Data**
  - 0
  - 1
  - Missing or invalid data. Pixel masked out due to NO_DATA in NBART source, 0 = valid data in NBART.

* - **Contiguity**
  - 1
  - 2
  - Some data is missing in the original image (usually missing bands). Pixel masked out due to lack of data contiguity.

* - **Solar Incidence**
  - 2
  - 4
  - Low solar angle means that the angle of the sun causes large shadow, therefore causing likely misclassifications of shadow as water. Pixel masked out due to solar incidence of less than 10 degrees.

* - **Terrain Shadow**
  - 3
  - 8
  - Topographic features can cast shadows, and these shadows are likely to be misclassified as water. Pixel masked out due to terrain shadow.

* - **High Slope**
  - 4
  - 16
  - This causes the classification of water to be less likely to be correct. Pixel masked out due to high slope.

* - **Cloud Shadow**
  - 5
  - 32
  - Shadows are likely to be misclassified as water. Pixel masked out due to cloud shadow.

* - **Cloud**
  - 6
  - 64
  - Cloud is affecting the output data. Pixel masked out due to cloud.

* - **Water**
  - 7
  - 128
  - Water detected.
:::

Furthermore, where multiple factors impeding a clear observation are detected, a combination of the decimal values will be set by adding the relevant decimal values together, e.g. 4 + 8 = 12. Notable combination values include Cloudy Terrain (Cloud + High Slope; 64 + 16 = 80), Shady Water (Water + Cloud Shadow; 128 + 32 = 160), and Cloudy Water (Water + Cloud; 128 + 64 = 192).

The following table represents these combinations of decimal values. In the table, the grey boxes are impossible values that cannot occur. The yellow boxes are ???????. 

:::{include} ../../../_components/water-observations-combination-decimals-table.md
:::

Full details of the original algorithms and features of DEA Water Observations can be found in the Water Observations from Space paper by Mueller et al. (2015).

## Lineage

Digital Earth Australia (DEA) Water Observations is derived from Landsat 5, 7, 8 and 9 imagery. Imagery is initially corrected to Analysis Ready Data (ARD) standard, and masked for cloud, cloud-shadow, data contiguity, steep slope, solar incidence angle, and terrain shadow. Water classification is achieved using a decision tree based on the individual spectral bands of the Landsat satellites and derived normalised difference indicies associated with water and vegetation. The output is then stored as an 8-bit, bit-field with values from 0 - 255 indicating the presence or absence of each mask type and the presence or absence of water.

## Processing steps

The water detection algorithm used to detect water from each observed pixel is based on a statistical regression tree analysis of a set of normalised difference indices and corrected band values. The regression is based on a set of water and non-water samples created by visual interpretation of 20 Landsat scenes from across Australia. The sample locations ensure that the logistic regression is based on the full geographic range of conditions experienced in Australia.

The regression analysis determined a set of best indices and bands for the analysis and the associated thresholds in each component to derive a final classification tree, producing a water/non-water classification for each pixel in the Data Cube. The final water classification for each pixel is modified by Pixel Quality (see associated PQ product information) and terrain.
Once the water algorithm has completed its process, the water detection for a pixel through time is combined to produce a total number of water observations for each pixel. This is compared to a total number of clear observations for the same pixel, derived from the PQ analysis. The ratio is expressed as a percentage water recurrence.

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

