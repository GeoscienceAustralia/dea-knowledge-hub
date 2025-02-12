import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


#
# Make big RGB image out of satellite bands. Scaling is 0-3000, with anything above 3000, scaled to 3000
# This makes an RGB image that looks the same as https://maps.dea.ga.gov.au
#
def mkBigRGB(sat_bigarray):
    red_rgb = np.clip(sat_bigarray.isel(time=0).nbart_red/3000.0, 0, 1)
    green_rgb = np.clip(sat_bigarray.isel(time=0).nbart_green/3000.0, 0, 1)
    blue_rgb = np.clip(sat_bigarray.isel(time=0).nbart_blue/3000.0, 0, 1)
    rgb_image = np.stack([red_rgb, green_rgb, blue_rgb], axis=-1)
    return rgb_image

def rgb_plot(ls_sat_array, ls_sat_bigarray, s2_sat_array, s2_sat_bigarray, PlatNamesSpace, field_data, formDate):
    if field_data[3] == 'Landsat8' or field_data[3] == 'Landsat9':
        sat_array = ls_sat_array.copy()
        sat_bigarray = ls_sat_bigarray.copy()
        sat_image = mkBigRGB(sat_array)
        sat_bigimage = mkBigRGB(sat_bigarray)
        if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
            sat_array2 = s2_sat_array.copy()
            sat_bigarray2 = s2_sat_bigarray.copy()
            sat_bigimage2 = mkBigRGB(sat_bigarray2)
    
    else:
        sat_array = s2_sat_array.copy()
        sat_bigarray = s2_sat_bigarray.copy()
        sat_bigimage = mkBigRGB(sat_bigarray)
        if 'Sentinel' in field_data[6] or 'Landsat' in field_data[6]:
            sat_array2 = ls_sat_array.copy()
            sat_bigarray2 = ls_sat_bigarray.copy()
            sat_bigimage2 = mkBigRGB(sat_bigarray2)
    
    try:
        sat_bigarray2
        # Make dual plots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10.5, 5.5))
        plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)
        # Get x and y coordinates from sat_bigarray
        x_coords = sat_bigarray.x.values
        y_coords = sat_bigarray.y.values
        x_coords2 = sat_bigarray2.x.values
        y_coords2 = sat_bigarray2.y.values
    
        # Plot the RGB image using original coordinates
        axes[0].imshow(sat_bigimage, extent=[x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()])
        axes[1].imshow(sat_bigimage2, extent=[x_coords2.min(), x_coords2.max(), y_coords2.min(), y_coords2.max()])
        rect = patches.Rectangle((float(sat_array.x.min()),float(sat_array.y.min())), 100, 100, angle=0.0, fill=False, color='white', lw = 2.5)
        rect2 = patches.Rectangle((float(sat_array.x.min()),float(sat_array.y.min())), 100, 100, angle=0.0, fill=False, color='black', lw = 1)
        rect3 = patches.Rectangle((float(sat_array2.x.min()),float(sat_array2.y.min())), 100, 100, angle=0.0, fill=False, color='white', lw = 2.5)
        rect4 = patches.Rectangle((float(sat_array2.x.min()),float(sat_array2.y.min())), 100, 100, angle=0.0, fill=False, color='black', lw = 1)
        axes[0].add_patch(rect)
        axes[0].add_patch(rect2)
        axes[1].add_patch(rect3)
        axes[1].add_patch(rect4)
    
        axes[0].set_title(PlatNamesSpace[field_data[3]])
        axes[1].set_title(PlatNamesSpace[field_data[6]])
    
    except (NameError, AttributeError):
        # Make single plot
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5.5, 5.5))
        plt.tight_layout(pad=2.7, w_pad=1.0, h_pad=1.0)
        # Get x and y coordinates from sat_bigarray
        x_coords = sat_bigarray.x.values
        y_coords = sat_bigarray.y.values
    
        # Plot the RGB image using original coordinates
        axes.imshow(sat_bigimage, extent=[x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()])
        rect = patches.Rectangle((float(sat_array.x.min()),float(sat_array.y.min())), 100, 100, angle=0.0, fill=False, color='white', lw = 2.5)
        rect2 = patches.Rectangle((float(sat_array.x.min()),float(sat_array.y.min())), 100, 100, angle=0.0, fill=False, color='black', lw = 1)
    
        axes.add_patch(rect)
        axes.add_patch(rect2)
    
        axes.set_title(PlatNamesSpace[field_data[3]])
    
    rgbPlot = '../../../site-report/'+formDate+'-'+field_data[0]+'/RGB-'+formDate+'-'+field_data[0]+'.png'
    if not os.path.exists(rgbPlot):
        plt.savefig(rgbPlot, dpi=300)
        print('New Figure Saved')
