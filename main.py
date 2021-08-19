import os
import matplotlib.pyplot as plt
import numpy as np
import skimage as sk
from skimage import io
from skimage import transform
from skimage import util
from skimage.util.dtype import img_as_ubyte, img_as_uint

def overlay(image):
    inverted_img = util.invert(image)
    #plt.text(-0.5, 0.5, '1', color = abs(picture[0][0] - 255) / 255)
    plt.text(-0.5, 0.5, '1', color = inverted_img[0][0] / 255)
    plt.text(4.5, 5.5, '1', color = inverted_img[0][0] / 255)


def save_and_display(image, name):
    io.imsave(fname = name + '.png', arr = image)
    io.imshow(image)
    plt.show()

def main():
    # print(sk.__version__)
    # print(path)

    path = '/Users/alecgoedinghaus/Documents/Personal Coding Projects/Image Numbering/minecraft_bust.png'
    bust = io.imread(path)

    # rescale bust from 320x320 to 32x32
    rescaled_bust = transform.downscale_local_mean(bust, (10, 10, 1), cval = 1)
    rescaled_bust = img_as_ubyte(rescaled_bust / 255)
    print(rescaled_bust)
    print(rescaled_bust.shape)


    save_and_display(rescaled_bust, 'output')

main()