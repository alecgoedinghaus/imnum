import os
import matplotlib.pyplot as plt
import skimage as sk
from skimage import io

path = '/Users/alecgoedinghaus/Documents/Personal Coding Projects/Image Numbering/minecraft_bust.png'
bust = io.imread(path)

def display(picture, name):
    io.imsave(fname = name + '.png', arr = picture)
    io.imshow(picture)
    plt.show()

def main():
    print(sk.__version__)
    print(path)

    display(bust, 'output')

main()