# Markdown Demo

## Calculate an index for this area manually

One of the most commonly used remote sensing indices is the Normalised Difference Vegetation Index or NDVI. This index uses the ratio of the red and near-infrared (NIR) bands to identify live green vegetation. The formula for NDVI is:

$$
\begin{aligned}
\text{NDVI} & = \frac{(\text{NIR} - \text{Red})}{(\text{NIR} + \text{Red})} \\
\end{aligned}
$$

When interpreting this index, high values indicate vegetation, and low values indicate soil or water.

```python
# Calculate NDVI using the formula
ds['ndvi'] = (ds.nbart_nir - ds.nbart_red) / (ds.nbart_nir + ds.nbart_red)

# Plot the results
ds.ndvi.isel(time=0).plot(vmin=-1, vmax=1, cmap='RdYlGn')
```

