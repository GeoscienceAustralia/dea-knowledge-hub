:::{dropdown} Why doesn't DEA make Landsat thermal bands available to users?
:name: landsat-no-thermal

Landsat satellite sensors not only collect data in the short-wave spectrum but also collect data into the thermal
infrared bands. The USGS makes this data available in the form of a surface temperature and emissivity product:
[Landsat Collection 2 Surface Temperature](https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-temperature).
It provides this separately to the surface reflectance products.

This USGS Surface Temperature product is a global product that uses global datasets to perform
corrections on the data that are collected by the satellite sensors. The land surface temperature outputs are very
sensitive to the atmospheric profile data that is used to perform the correction. For the global analysis, the
[NASA Modern Era Retrospective-Analysis for Research and Applications (MERRA)](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
atmospheric data is used to provide values for height, air temperature, and humidity. While this dataset works
well for a global correction, studies over Australia have shown that the correction can be improved
when higher resolution datasets are considered ([Li et al, 2015](https://mssanz.org.au/modsim2015/L11/li.pdf)).

DEA’s ARD product provides high-quality data corrections for Australian conditions. At present, we do not produce a
custom land surface temperature dataset for Australia, and so we have not included the thermal bands in our ARD package.

If you would like to use USGS Landsat thermal data directly, we provide a Jupyter notebook that shows you
[how to combine DEA ARD data with USGS thermal data](/notebooks/How_to_guides/Planetary_computer/#Load-time-series-satellite-data-from-Microsoft-Planetary-Computer).
:::

