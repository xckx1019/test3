from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def jpeg_detector_1(userinput):
    im = Image.open(userinput).convert('L')
    pix = im.load()
    M, N = im.size
    arr = np.zeros((M/8 - 1, N/8 - 1))
    arr2 = np.zeros((M/8 - 1, N/8 - 1))

    for i in range(0, M/8 - 1):
        for j in range(0, N/8 - 1):
            A = pix[i * 8 + 3, j * 8 + 3]
            B = pix[i * 8 + 4, j * 8 + 3]
            C = pix[i * 8 + 3, j * 8 + 4]
            D = pix[i * 8 + 4, j * 8 + 4]

            E = pix[i * 8 + 7, j * 8 + 7]
            F = pix[i * 8 + 8, j * 8 + 7]
            G = pix[i * 8 + 7, j * 8 + 8]
            H = pix[i * 8 + 8, j * 8 + 8]

            Z = abs(A - B - C + D)
            Z2 = abs(E - F - G + H)
            arr[i][j] = Z
            arr2[i][j] = Z2

    #print arr
    #print arr2


    h1, binEdges = np.histogram(arr, bins=np.arange(0, 256), normed=True)
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    plt.subplot(131), plt.plot(bincenters, h1, '-')

    h2, binEdges = np.histogram(arr2, bins=np.arange(0, 256), normed=True)
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    plt.subplot(132), plt.plot(bincenters, h2, '-')

    h3 = abs(h1 - h2)
    k = sum(h3)
    #print k

    plt.subplot(133), plt.plot(bincenters, h3, '-')
    plt.show()
    return k

userinput = raw_input('Enter the name of a image file a you want to read: ')
A = jpeg_detector_1(userinput);
print A