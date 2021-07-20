
============================
 Frequently Asked Questions
============================


.. based on a conversation in Slack on <2021-07-06 Tue>

Why does Collection 3 ARD have a higher latency than Collection 2 ARD?
==================================================================

Collection 3 ARD appears to lag about a week behind Collection 2 ARD. When will this be fixed?

    Collection 2 ARD uses Collection 5 MODIS Bidirectional Reflectance Distribution Function 
    data (BRDF) which was decommissioned and replaced by Collection 6 BRDF as of 2018. Since 
    no real BRDF is available, Collection 2 ARD uses seasonal MODIS BRDF. In contrast, 
    Collection 3 ARD uses the "real" Collection 6 MODIS BRDF for new acquisitions, so needs 
    to "wait" until this are available. BRDF is derived from 16 days of MODIS observations 
    over the area (to ensure 16 different view/solar angles can be used to simulate the model), 
    hence the delay. To conclude, Collection 3 ARD has a higher latency than Collection 2 ARD, 
    but uses more reliable and up-to-date calibration.
