## Background

This product has been deprecated and is superseded by this product: [DEA Water Observations Statistics (Landsat)](https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat)

The Water Observations from Space Filtered Statistics (WO-FILT-STATS) is the 'cleaned' version of the WOfS Statistics product (WO-STATS).

WO-STATS takes the full, ongoing archive of all Water Observation Feature Layers (WOFLs) and combines them into a single product summary showing how often surface water was observed by the Landsat satellites from 1986 to the present.

WO-FILT-STATS goes further, comparing WO\_STATS with other national surface water datasets to understand how confident we are that the water shown in WO-STATS is consistent with the long term understanding of water in the Australian landscape. Those areas where WO-STATS is not consistent with the other national datasets are then filtered out, to reduce misclassification from clouds, shadows and satellite errors.

## What this product offers

WO-FILT-STATS consists of:

* a **Confidence layer** that compares the WO-STATS water summary to other national water datasets.
* a **Filtered Water Summary** which uses the Confidence to mask areas of the WO-STATS water summary where Confidence is low. The Filtered Water Summary provides the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist.

% ## Data description

## Applications

* Helps understand where flooding may have occurred in the past, to inform emergency management and risk assessment.
* Provides an indication of the permanence of surface water in the Australian landscape by showing where water is observed rarely in comparison to where it is often observed, informing water management and mapping.
* Can assist with wetland analyses, water connectivity and surface-ground water relationships.

## Technical information

WO-FILT-STATS consists of the following datasets:

* **Confidence:** the degree of agreement between water shown in the Water Summary and other national datasets. The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means.  
* **Filtered Water Summary:** A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level. This layer gives a noise-reduced view of surface water across Australia. It provides the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. 

Both layers are represented as 32-bit float.

Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist.

In previous versions of WOfS, the basic water classifications, statistical summaries and confidence products were contained within one product with several datasets. As of version 2.1.5, WOfS is split into three products: Water Observation Feature Layers (WO\_25\_2.1.5), Summary Statistics (WO-STATS\_25\_2.1.5), and Filtered Summary Statistics (WO-Fil-STATS\_25\_2.1.5).

## Lineage

The WOfS product is a key component of the National Flood Risk Information Portal (NFRIP), developed by GA. The objective of Water Observations from Space is to analyse GA's historic archive of satellite imagery to derive water observations, to help understand where flooding may have occurred in the past. The collection of many hundred thousand WOFLs that make up WOfS are too cumbersome to display easily. WO\_STATS provides the mechanism to present and deliver WOfS in a more easily digestible form, and provides understanding of water in the landscape. WO-FILT-STATS provides extra information to give a confidence in whether water is likely in the locations shown by the other WOfS products and provides a final, "cleaned" summary of water over time.

WO-FILT-STATS is created from the WOfS-STATS statistics (Water Observations Statistics 2 (Landsat)) derived from water classification (Water Observations 2 (Landsat)).

Reviews of prototype products identified the need to indicate the level of confidence for the surface water observations. The confidence level will help the user to distinguish between unusual but valid water detections (such as flood plains which might only be observed as water once in the 15 year interval) and false positives which can be caused, for instance, by steep shady slopes. The confidence level was determined through a multiple logistic regression of water observations against several factors that would either support or contradict the finding of water being present at the site. The factors comprise:

* **MrVBF**, a multi-resolution valley bottom flatness product (Gallant et al., 2012) derived from Shuttle RADAR Topographic Mission (SRTM) data as part of the Terrestrial Ecosystems Research Network (TERN). Surface water pixels identified in valley bottoms were more likely to be positively detected.
* **Slope** derived from SRTM Digital Surface Models. Water pixels on a slope were considered less plausible than those on a flat surface.
* **MODIS Open Water Likelihood (OWL)** (Ticehurst et al, 2010) provides a plausibility based an independent water detection algorithm employing the MODIS sensor. If both detection algorithms agree on the presence of a surface water pixel, there is a greaterÂ plausibility that the detection is correct.
* **Observation Frequency (P)**, the number of observations of water as a fraction of the number of clear observations of the target pixel. P is high for more permanent water bodies.
* **Built-Up areas** indicating areas of dense urban development. In such areas the water detection algorithm struggles to cope with the deep shadows cast by multi-story buildings and the generally noisy spectral response created by structures. The Built-Up layer is derived from the Australian Bureau of Statistics ASGS 2011 dataset, for urban centres of populations of 100 000 and over.

Once calculated the Confidence is used to filter the Water Summary from WO-STATS where confidence is <10% to create the Filtered Water Summary.

## Processing steps

1. WOfS Confidence calculation

1. WOfS Summary Filtering

% ## Software

% ## References

