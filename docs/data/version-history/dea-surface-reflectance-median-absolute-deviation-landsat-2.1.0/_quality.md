## Accuracy

The accuracy of the TMAD is dependent on the accuracy of the underpinning Earth Observation data. As the values of the MADs are synthetic (not observed directly by satellite), they cannot be verified by field work.

To calculate a MAD representative of clear observations, the majority of the input data must be clear of clouds, shadows or other issues that can adversely affect an observation. Where a location experiences more than 50% of time under the impact of clouds and shadows (such as areas of Tasmania), the MAD can produce an output that is essentially cloud / shadow noise. As such, it is necessary to use a large enough collection of data to enable a clear median to be calculated. However, this also provides a basis for cloud and shadow detection through time series analysis.

To mitigate the impact of poor quality observations and other artefacts, the input data is first screened using the Pixel Quality product (PQ\_25\_2.0.0); however, some poor pixels are likely to still be included in the data after screening. Increasing the period from which observations are included in the input dataset also helps to mitigate the issue. Where no-data pixels occur in locations that clear observations should occur, the cause is a lack of clear pixels to populate the MADs.

% ## Quality assurance

