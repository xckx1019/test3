from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def jpeg_detector_1(userinput):
    im = Image.open(userinput).convert('L')
    pix = im.load()
    M, N = im.size
    arr = np.zeros((M / 8 - 1, N / 8 - 1))
    arr2 = np.zeros((M / 8 - 1, N / 8 - 1))
    p_max = 0
    q_max = 0
    E_max = 0
    E = np.zeros((8, 8))

    for p in range(0, 8):
        for q in range(0, 8):
            for i in range(0, M/8 - 1):
                for j in range(0, N/8 - 1):

                    A = pix[i * 8 + p, j * 8 + q]
                    B = pix[i * 8 + p + 1, j * 8 + q]
                    C = pix[i * 8 + p, j * 8 + q + 1]
                    D = pix[i * 8 + p + 1, j * 8 + q + 1]

                    Z = abs(A - B - C + D)
                    E[p, q] = E[p, q] + Z
            a = E.sum(axis=0)
            b = E.sum(axis=1)
            c = np.argmax(a)
            d = np.argmax(b)
            #p_max = d
            #q_max = c

            #if E[p, q] >= E_max:
              #  E_max = E[p, q]
               # q_max = q
               # p_max = p
    #print q_max, p_max

    p_max = d
    q_max = c
    m = p_max - 4
    n = q_max - 4

    if (p_max and q_max) >= 4:
        block = 0
    else:
        block = 1
    for i in range(block, M / 8 - 1):
        for j in range(block, N / 8 - 1):
            A = pix[i * 8 + m, j * 8 + n]
            B = pix[i * 8 + m + 1, j * 8 + n]
            C = pix[i * 8 + m, j * 8 + n + 1]
            D = pix[i * 8 + m + 1, j * 8 + n + 1]

            E = pix[i * 8 + p_max, j * 8 + q_max]
            F = pix[i * 8 + p_max + 1, j * 8 + q_max]
            G = pix[i * 8 + p_max, j * 8 + q_max + 1]
            H = pix[i * 8 + p_max + 1, j * 8 + q_max + 1]

            Z = abs(A - B - C + D)
            Z2 = abs(E - F - G + H)
            arr[i][j] = Z
            arr2[i][j] = Z2

    h1, binEdges = np.histogram(arr, bins=np.arange(0, 256), normed=True)
    bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

    h2, binEdges = np.histogram(arr2, bins=np.arange(0, 256), normed=True)
    bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

    h3 = abs(h1 - h2)
    k = sum(h3)

    return [k, [m, n], [p_max, q_max]]

#userinput = raw_input('Enter the name of a image file a you want to read: ')
a = jpeg_detector_1("I_95_crop.png")
print a
