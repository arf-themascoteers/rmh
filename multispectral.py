import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

file_path = 'multispectral.tif'
with rasterio.open(file_path) as src:
    print("Number of Channels",src.count)
    blue_channel = src.read(1)
    green_channel = src.read(2)
    red_channel = src.read(3)
    nir_channel = src.read(4)

    show(blue_channel, cmap='gray')
    show(green_channel, cmap='gray')
    show(red_channel, cmap='gray')
    show(nir_channel, cmap='gray')

    rgb_image = np.array([red_channel, green_channel, blue_channel])
    rgb_image = rgb_image/np.max(rgb_image)
    print(rgb_image)
    show(rgb_image)


