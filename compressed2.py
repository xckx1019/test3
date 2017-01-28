from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt


def jpeg_detector_2(userinput):
    im = Image.open(userinput).convert('L')
    pix = im.load()
    M, N = im.size

    p_max = 0
    q_max = 0
    e_max = 0
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
            if E[p, q] >= e_max:
                e_max = E[p, q]
                q_max = q
                p_max = p

    return [q_max, p_max]

spath ="C:/temp/cropped_100"
a = []
a = os.listdir(spath)
#print a

source = "C:/temp/cropped_100/"
list_k = []
for i in a:
    userinput = source + i
    A = jpeg_detector_2(userinput);
    list_k.append(A)
b = np.array(list_k)
np.save('detector2_cropped_100.npy', b)
print b




