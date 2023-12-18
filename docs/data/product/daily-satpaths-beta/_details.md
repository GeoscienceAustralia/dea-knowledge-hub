## Background

Every day more than a dozen foreign-operated, public-good, non-commercial, medium to low resolution satellites fly over Australia and its territories. They cross the continent several times a day and their sensors capture images of the land and coastal waters.  

Satellite overpass schedules for each spacecraft are predictable and can be calculated with a degree of accuracy. The Daily SatPaths provides information on which satellite sensors have and will potentially acquire data over Australia during a given date and time interval. It is important to note that actual acquisition schedules may differ from those presented in Daily SatPaths due the operational limitations of the satellite.

## What this product offers

Daily SatPaths calculates date-specific predicted schedules for flyovers over Australia for 19 of the most popular public good satellites used by researchers in academia, and by public and private sector organisations.

It also displays, on an interactive map, the portion of Australia that is “visible” to those satellite sensors on each flyover (i.e. the so-called “ground footprint”).

The flight path schedules and sensor specific footprints can be downloaded in a tabular format (.csv file) and polygons in GeoJSON format for use in GIS software.

% ## Data description

## Applications

The information helps to answer three basic questions:

* what satellites are flying over Australia on a particular day, where and at what time?
* which satellite sensors will potentially acquire data over an area of specific interest?; and
* which ground stations in the [ANGSTT network](https://angstt.gov.au/) those satellites are visible from, hence which of those stations could potentially downlink the data?

## Technical information

Daily SatPaths calculates predictive schedules for flyovers over Australia and ground footprints for selected sensors (in most common mode of acquisition) on board the following non-commercial, public good, mid to low resolution orbiting satellites operated by USGS, NASA, NOAA and ESA.

   AQUA ([MODIS](https://cmi.ga.gov.au/resources/glossary/U?keyword=MODIS)): 2,330km swath

   TERRA (MODIS): 2,350km swath

   NOAA 15 ([AVHRR](https://cmi.ga.gov.au/resources/glossary/U?keyword=AVHRR)): 2,940km swath

   NOAA 18 (AVHRR): 2,940km swath

   NOAA 19 (AVHRR): 2,940km swath

   NOAA 20 ([VIIRS](https://cmi.ga.gov.au/resources/glossary/U?keyword=VIIRS)): 2,940km swath

   NPP (VIIRS): 3,040km swath

   LANDSAT 7 ([ETM+](https://cmi.ga.gov.au/resources/glossary/U?keyword=ETM)): 185km swath

   LANDSAT 8 ([OLI](https://cmi.ga.gov.au/resources/glossary/U?keyword=OLI)): 185km swath

   LANDSAT 9 (OLI): 185km swath

   SENTINEL 1A ([C-SAR](https://cmi.ga.gov.au/resources/glossary/U?keyword=Sentinel)): 250km – Interferometric Wide Swath Mode

   SENTINEL 1B (C-SAR): 250km – Interferometric Wide Swath Mode

   SENTINEL 2A (MSI): 290km swath

   SENTINEL 2B (MSI): 290km swath

   SENTINEL 3A (SLSTR): 1,270km swath

   SENTINEL 3B (SLSTR): 1.270km swath

   METOP-A (AVHRR): 2,900km swath

   METOP-B (AVHRR) : 2,900km swath

   METOP-C (AVHRR) : 2,900km swath

Predictive schedules are calculated for seven Australian ground stations which are participating in the [ANGSTT network](http://www.angstt.gov.au/):

   Alice Springs (ALS), operated by Geoscience Australia

   Cleveland Bay (CFQ), operated by AIMS

   Cribb Point (CPT), operated by Australian Bureau of Meteorology

   Hobart (HBT), operated by CSIRO

   Learmonth (LMO), operated by Australian Bureau of Meteorology

   Murdoch (MUR), operated by Landgate

   Shoal Bay (DAR), operated by Australian Bureau of Meteorology

The timing and footprints of satellite overpasses are calculated based on the parameters specified in a two-line element set (TLE) from [space-track.org](https://www.space-track.org/). These parameters are updated once a day and are republished in a [text file](https://satpaths.nemo.ga.gov.au/gatle.txt) by Geoscience Australia as a free service.

## Lineage

Information on start and end times for satellite flyovers, as well as position of satellites at a given time, are generated in real-time in the user browser based on current day two-line element set (TLE) data from SpaceTrack.org and jspredict library with algorithms ported from Predict open source tracking and orbital prediction software ([https://www.qsl.net/kd2bd/predict.html](https://www.qsl.net/kd2bd/predict.html)).

Ground footprint information is generated based on published, sensor specific swath widths, using general purpose ellipsoidal geometry spatial libraries latlon-ellipsoidal.js and latlon-vincenty.js .

% ## Processing steps

## Software

Daily SatPaths single page application is written in HTML5 and JavaScript.

It uses third party data and open source libraries, including:

* TLE information from [SpaceTrack.org](https://www.space-track.org)
* ground station locations from [angstt.gov.au](https://angstt.gov.au/)
* base map by [OpenStreetMap](https://www.openstreetmap.org) contributors
* [jquery](https://jquery.com)
* [jquery UI](https://jqueryui.com)
* [leafletjs](https://leafletjs.com)
* [momentjs](https://momentjs.com)
* [momentjs timezones](https://momentjs.com/timezone/)
* [satellite.js](https://github.com/shashwatak/satellite-js)
* [jspredit](https://github.com/nsat/jspredict)
* [vector3djs](https://www.movable-type.co.uk/scripts/geodesy/docs/module-vector3d.html)
* [latlon-ellipsoidal.js](https://www.movable-type.co.uk/scripts/geodesy/docs/module-latlon-ellipsoidal.html)
* [latlon-vincenty.js](https://www.movable-type.co.uk/scripts/geodesy/docs/module-latlon-ellipsoidal-vincenty.html)
* [dms.js](https://www.movable-type.co.uk/scripts/geodesy/docs/module-dms.html)
* [ResizeSensor.js](https://github.com/procurios/ResizeSensor)
* [ElementQueries.js](https://github.com/procurios/ElementQueries)
* [dataTables.js](https://datatables.net)

% ## References

