from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def grid_position_search(userinput):
    im = Image.open(userinput).convert('L')
    pix = im.load()
    M, N = im.size
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
                    E[p,q] = E[p, q] + Z
            if E[p,q] >= E_max:
                E_max = E[p, q]
                q_max = q
                p_max = p
    print np.argmax(np.sum(E, axis=1))
    print np.argmax(np.sum(E, axis=0))
    print E

    return [p_max, q_max]




#userinput = raw_input('Enter the name of a image file a you want to read: ')
q=grid_position_search("I_95_crop.png")
print q