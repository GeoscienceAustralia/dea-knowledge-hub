## Accuracy

The accuracy of the algorithms for test locations is described in their respective journal articles. However the combination of complex cloud environments, thin cirrus and the scan line corrector error all contribute to the limitations of the PQ25 product . Currently, both the cloud and cloud shadow algorithms rely on the thermal data in order to effectively screen out cloud/cloud shadow affected pixels. The absence of thermal data prevents these algorithms from running, thereby producing a PQ25 product lacking any cloud or cloud shadow masks. This severely can impact any subsequent analysis.

The Land Sea Mask, whilst derived from a 100K vector file, the boundary shape may not accurately represent the coastal features visible in the imagery. In order to decrease the chances of eliminating pixels identified as land, the source vector file was buffered (extended) by 150m outwards towards the sea.

## Quality assurance

The validation of the underlying algorithms is contained within the journal articles that describe ACCA (Irish et al. 2006), Fmask (Zhu and Woodcock 2012) and the ATBD that describes the sensor saturation flagging method (Roy et al. 2010).

