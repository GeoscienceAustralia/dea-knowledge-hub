
============================
 Frequently Asked Questions
============================


.. based on a conversation in Slack on <2021-07-06 Tue>

Why does Collection 3 ARD have a higher latency than Collection 2?
==================================================================

One of our stakeholders is wondering why C3 lags about a week behind C2, and
when this will be fixed.?


robbibt

    My understanding is that the lag is due to Collection 3 waiting for certain
    ancillary atmospheric correction data to be available before the ARD is
    generated.

    Collection 2 used a (slightly dodgy?) fall-back method to produce data before
    those inputs were available, which C3 doesn't do. So, Collection 2 has lower
    latency, but the most recent data is less reliable than the higher latency C3. I
    don't think there are any plans to "fix" this, apart from perhaps near real time
    Landsat coming out of CARSA.

lanweiwang

    It's likely due to MODIS BRDF - C2 uses Collection 5 MODIS BRDF which stopped
    (replaced by collection 6 BRDF) around 2 years ago. Since no real BRDF is
    available, C2 is using seasonal MODIS BRDF; and C3 is using the "real"
    collection 6 MODIS BRDF for new acquisitions, so needs to "wait" until they are
    available - BRDF were derived from 16 days of MODIS observations over the same
    area (so they have 16 different view/solar angles to simulate the model) hence
    the delay.
