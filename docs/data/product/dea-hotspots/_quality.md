## Accuracy

### Quality assurance

* False positives (showing a Hotspot without an underlying cause) are possible. 
* False negatives (failing to show a Hotspot, despite a heated land surface, fire, etc.) are possible.  
* Hotspots are potential bushfires, but could also indicate other phenomena, such as gas fires, heavy industry, furnaces, smoke plumes, jet contrails and hot rocks.
* Not all fires will be detected as Hotspots.
* The Hotspot location on any map (no matter how detailed) is only accurate to ± 375 m at best (VIIRS).
* Hotspots are not presented in real-time and not designed to be used in isolation of other data sources. It is not accurate enough to be relied upon for time-critical detection and location of fires.
* Geostationary satellite derived products algorithms may be optimised for day or night conditions.  For algorithms such as BRIGHT that provide hotspots every 10 minutes, 24 hours per day, temporal windows approximately +/- 1 hour of sunset and sunrise are considered unreliable periods.
* No Hotspots are produced if satellite data is not received (e.g. for AHI, 0240 and 1440 UTC times are not received).
* Hotspots should not be used for safety of life decisions. For local updates and alerts, please refer to your state emergency or fire service.
* Depending on the sensor, generally, a flaming or smouldering fire would need to be at least 1,000 m2 to be recognised as a Hotspot. Under exceptional (and rare) conditions (no cloud, smoke, wind etc), a flaming fire at 50m2 may be detected. However, fires are often smaller than the size of the satellite pixel.

### Missing Hotspots

Hotspots may be obscured or missing from the map due to the following reasons:

* Polar Orbiting satellites are not designed to provide live updates on fire fronts, as they only look over the fire ground 4-7 times per day.
* Optical satellites cannot see though clouds, heavy smoke or tree canopy.  
* Fires may be missed if they are relatively small or do not cover a spatial footprint large enough to be detected by the sensors (e.g. the MODIS footprint is 1km2).  
* Cool fires are not likely to be detected.  
* Sensors can be inoperable for extended periods of time, disrupting the detection of Hotspots.  
* The fire may have been burning during a time when no satellite was looking over the fire ground.  

## DEA Hotspots Tech Alerts

### 19 Dec 2024: NOAA-21-derived DEA Hotspots are now available  

Following our [communication](https://communication.ga.gov.au/link/id/zzzz675f7ce74a008871Pzzzz6567c8b713b5b826/page.html) in November regarding changes to the Hotspots service, we are pleased to advise that Hotspots derived from the Visible Infrared Imaging Radiometer Suite (VIIRS) sensor onboard NOAA-21 are now available. NOAA-21 currently passes over Australia at approximately 3pm and 2am Australian Eastern Standard Time, increasing the density and reliability of the afternoon and nighttime observations.

In the Hotspots application, the NOAA-21 feed is off by default. You can include either the VIIRS ‘AFIMG NOAA-21’, or ‘AFMOD NOAA-21’ Hotspots algorithms as additional layers in the Hotspots map interface by selecting these layers from the VIIRS menu in the legend.  

[View the Tech Alert](https://communication.ga.gov.au/DEAHotspots-19Dec24)

### 18 Nov 2024: DEA Hotspots &mdash; Enhancing Bushfire Monitoring with New Satellite Data

We are writing to keep you informed of changes that are occurring to the DEA Hotspots service. While faced with the loss of the MODIS Terra for our morning observations, we can continue to use available satellites to bolster the density and reliability of our afternoon observations. Data from the Visible Infrared Imaging Radiometer Suite (VIIRS) sensor onboard NOAA-21 will be available in DEA Hotspots by early December 2024. Once NOAA-21 data is available, a tech alert will be issued to users.

[View the Tech Alert](https://communication.ga.gov.au/DEA-Hotspots-18Nov)

### 13 May 2024: Terra-derived DEA Hotspots are unavailable

Direct Broadcast satellite downloads from the Terra satellite have again become unavailable. This means that Terra-derived [DEA Hotspots](https://hotspots.dea.ga.gov.au/) are unavailable until further notice.

This is due to the TERRA MODIS satellite experiencing power problems. The satellite continues to collect data but its direct broadcast has stopped.