import os
import matplotlib.pyplot as plt
import numpy as np
import skimage as sk
from skimage import io, transform, util
from skimage.util.dtype import img_as_ubyte, img_as_uint

def get_like_colors(image, dimension, tolerance = 100):
    values = np.zeros([dimension[0], dimension[1]])
    iterator = 0

    for i in range(dimension[0]):
        for j in range(dimension[1]):
            # If values != 0, then this pixel's group has been numbered
            if values[i, j] == 0:
                iterator += 1
                for k in range(dimension[0]):
                    for l in range(dimension[1]):
                        dist = [abs(int(image[i, j, rgb]) - int(image[k, l, rgb])) for rgb in range(3)]
                        if all(dist_i < tolerance for dist_i in dist):
                            values[i, j] = iterator
                            values[k, l] = iterator

    return values, iterator

def overlay(image, values, dimension):
    inverted_img = util.invert(image)

    # Make this display each different number on separate plots
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            plt.text(-0.5 + i, 0.5 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = 6)

def save_and_display(image, name):
    io.imshow(image)
    plt.savefig(name + '_plt.png', bbox_inches = 'tight')
    plt.show()

def main():
    path = '/Users/alecgoedinghaus/Documents/Personal Coding Projects/Image Numbering/minecraft_bust.png'
    bust = io.imread(path)

    # rescale bust from 320x320 to 32x32
    rescaled_bust = transform.downscale_local_mean(bust, (10, 10, 1), cval = 1)
    rescaled_bust = img_as_ubyte(rescaled_bust / 255)

    values, num_plots = get_like_colors(rescaled_bust, (32, 32), tolerance = 25)
    overlay(rescaled_bust, values, (32, 32))
    save_and_display(rescaled_bust, 'output')

main()