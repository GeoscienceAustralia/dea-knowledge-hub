## Background

It is important to know where water is normally present in a landscape, where water is rarely observed, and where inundation has occasionally occurred.

These observations tell us where flooding has occurred in the past, and allows us to understand wetlands, water connectivity and surface-groundwater relationships. This can lead to more effective emergency management and risk assessment.

This is the principal Digital Earth Australia (DEA) Water product (previously known as Water Observations from Space (WOfS)), providing the individual water observations per satellite image that are subsequently used in the following DEA Water suite and related water bodies products: DEA Waterbodies (Landsat), DEA Water Observations Statistics (Landsat), DEA Water Observations Filtered Statistics (Landsat).

This product shows where surface water was observed by the Landsat satellites on any particular day since mid 1986. These daily data layers are termed Water Observations (WOs).

## What this product offers

DEA Water Observations is a gridded dataset indicating areas where surface water has been observed using the Geoscience Australia (GA) Earth observation satellite data holdings. The current product (version 2.0.0) includes observations taken between 1986 and the present (inclusive) from the Landsat 5, 7, 8, and 9 satellites. WOs cover all of mainland Australia and Tasmania but exclude offshore Territories. The dataset is updated automatically as each new Landsat scene is acquired and processed to Analysis Ready Data (ARD) state. 

The Water Observations show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows, or where sensor problems cause parts of a scene to not be observable.

% ## Data description

## Applications

The DEA Water Observations (WOs) are used to determine the area of surface water present in the corresponding satellite scene, and can be used for several water monitoring applications. Uses of the individual WOs include:

* flood extent
* amount of water in water bodies, major rivers and the coastal zone.

As the WOs are separated from the derived statistics of the associated DEA Water statistical products, the WOs are most useful for performing analyses requiring the investigation of surface water extent for particular times rather than over long term time series.

## Technical information

Data is provided as Water Observation Feature Layers (WOFLs) in a one-to-one relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The data type is a bit field, which allows multiple bits to be set simultaneously.

In the WOFL, each pixel is encoded as a bit flag which represents a decimal. This decimal corresponds to a classification or a combination of classifications. These classifications and combinations of classifications are mapped to colours on [DEA Maps](https://maps.dea.ga.gov.au/) and in the output of the `plot_wo` function. This allows you to easily view these classifications of the landscape. See Figure 1 for an example of these map colours and see Table 1 for details of these classifications. Learn more about bit flags in the [DEA Notebook: Introduction to DEA Water Observations](/notebooks/DEA_products/DEA_Water_Observations/).

A pixel in the WOFL can have a combination of multiple classifications. This is encoded by adding the decimal values of these classifications together. For example, a pixel with a decimal value of 192 is classified as both Water and Cloud (because 128 + 64 = 192). Furthermore, more than two classifications can be combined. For example, a pixel with a decimal value of 56 is classified as High Slope and Cloud Shadow and Terrain Shadow (because 16 + 32 + 8 = 56). The most commonplace of these combinations have been given their own names and colours so they can be easily seen on the map: Cloudy Water, Shaded Water, and Cloudy Steep Terrain. See Table 2 for the decimal values of all combinations of two classifications. Some values are greyed out because they cannot occur for any of several reasons. For instance, a classification cannot be combined with itself, so Cloud + Cloud is greyed out.

Note that decimal values in the WOFL can range from 0 to 255.

For more information about the original algorithms and features of DEA Water Observations, see the paper: [Water observations from space by Mueller et al. (2016)](https://doi.org/10.1016/j.rse.2015.11.003).

<figure>
    <img src="/_static/water-observations/water-observations-colours-example.png" alt="Colour map of Water Observations product." />
    <figcaption>Figure 1. Map colours example.</figcaption>
</figure>

:::{include} ../../../_components/water-observations-classifications-table.html
:::

:::{include} ../../../_components/water-observations-combination-decimals-table.html
:::

## Lineage

Digital Earth Australia (DEA) Water Observations is derived from Landsat 5, 7, 8 and 9 imagery. Imagery is initially corrected to Analysis Ready Data (ARD) standard, and masked for cloud, cloud-shadow, data contiguity, steep slope, solar incidence angle, and terrain shadow. Water classification is achieved using a decision tree based on the individual spectral bands of the Landsat satellites and derived normalised difference indicies associated with water and vegetation. The output is then stored as an 8-bit, bit-field with values from 0 - 255 indicating the presence or absence of each mask type and the presence or absence of water.

## Processing steps

The water detection algorithm used to detect water from each observed pixel is based on a statistical regression tree analysis of a set of normalised difference indices and corrected band values. The regression is based on a set of water and non-water samples created by visual interpretation of 20 Landsat scenes from across Australia. The sample locations ensure that the logistic regression is based on the full geographic range of conditions experienced in Australia.

The regression analysis determined a set of best indices and bands for the analysis and the associated thresholds in each component to derive a final classification tree, producing a water/non-water classification for each pixel in the Data Cube. The final water classification for each pixel is modified by Pixel Quality (see associated PQ product information) and terrain.
Once the water algorithm has completed its process, the water detection for a pixel through time is combined to produce a total number of water observations for each pixel. This is compared to a total number of clear observations for the same pixel, derived from the PQ analysis. The ratio is expressed as a percentage water recurrence.

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

