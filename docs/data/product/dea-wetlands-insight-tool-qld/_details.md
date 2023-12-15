## Background

Wetlands provide a wide range of ecosystem services including improving water quality, carbon sequestration, as well as providing habitat for fish, amphibians, reptiles and birds.  Managing wetlands in Australia is challenging due to competing pressures for water availability and highly variable climatic settings.  The Wetlands Insight Tool (QLD) has been developed to provide catchment managers, environmental water holders, and wetlands scientists a consistent historical baseline of wetlands dynamics from 1987 onwards. The Wetlands Insight Tool (QLD) is available online through the Queensland Government Wetland*Info* website.

## What this product offers

The Wetlands Insight Tool (QLD) summarises how the amount of water, green vegetation, dry vegetation and bare soil varies over time within each wetland. It provides the user with the ability to compare how the wetland is behaving now with how it has behaved in the past.  This allows users to identify how changes in water availability have affected the wetland. It achieves this by presenting a combined view of Water Observations from Space, Tasseled Cap Wetness and Fractional Cover measurements from the Landsat series of satellites, summarised as a stacked line plot to show how that wetland has changed over time. 

![Wetlands Insight Tool stacked line plot for a seasonally inundated wetland](/_files/cmi/72035_EDWARD_RIVER_2a_sml.jpg)

% ## Data description

## Applications

The product is designed to support QLD wetland managers, catchment managers and environmental waterholders in understanding whether or not wetlands are changing over time.  In instances where the wetlands are changing, the tool allows users to identify whether the changes are gradual, rapid, once-off or cyclical in nature.  For example the response of wetlands to the following drivers can be assessed:
* Changes in river flow volumes
* Changes in flood frequency
* Long term shifts in rainfall
* Wet-season/Dry-season shifts in water availability
* Invasive weeds
* Environmental watering events

Care should be used when interpreting Wetlands Insight Tool (QLD) results as increases/decreases in particular cover types can be associated with different processes.  For example an increase in green cover could indicate canopy recovery of desirable wetland species or an increase in the amount of invasive weeds.

## Technical information

![Wetlands Insight Tool flow chart. A flow chart that begins with a pixel, separates it on whether the pixel is classified by WOfS into water or not-water. The next step separates the pixel on whether the Tasseled Cap Wetness is greater than -350. If yes, the pixel is classified as wet. If no, the pixel percentage cover values are returned from Fractional Cover of Vegetation as bare soil, dry vegetation and green vegetation percentages.  ](/_files/cmi/WITflowChartv2_950x615.PNG)

Every pixel within a wetland polygon is evaluated using this decision tree at every time step, and the results are tabulated to create the input data to the stacked line plot for that wetland.

## Lineage

The code base used to generate the QLD Wetlands Insight Tool results is available at [https://github.com/GeoscienceAustralia/wit\_tooling](https://github.com/GeoscienceAustralia/wit_tooling)

% ## Processing steps

% ## Software

## References

Scarth, P., Röder, A., Schmidt, M., 2010. Tracking grazing pressure and climate interaction - the role of Landsat fractional cover in time series analysis. In: Proceedings of the 15th Australasian Remote Sensing and Photogrammetry Conference (ARSPC), 13-17 September, Alice Springs, Australia. Alice Springs, NT.

Guerschman, J.P., Scarth, P.F., McVicar, T.R., Renzullo, L.J., Malthus, T.J., Stewart, J.B., Rickards, J.E., & Trevithick, R. (2015). Assessing the effects of site heterogeneity and soil properties when unmixing photosynthetic vegetation, non-photosynthetic vegetation and bare soil fractions from Landsat and MODIS data. *Remote Sensing of Environment,* 161, 12-26, [https://doi.org/10.1016/j.rse.2015.01.021](https://doi.org/10.1016/j.rse.2015.01.021)

Muir, J., Schmidt, M., Tindall, D., Trevithick, R., Scarth, P., Stewart, J., 2011. Guidelines for Field measurement of fractional ground cover: a technical handbook supporting the Australian collaborative land use and management program. Tech. rep., Queensland Department of Environment and Resource Management for the Australian Bureau of Agricultural and Resource Economics and Sciences, Canberra.

Mueller, N., Lewis, A.  Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A.,  Tan, P., Curnow, S. and  Ip, A.(2016) 'Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia', Remote Sensing of Environment, 174, 341-352, [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

Crist, E.P. (1985) 'A TM Tasseled Cap equivalent transformation for reflectance factor data', Remote Sensing of Environment, 17(3), 301-306, [https://doi.org/10.1016/0034-4257(85)90102-6](https://doi.org/10.1016/0034-4257(85)90102-6)

