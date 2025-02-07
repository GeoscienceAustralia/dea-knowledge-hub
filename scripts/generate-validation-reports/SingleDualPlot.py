import os
import matplotlib.pyplot as plt
from scipy.stats import linregress


def single_plot(PlatNames, PlatNamesSpace, field_data, prev_data, today_data, prev_today_data, formDate):
    #
    # MAKE SINGLE OVERPASS OVERALL SUMMARY PLOT
    #
    plot_scale = [0.0, 0.8, 0.0, 0.8]

    #
    # Set up parameters, based on whether we are plotting Landsat or Sentinel data
    #
    if 'L' in PlatNames[field_data[3]]:
        bands = ['CA', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2']
        cols = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF00FF', '#007700', '#003300']
        bandNames = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'NIR', 'SWIR 1', 'SWIR2']
        mark = ['o', '^', 's', '+', 'X', 'D', '*']
        markY = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596]
        textY = [0.825, 0.785, 0.745, 0.705, 0.665, 0.625, 0.585]
    else:
        bands = ['CA', 'blue', 'green', 'red', 'RE1', 'RE2', 'RE3', 'nir_1', 'nir_2', 'swir_2', 'swir_3']
        cols = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF0077', '#FF7777', '#FF7700', '#FF00FF', '#FF0077', '#007700', '#003300']
        bandNames = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'Red Edge 1', 'Red Edge 2', 'Red Edge 3', 'NIR 1', 'NIR 2', 'SWIR 2', 'SWIR 3']
        mark = ['o', '^', 's', '+', '+', '+', '+', 'X', 'X', 'D', '*']
        markY = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596, 0.544, 0.492, 0.440, 0.388]
        textY = [0.825, 0.785, 0.745, 0.705, 0.665, 0.625, 0.585, 0.545, 0.505, 0.465, 0.425]

    #
    # Setup plot
    #
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5.5, 5.5))
    #fig.suptitle('Landsat 8 SR comparison with field data')
    plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)

    #
    # Define plot limits and stretch, based on these limits
    #
    plt.xlim(plot_scale[0], plot_scale[1])
    plt.ylim(plot_scale[2], plot_scale[3])
    x_stretch = (plot_scale[1]-plot_scale[0])
    y_stretch = (plot_scale[3]-plot_scale[2])

    # Loop over each band
    for i in range(len(bands)):
        # Plot previous data as black dots
        plt.scatter(prev_data[prev_data.BAND == bands[i]].fieldmean,
                    prev_data[prev_data.BAND == bands[i]].satmean,
                    marker='.', 
                    color='black',
                    s=5, linewidth=1)

        # Plot today's data as coloured symbols
        plt.scatter(today_data[today_data.BAND == bands[i]].fieldmean,
                    today_data[today_data.BAND == bands[i]].satmean,
                    marker=mark[i], 
                    color=cols[i],
                    s=70, linewidth=2)

        # Plot coloured markers for legend in top-left area
        plt.scatter((0.05*x_stretch)+plot_scale[0], 
                    (markY[i]*y_stretch)+plot_scale[2], 
                    marker=mark[i], 
                    s=70, linewidth=1, 
                    facecolors=cols[i], 
                    edgecolors=cols[i])

        # Plot labels for each band to go with legend markers
        plt.figtext(0.21, textY[i], bandNames[i], color=cols[i])

    # Plot median errorbar
    plt.errorbar(x=0.05*x_stretch,y=0.96*y_stretch, xerr=prev_today_data.fieldstd.median(),yerr=prev_today_data.satstd.median(), linewidth=1, color='#000000',fmt='.', mec='#000000', capsize=1)
    plt.figtext(0.27*x_stretch, 1.08*y_stretch, "Median error", color='#000000')

    # Calculate best fit and report parameters in bottom-right
    slope, intercept, r_value, p_value, std_err = linregress(prev_today_data.satmean, prev_today_data.fieldmean)
    plt.figtext(0.50, 0.19, "R$^2$ coefficient = "+str(round(r_value**2, 3))+"\nslope = "+str(round(slope, 3))+"\nintercept = "+str(round(intercept, 3))+"\nstandard error = "+str(round(std_err, 3)))

    # Plot straight line that goes between (0,0) and (1,1)
    p1, p2 = [0, 1], [0, 1]
    plt.plot(p1, p2)

    plt.title(field_data[0]+' '+field_data[1]+' '+PlatNamesSpace[field_data[3]])
    plt.xlabel('Field Site Surface Reflectance')
    plt.ylabel('Satellite Surface Reflectance')

    compPlot = '../../../site-report/'+formDate+'-'+field_data[0]+'/OverallComparison-'+formDate+'-'+field_data[0]+'.png'
    if not os.path.exists(compPlot):
        plt.savefig(compPlot, dpi=300)
        print('New Figure Saved')

def dual_plot(PlatNames, PlatNamesSpace, field_data, prev_data1, today_data1, prev_today_data1, prev_data2, today_data2, prev_today_data2, formDate):
    #
    # MAKE DUAL OVERPASS OVERALL SUMMARY PLOT
    #
    plot_scale = [0.0, 0.8, 0.0, 0.8]

    #
    # Set up parameters, based on whether we are plotting Landsat or Sentinel data
    #
    if 'L' in PlatNames[field_data[3]]:
        bands1 = ['CA', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2']
        cols1 = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF00FF', '#007700', '#003300']
        bandNames1 = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'NIR', 'SWIR 1', 'SWIR 2']
        mark1 = ['o', '^', 's', '+', 'X', 'D', '*']
        markY1 = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596]
        textY1 = [0.717, 0.675, 0.633, 0.591, 0.549, 0.507, 0.465]

        if 'S' in PlatNames[field_data[3]]:
            bands2 = ['CA', 'blue', 'green', 'red', 'RE1', 'RE2', 'RE3', 'nir_1', 'nir_2', 'swir_2', 'swir_3']
            cols2 = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF0077', '#FF7777', '#FF7700', '#FF00FF', '#FF0077', '#007700', '#003300']
            bandNames2 = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'Red Edge 1', 'Red Edge 2', 'Red Edge 3', 'NIR 1', 'NIR 2', 'SWIR 2', 'SWIR 3']
            mark2 = ['o', '^', 's', '+', '+', '+', '+', 'X', 'X', 'D', '*']
            markY2 = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596, 0.544, 0.492, 0.440, 0.388]
            textY2 = [0.717, 0.675, 0.633, 0.591, 0.549, 0.507, 0.465, 0.425, 0.385, 0.345, 0.305]
        else:
            bands2 = ['CA', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2']
            cols2 = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF00FF', '#007700', '#003300']
            bandNames2 = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'NIR', 'SWIR 1', 'SWIR 2']
            mark2 = ['o', '^', 's', '+', 'X', 'D', '*']
            markY2 = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596]
            textY2 = [0.717, 0.675, 0.633, 0.591, 0.549, 0.507, 0.465]

    else:
        bands1 = ['CA', 'blue', 'green', 'red', 'RE1', 'RE2', 'RE3', 'nir_1', 'nir_2', 'swir_2', 'swir_3']
        cols1 = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF0077', '#FF7777', '#FF7700', '#FF00FF', '#FF0077', '#007700', '#003300']
        bandNames1 = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'Red Edge 1', 'Red Edge 2', 'Red Edge 3', 'NIR 1', 'NIR 2', 'SWIR 2', 'SWIR 3']
        mark1 = ['o', '^', 's', '+', '+', '+', '+', 'X', 'X', 'D', '*']
        markY1 = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596, 0.544, 0.492, 0.440, 0.388]
        textY1 = [0.717, 0.675, 0.633, 0.591, 0.549, 0.507, 0.465, 0.425, 0.385, 0.345, 0.305]

        bands2 = ['CA', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2']
        cols2 = ['#0077FF', '#0000FF', '#00FF00', '#FF0000', '#FF00FF', '#007700', '#003300']
        bandNames2 = ['Coastal Aerosol', 'Blue', 'Green', 'Red', 'NIR', 'SWIR 1', 'SWIR 2']
        mark2 = ['o', '^', 's', '+', 'X', 'D', '*']
        markY2 = [0.908, 0.856, 0.804, 0.752, 0.700, 0.648, 0.596]
        textY2 = [0.717, 0.675, 0.633, 0.591, 0.549, 0.507, 0.465]

    #
    # Setup plot
    #
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10.5, 5.5))
    #fig.suptitle('Landsat 8 SR comparison with field data')
    plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)

    #
    # Define plot limits and stretch, based on these limits
    #
    axes[0].set_xlim(plot_scale[0], plot_scale[1])
    axes[0].set_ylim(plot_scale[2], plot_scale[3])
    axes[1].set_xlim(plot_scale[0], plot_scale[1])
    axes[1].set_ylim(plot_scale[2], plot_scale[3])
    x_stretch = (plot_scale[1]-plot_scale[0])
    y_stretch = (plot_scale[3]-plot_scale[2])

    # Loop over each band
    for i in range(len(bands1)):
        # Plot previous data as black dots
        axes[0].scatter(prev_data1[prev_data1.BAND == bands1[i]].fieldmean,
                    prev_data1[prev_data1.BAND == bands1[i]].satmean,
                    marker='.',
                    color='black',
                    s=5, linewidth=1)

        # Plot today's data as coloured symbols
        axes[0].scatter(today_data1[today_data1.BAND == bands1[i]].fieldmean,
                    today_data1[today_data1.BAND == bands1[i]].satmean,
                    marker=mark1[i],
                    color=cols1[i],
                    s=70, linewidth=2)

        # Plot coloured markers for legend in top-left area
        axes[0].scatter((0.05*x_stretch)+plot_scale[0],
                    (markY1[i]*y_stretch)+plot_scale[2],
                    marker=mark1[i],
                    s=70, linewidth=1,
                    facecolors=cols1[i],
                    edgecolors=cols1[i])

        # Plot labels for each band to go with legend markers
        axes[0].text(0.1*x_stretch, textY1[i], bandNames1[i], color=cols1[i])

    for i in range(len(bands2)):
        # Plot previous data as black dots
        axes[1].scatter(prev_data2[prev_data2.BAND == bands2[i]].fieldmean,
                    prev_data2[prev_data2.BAND == bands2[i]].satmean,
                    marker='.',
                    color='black',
                    s=5, linewidth=1)

        # Plot today's data as coloured symbols
        axes[1].scatter(today_data2[today_data2.BAND == bands2[i]].fieldmean,
                    today_data2[today_data2.BAND == bands2[i]].satmean,
                    marker=mark2[i],
                    color=cols2[i],
                    s=70, linewidth=2)

        # Plot coloured markers for legend in top-left area
        axes[1].scatter((0.05*x_stretch)+plot_scale[0],
                    (markY2[i]*y_stretch)+plot_scale[2],
                    marker=mark2[i],
                    s=70, linewidth=1,
                    facecolors=cols2[i],
                    edgecolors=cols2[i])

        # Plot labels for each band to go with legend markers
        axes[1].text(0.1*x_stretch, textY2[i], bandNames2[i], color=cols2[i])



    # Plot median errorbar
    axes[0].errorbar(x=0.05*x_stretch,y=0.96*y_stretch, xerr=prev_today_data1.fieldstd.median(),yerr=prev_today_data1.satstd.median(), linewidth=1, color='#000000',fmt='.', mec='#000000', capsize=1)
    axes[0].text(0.1*x_stretch, 0.95*y_stretch, "Median error", color='#000000')
    axes[1].errorbar(x=0.05*x_stretch,y=0.96*y_stretch, xerr=prev_today_data2.fieldstd.median(),yerr=prev_today_data2.satstd.median(), linewidth=1, color='#000000',fmt='.', mec='#000000', capsize=1)
    axes[1].text(0.1*x_stretch, 0.95*y_stretch, "Median error", color='#000000')

    # Calculate best fit and report parameters in bottom-right
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(prev_today_data1.satmean, prev_today_data1.fieldmean)
    axes[0].text(0.45, 0.1, "R$^2$ coefficient = "+str(round(r_value1**2, 3))+"\nslope = "+str(round(slope1, 3))+"\nintercept = "+str(round(intercept1, 3))+"\nstandard error = "+str(round(std_err1, 3)))
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(prev_today_data2.satmean, prev_today_data2.fieldmean)
    axes[1].text(0.45, 0.1, "R$^2$ coefficient = "+str(round(r_value2**2, 3))+"\nslope = "+str(round(slope2, 3))+"\nintercept = "+str(round(intercept2, 3))+"\nstandard error = "+str(round(std_err2, 3)))

    # Plot straight line that goes between (0,0) and (1,1)
    p1, p2 = [0, 1], [0, 1]
    axes[0].plot(p1, p2)
    axes[1].plot(p1, p2)

    axes[0].set_title(field_data[0]+' '+field_data[1]+' '+PlatNamesSpace[field_data[3]])
    axes[0].set_xlabel('Field Site Surface Reflectance')
    axes[0].set_ylabel('Satellite Surface Reflectance')
    axes[1].set_title(field_data[0]+' '+field_data[1]+' '+PlatNamesSpace[field_data[6]])
    axes[1].set_xlabel('Field Site Surface Reflectance')
    #axes[1].set_ylabel('Satellite Surface Reflectance')

    compPlot = '../../../site-report/'+formDate+'-'+field_data[0]+'/OverallComparison-'+formDate+'-'+field_data[0]+'.png'
    if not os.path.exists(compPlot):
        plt.savefig(compPlot, dpi=300)
        print('New Figure Saved')

