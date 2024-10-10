## Background

These are the statistics generated from the DEA Water Observations (Water Observations from Space) suite of products, which gives summaries of how often surface water was observed by the Landsat satellites for various periods (per year, per season and for the period from 1986 to the present).

Water Observations Statistics (WO-STATS) provides information on how many times the Landsat satellites were able to clearly see an area, how many times those observations were wet, and what that means for the percentage of time that water was observed in the landscape.

## What this product offers

Each dataset in this product consists of the following datasets:
* **Clear Count:** how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems)
* **Wet Count:** how many times water was detected in observations that were clear
* **Water Frequency:** what percentage of clear observations were detected as wet (i.e. the ratio of wet to clear as a percentage)

% ## Data description

## Applications

* Helps understand where flooding may have occurred in the past, to inform emergency management and risk assessment.
* Provides an indication of the permanence of surface water in the Australian landscape by showing where water is observed rarely in comparison to where it is often observed, informing water management and mapping.
* Can assist with wetland analyses, water connectivity and surface-ground water relationships.
* The annual product provides information on how surface water changes per year across Australia, and is useful for drought analysis.
* The seasonal product is useful for understanding the differences in water availability between the summer and winter periods across Australia.

## Technical information

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the input water classifications, and can be difficult to interpret on its own. 

WO-STATS is available in multiple forms, depending on the length of time over which the statistics are calculated. At present the following are available:
* **DEA WO Multi-Year:** `ga_ls_wo_fq_myear_3`: statistics calculated from the full depth of time series (1986 to present) unfiltered
* **DEA WO Calendar Year:** `ga_ls_wo_fq_cyear_3`: statistics calculated from each calendar year (1986 to present)
* **DEA WO November to March:** `ga_ls_wo_fq_nov_mar_3`: statistics calculated yearly from November to March (1986 to present)
* **DEA WO April to October:** `ga_ls_wo_fq_apr_oct_3`: statistics calculated yearly from April to October (1986 to present)

In addition, a confidence-filtered Multi-Year Summary is under development, which will contain a confidence layer and subsequent filtered water frequency layer. This provides a noise-reduced view of the unfiltered multi-year summary.

## Lineage

This product is created from the WO water classification (Water Observations (Landsat)). Every pixel location is analysed statistically to derive the count of clear observations, the count of clear-wet observations and then to calculate the percentage of clear observations that were also wet. This provides a 'normalised' water frequency product for all of Australia.

Each product within the WO-STATS set is derived from the available Landsat observations within the respective period: calendar years; Apr-Oct each year; Nov-Mar each year; all-of-time (first available Landsat observation in the DEA archive to the most recent).

To create the confidence layer required for the filtered product, a logistic regression is created between the un-filtered product and information about terrain, built-up areas, and coarse national water observations. In this way the confidence reflects the likelihood that the observed water is scientifically feasible at every pixel.

## Processing steps

Calculation of clear count, wet count and water summary (percentage of clear observations that are wet).

For each WO pixel through time:

<div class="processing-steps"></div>

1. count the number of clear observations (ie observations not masked by pixel quality for cloud, shadows or sensor issues) to produce clear count dataset;
1. count the number of clear observations that are wet to produce wet count dataset;
1. create the ratio of wet to clear from the wet and clear count datasets and produce as a percentage dataset.

% ## Software

## References

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

