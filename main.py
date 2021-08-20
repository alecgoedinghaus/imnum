import argparse
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform, util
from skimage.util.dtype import img_as_ubyte
from matplotlib.backends.backend_pdf import PdfPages

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

def overlay(image, values, num_plots, dimension, expand):
    inverted_img = util.invert(image)

    if not expand:
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                plt.text(-0.375 + i, 0.25 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = 6)

    else:
        figs = []
        plt.rcParams.update({'figure.max_open_warning': num_plots + 1})
        for plot_num in range(1, num_plots + 1):
            fig, axs = plt.subplots(1)
            for i in range(dimension[0]):
                for j in range(dimension[1]):
                    if int(values[j, i]) == plot_num:
                        # axs[plot_num - 1].imshow(image)
                        # axs[plot_num - 1].text(-0.375 + i, 0.25 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = 4)
                        axs.imshow(image)
                        axs.text(-0.375 + i, 0.25 + j, str(int(values[j, i])), color = inverted_img[j, i] / 255, size = 6)
            figs.append(fig)

        with PdfPages('output_multi.pdf') as pdf:
            for fig in figs:
                plt.figure(fig)
                pdf.savefig()

def save_and_display(image, name):
    io.imshow(image)
    plt.savefig(name + '.pdf', bbox_inches = 'tight')
    # plt.show()


# def expanded_display(image, values, num_plots):

#     io.imshow(image)
#     plt.savefig()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'Image file to be analyzed')
    parser.add_argument('-s', '--scale', type = int, default = 0, help = 'Scale factor for the image, leave empty for no scaling')
    parser.add_argument('-t', '--tolerance', type = int, default = 25, help = 'Tolerance for similar pixels. 0 for exact match, default 25')
    args = parser.parse_args()

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
    overlay(image, values, num_plots, (length, height), True)
    save_and_display(image, 'output')

main()