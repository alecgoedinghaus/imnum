import os
import matplotlib.pyplot as plt
import numpy as np
import skimage as sk
from skimage import io, transform, util
from skimage.util.dtype import img_as_ubyte, img_as_uint

def get_like_colors(image, tolerance, x, y):
    values = np.zeros([x, y])
    iterator = 0

    for i in range(x):
        for j in range(y):
            # If values != 0, then this pixel's group has been numbered
            if values[i, j] == 0:
                iterator += 1
                for k in range(x):
                    for l in range(y):
                        dist = np.linalg.norm(image[i, j] - image[k, l])
                        if dist < tolerance:
                            values[i, j] = iterator
                            values[k, l] = iterator

    return values

def overlay(image, values, x, y):
    #values = get_like_colors(image, 100, x, y)
    inverted_img = util.invert(image)

    # Make this display each different number on separate plots
    for i in range(x):
        for j in range(y):
            plt.text(-0.5 + i, 0.5 + j, str(int(values[i, j])), color = inverted_img[j, i] / 255, size = 6)
        
    # plt.text(-0.5 + 5, 0.5 + 30, '1', color = inverted_img[30, 5] / 255, size = 8)

def save_and_display(image, name):
    # io.imsave(fname = name + '.png', arr = image)
    io.imshow(image)
    plt.savefig(name + '_plt.png', bbox_inches = 'tight')
    plt.show()

def main():
    path = '/Users/alecgoedinghaus/Documents/Personal Coding Projects/Image Numbering/minecraft_bust.png'
    bust = io.imread(path)

    # rescale bust from 320x320 to 32x32
    rescaled_bust = transform.downscale_local_mean(bust, (10, 10, 1), cval = 1)
    rescaled_bust = img_as_ubyte(rescaled_bust / 255)

    values = get_like_colors(rescaled_bust, 50, 32, 32)
    overlay(rescaled_bust, values, 32, 32)
    save_and_display(rescaled_bust, 'output')

main()