import argparse
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform, util
from skimage.util.dtype import img_as_ubyte
from matplotlib.backends.backend_pdf import PdfPages

def get_like_colors(image, dimension, tolerance):
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

    print('Found ' + str(iterator) + ' unique pixel colors')
    return values, iterator

def overlay(image, values, num_plots, dimension, expand, font_size):
    inverted_img = util.invert(image)

    if not expand:
        for i in range(dimension[1]):
            for j in range(dimension[0]):
                plt.text(-0.375 + i, 0.25 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = font_size)
        
        return 0

    else:
        # Unnecessary warning (but probably actually matters for large images)
        plt.rcParams.update({'figure.max_open_warning': num_plots + 1})

        figs = []
        for plot_num in range(1, num_plots + 1):
            fig, axs = plt.subplots(1)
            for i in range(dimension[1]):
                for j in range(dimension[0]):
                    if int(values[j, i]) == plot_num:
                        axs.set_title(plot_num)
                        axs.imshow(image)
                        axs.text(-0.375 + i, 0.25 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = 6)
            figs.append(fig)

        return figs

def save_as_pdf(image, name, figs):
    if figs == 0:
        io.imshow(image)
        plt.savefig(name + '.pdf', bbox_inches = 'tight')
    else:
        with PdfPages(name + '_expanded.pdf') as pdf:
            for fig in figs:
                plt.figure(fig)
                pdf.savefig()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'Image file to be analyzed')
    parser.add_argument('-f', '--font_size', type = int, default = 6, help = 'Font size for the displayed numbers (default: 6)')
    parser.add_argument('-e', '--expand', action = 'store_true', help = 'Break up each pixel numbering into its own page')
    parser.add_argument('-s', '--scale', type = int, default = 0, help = 'Scale factor for the image, can only go smaller (default: 1)')
    parser.add_argument('-t', '--tolerance', type = int, default = 25, help = 'Tolerance for similar pixels. 0 for exact match (default: 25)')
    args = parser.parse_args()

    file = args.file
    font_size = args.font_size
    scale = args.scale
    tol = args.tolerance
    expand = args.expand
    image = io.imread(file)

    if scale != 0:
        image = transform.downscale_local_mean(image, (scale, scale, 1), cval = 1)
        image = img_as_ubyte(image / 255)

    length = image.shape[0]
    height = image.shape[1]

    values, num_plots = get_like_colors(image, (length, height), tol)
    figs = overlay(image, values, num_plots, (length, height), expand, font_size)
    save_as_pdf(image, 'output', figs)

main()