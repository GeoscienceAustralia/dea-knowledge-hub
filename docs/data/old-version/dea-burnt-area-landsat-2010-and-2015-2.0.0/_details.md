## Background

The Burned Area product provided information on the area of Australia burnt per calendar year using the Landsat satellites. This information was useful for understanding which areas burnt at which time of year and to what degree, and helps inform how often an area burnt and how long since last burn.

## What this product offers

The Burned Area product offers an annual understanding of all areas burnt across Australia. It provides area burnt, the month the burn occurred, and an assessment of burn severity.

% ## Data description

## Applications

* To understand which areas burnt during a calendar year
* To assess burn severity for each burn area
* To be used as an input to carbon accounting
* To understand land cover change
* To assess the time since last burn and frequency of burn, and hence possible fuel loads

## Technical information

Burned area is mapped from Landsat surface reflectance time series. It implements a change detection algorithm developed jointly by ANU and GA.

The maps are produced for calendar years. The layers available are: 
* StartDate, detected start-date of severe and moderate burned area
* Duration, duration of land cover change due to the bushfire
* Severity, severity of land cover change due to the bushfire
* Severe, binary mask for severe burnt area; Moderate, binary mask for moderate and severe burnt area
* Corroborate, binary mask for corroborating evidence from hotspots data with 4km buffer
* Cleaned, month of first detection, filtered by spatial and temporal coincidence with corroborate layer

## Lineage

Burned area is mapped from Landsat surface reflectance time series. It implements a change detection algorithm developed jointly by ANU and GA.

% ## Processing steps

% ## Software

% ## References

