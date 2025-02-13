## Changelog

### Version 2.0.0

Landsat 9 was incorporated into this product starting in October 2021, providing an increase in available observations from November 2021 onwards.

### Version 1.6.0

Version 1.6.0 was updated with changes to the way different factors impeding water detection are dealt with. These changes result in improved detection rates and allow discrimination of different factors impeding water observations. Masking of the ocean with a pre-defined mask has been removed, and the extent of the ocean is now defined by the algorithm. Masking for terrain and solar incident angle have been decoupled in order to provide better visibility about the reason for masking. The solar incident angle threshold used to remove poor quality observations collected when the sun is at a very low angle has been reduced from 30 degrees to 10 degrees. This change increases the number of observations included in the dataset during winter months while still removing those that are most badly impacted by shadowing caused by low solar incident angle. 

