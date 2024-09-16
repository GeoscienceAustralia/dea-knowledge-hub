## Background

Fractional cover data can be used to identify large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land management practices and rangeland condition.

This information is used by policy agencies, natural and agricultural land resource managers, and scientists to monitor land conditions over large areas over long time frames.

## What this product offers

Fractional Cover (FC), developed by the Joint Remote Sensing Research Program, is a measurement that splits the landscape into three parts, or fractions:
* green (leaves, grass, and growing crops)
* brown (branches, dry grass or hay, and dead leaf litter)
* bare ground (soil or rock)

Digital Earth Australia (DEA) uses Fractional Cover to characterise every 30 m square of Australia for any point in time from 1986 to today.

% ## Data description

## Applications

Fractional cover provides valuable information for a range of environmental and agricultural applications, including:
* soil erosion monitoring
* land surface process modelling
* land management practices (e.g. crop rotation, stubble management, rangeland management)
* vegetation studies
* fuel load estimation
* ecosystem modelling
* land cover mapping

## Technical information

Fractional Cover (FC) provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare soils for every 30m x 30m ground footprint across the whole Australian continent. This information is available for every cloud free satellite observation over Australia from 1986 till now. FC can potentially provide insights into the interplay and changes in areas of dry vegetation and/or bare soil as well as allowing the mapping of green vegetation extent.

The FC algorithm was developed by the Joint Remote Sensing Research Program (JRSRP) and is described in Scarth et al. (2010). It has been implemented by Geoscience Australia for every observation from Landsat Thematic Mapper (Landsat 5), Enhanced Thematic Mapper (Landsat 7) and Operational Land Imager (Landsat 8 and 9) acquired since 1986. It is calculated from terrain corrected surface reflectance (DEA Surface Reflectance).

FC provides a 30m scale fractional cover representation of the proportions of green vegetation, non-green vegetation, and bare surface cover across the Australian continent. The fractions are retrieved by inverting multiple linear regression estimates and using synthetic endmembers in a constrained non-negative least squares unmixing model.

For more information, see Scarth et al. (2010) and Schmidt et al. (2010), and a brief description of the FC algorithm on the [TERN website](https://portal.tern.org.au/metadata/22026).

### Data layers

The product consists of four data layers:
* The fractional cover of green vegetation (PV) 
* The fractional cover of non-green vegetation (NPV)
* The fractional cover of bare soil (BS)
* The fractional cover unmixing error (UE)

The values for this product are scaled as follows:  
* For the fractional cover bands (PV, NPV, BS)  
* 0-100 = fractional cover values that range between 0 and 100%

Due to model uncertainties and the limitations of the training data, some areas may show cover values in excess of 100%.  These areas can either be excluded or treated as equivalent to 100%

For the unmixing error (UE) band, the values are scaled between 0 and 127. High unmixing error values represent areas of high model uncertainty (areas of water, cloud, cloud shadow or soil types/colours that were not included in the model training data).

### Processing steps

Fractional Cover (FC) provides a representation of the proportions of living vegetation, dry and dying vegetation (including deciduous trees during autumn, dying grass, etc.), and bare soils across the Australian continent for any point in time in the Landsat archive since 1987. FC can potentially provide insight into areas of dry/dying vegetation and/or bare soil as well as allowing the mapping of living vegetation extent.

Fractional cover data can be used to identify large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land management practices and rangeland condition. This information could enable policy agencies, natural and agricultural land resource managers, and scientists to monitor land conditions over large areas over long time frames.

The Fractional Cover (FC) algorithm was developed by the Joint Remote Sensing Research Program and is described in described in Scarth et al. (2010). It has been implemented by Geoscience Australia for every observation from Landsat Thematic Mapper (Landsat 5), Enhanced Thematic Mapper (Landsat 7) and Operational Land Imager (Landsat 8) acquired since 1987. It is calculated from surface reflectance data.

FC provides a fractional cover representation of the proportions of green or photosynthetic vegetation, non-photosynthetic vegetation, and bare surface cover across the Australian continent. The fractions are retrieved by inverting multiple linear regression estimates and using synthetic endmembers in a constrained non-negative least squares unmixing model. For further information please see Scarth et al., 2010 and Schmidt et al., 2010. 

% ## Software

## Lineage

The fractional cover algorithm was developed by the Joint Remote Sensing Research Program (JRSRP) and is described in Scarth et al. (2010). While originally calibrated in Queensland, a large collaborative effort between The Department of Agriculture - ABARES and State and Territory governments to collect additional field data has enabled the calibration/validation to extend to the entire Australian continent.

1390 field data sites were used to train the model, and a separate 1565 sites were used to evaluate the model accuracy.

FC was made possible by the collaborative framework established by the [Terrestrial Ecosystem Research Network (TERN)](http://www.tern.org.au) through the [National Collaborative Research Infrastructure Strategy (NCRIS)](https://www.education.gov.au/national-collaborative-research-infrastructure-strategy-ncris) and collaborative effort between state and Commonwealth governments.

## References

Flood, N. (2014). Continuity of reflectance data between Landsat-7 ETM+ and Landsat-8 OLI, for both top-of-atmosphere and surface reflectance: A study in the Australian landscape. *Remote Sensing*, *6*(9), 7952–7970. [https://doi.org/10.3390/rs6097952](https://doi.org/10.3390/rs6097952)

Muir, J., Schmidt, M., Tindall, D., Trevithick, R., Scarth, P. and Stewart, J.B. (2011). Guidelines for field measurement of fractional ground cover: a technical handbook supporting the Australian Collaborative Land Use and Management Program. *Queensland* *Department of Environment and Resource Management for the Australian Bureau of* *Agricultural and Resource Economics and Sciences*. 

Scarth, P., Roder, A. and Schmidt, M. (2010). Tracking grazing pressure and climate interaction - the role of Landsat fractional cover in time series analysis. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*

Schmidt, M., Denham, R. and Scarth, P. (2010), Fractional ground cover monitoring of pastures and agricultural areas in Queensland. *Proceedings of the 15th Australasian Remote Sensing & Photogrammetry Conference.*

