import argparse
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, transform, util
from skimage.util.dtype import img_as_ubyte, img_as_uint

def get_like_colors(image, dimension, tolerance = 25):
    values = np.zeros([dimension[0], dimension[1]])
    iterator = 0

    for i in range(dimension[0]):
        for j in range(dimension[1]):
            # If values != 0, then this pixel's group has been numbered
            if values[i, j] == 0:
                iterator += 1
                for k in range(dimension[0]):
                    for l in range(dimension[1]):
                        dist = [abs(int(image[i, j, rgb]) - int(image[k, l, rgb])) for rgb in range(image.shape[2])]
                        if all(dist_i <= tolerance for dist_i in dist):
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
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type = str, help = 'Image file to be analyzed')
    parser.add_argument('-s', '--scale', type = int, default = 0, help = 'Scale factor for the image, leave empty for no scaling')
    parser.add_argument('-t', '--tolerance', type = int, default = 25, help = 'Tolerance for similar pixels. 0 for exact match, default 25')

    args = parser.parse_args()
    print(args.file)

    file = args.file
    scale = args.scale
    tol = args.tolerance
    
    image = io.imread(file)

    if scale != 0:
        image = transform.downscale_local_mean(image, (scale, scale, 1), cval = 1)
        image = img_as_ubyte(image / 255)

    length = image.shape[0]
    height = image.shape[1]

    values, num_plots = get_like_colors(image, (length, height), tolerance = tol)
    overlay(image, values, (length, height))
    save_and_display(image, 'output')

main()