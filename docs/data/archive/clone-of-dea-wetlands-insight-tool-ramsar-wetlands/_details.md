## Background

Wetlands provide a wide range of ecosystem services including improving water quality, carbon sequestration, as well as providing habitat for fish, amphibians, reptiles and birds.  Managing wetlands in Australia is challenging due to competing pressures for water availability and highly variable climatic settings.  The Wetlands Insight Tool (Ramsar Wetlands) has been developed to provide catchment managers, environmental water holders, and wetlands scientists a consistent historical baseline of wetlands dynamics from 1987 onwards. The Wetlands Insight Tool (Ramsar Wetlands) is available online through the DEA Maps website.

The Ramsar Wetlands of Australia Dataset is available under a [Creative Commons Attribution 3.0 Australia Licence](https://creativecommons.org/licenses/by/3.0/au/) . We created individual wetland polygons from the multipart Ramsar polygons in the dataset. The 6 Australian Ramsar Sites in external territories are excluded as they are outside of Australia’s satellite data footprint.

## What this product offers

The Wetlands Insight Tool (Ramsar Wetlands) summarises how the amount of water, green vegetation, dry vegetation and bare soil varies over time within each wetland boundary. It provides the user with the ability to compare how the wetland is behaving now with how it has behaved in the past.  This allows users to identify how changes in water availability have affected the wetland. It achieves this by presenting a combined view of Water Observations from Space (DEA Water Observations), Tasseled Cap Wetness (DEA Wetness Percentiles) and Fractional Cover (DEA Fractional Cover) measurements from the Landsat series of satellites, summarised as a stacked line plot to show how that wetland has changed over time. 

![Wetlands Insight Tool plot for Narran Lakes Nature Reserve, NSW, showing open water, wet, green vegetation, dry vegetation and bare soil.](/sites/default/files/inline-images/Fig6_small968px_0.png)

% ## Data description

## Applications

The product is designed to support Ramsar wetland managers, catchment managers and environmental waterholders in understanding whether or not wetlands are changing over time.  In instances where the wetlands are changing, the tool allows users to identify whether the changes are gradual, rapid, once-off or cyclical in nature.  For example the response of wetlands to the following drivers can be assessed:

* Changes in river flow volumes
* Changes in flood frequency
* Long term shifts in rainfall
* Wet-season/Dry-season shifts in water availability
* Invasive weeds
* Environmental watering events

Care should be used when interpreting Wetlands Insight Tool (Ramsar Wetlands) results as increases/decreases in particular cover types can be associated with different processes.  For example an increase in green cover could indicate canopy recovery of desirable wetland species or an increase in the amount of invasive weeds.

## Technical information

![Every pixel within a wetland polygon is evaluated using this decision tree at every time step, and the results are tabulated to create the input data to the stacked line plot for that wetland. The image shows a flow chart where a pixel is checked to see if it is cloudy or nodata, classified by WOfS as water, the Tasseled Cap Wetness value is greater than negative 350. if yes the pixel is classified as cloudy or notdata, then open water, then wet, and if no then the Fractional Cover of Vegetation percentage is retrieved for the pixel and the percentage of green vegetation, dry vegetation and bare soil is returned. ](/sites/default/files/inline-images/Fig2_small968px.png)

## Lineage

The code base used to generate the Ramsar Wetlands Insight Tool results is available at [https://github.com/GeoscienceAustralia/wit\_tooling](https://github.com/GeoscienceAustralia/wit_tooling)

* The polygon set defined in [http://www.environment.gov.au/fed/catalog/search/resource/details.page?uuid=%7BF49BFC55-4306-4185-85A9-A5F8CD2380CF%7D](https://wetlandinfo.des.qld.gov.au/wetlands/) 
* [DEA Water Observations (Landsat)](https://cmi.ga.gov.au/data-products/dea/142/dea-water-observations-landsat)
* [DEA Fractional Cover (Landsat](https://cmi.ga.gov.au/data-products/dea/119/dea-fractional-cover-landsat))
* [DEA Surface Reflectance NBART (Landsat)](https://cmi.ga.gov.au/data-products/dea/115/dea-surface-reflectance-nbart-landsat)

% ## Processing steps

## Software

The Fractional cover (v2) algorithm is provided courtesy of the Joint Remote Sensing Research Program. The development of the algorithm was supported by field data collection by Australian State and Territory agencies, TERN and the National Ground Cover Monitoring Program, coordinated by ABARES. The code base used to generate the Ramsar Wetlands Insight Tool results is available at <conflux links>#FIXME

## References

* Scarth, P., Röder, A., Schmidt, M., 2010. Tracking grazing pressure and climate interaction - the role of Landsat fractional cover in time series analysis. In: Proceedings of the 15th Australasian Remote Sensing and Photogrammetry Conference (ARSPC), 13-17 September, Alice Springs, Australia. Alice Springs, NT.
* Guerschman, J.P., **Scarth**, P.F., McVicar, T.R., Renzullo, L.J., Malthus, T.J., Stewart, J.B., Rickards, J.E., & **Trevithick**, R. (2015). Assessing the effects of site heterogeneity and soil properties when unmixing photosynthetic vegetation, non-photosynthetic vegetation and bare soil fractions from Landsat and MODIS data. *Remote Sensing of Environment,* 161, 12-26, [https://doi.org/10.1016/j.rse.2015.01.021](https://doi.org/10.1016/j.rse.2015.01.021)
* Muir, J., Schmidt, M., Tindall, D., Trevithick, R., Scarth, P., Stewart, J., 2011. Guidelines for Field measurement of fractional ground cover: a technical handbook supporting the Australian collaborative land use and management program. Tech. rep., Queensland Department of Environment and Resource Management for the Australian Bureau of Agricultural and Resource Economics and Sciences, Canberra.
* Mueller, N., Lewis, A.  Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A.,  Tan, P., Curnow, S. and  Ip, A.(2016) 'Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia', Remote Sensing of Environment, 174, 341-352, [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)
* Crist, E.P. (1985) 'A TM Tasseled Cap equivalent transformation for reflectance factor data', Remote Sensing of Environment, 17(3), 301-306, [https://doi.org/10.1016/0034-4257(85)90102-6](https://doi.org/10.1016/0034-4257(85)90102-6)

