from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
from operator import add

def load_3(userinput):
#horizontal
    im = Image.open(userinput).convert('L')
    pix = np.array(im).astype(np.float)
    r, c = pix.shape

    if r < c:
        # rotate the image
        pix = np.rot90(pix)
        r, c = pix.shape

    arr_h = np.zeros((31, 32))
    arr_v = np.zeros((32, 31))
    sum_h = np.zeros((c / 32, r / 32))
    sum_v = np.zeros((c / 32, r / 32))
    for row in xrange(0, r/32):
        for col in xrange(0, c/32):
            for j in xrange(32):
                for i in xrange(31):

                        h1 = pix[row * 32 + i + 1, col * 32 + j]
                        h2 = pix[row * 32 + i, col * 32 + j]
                        h = h1 - h2
                        arr_h[i][j] = h

            fft = np.abs(np.fft.fft2(arr_h, [32, 32]))  #FFT of horizontal gradient

            if sum(fft[1:16, 0]) == 0:
                    sum1 = 0
            else:
                    sum1 = (fft[3, 0] + fft[7, 0] + fft[11, 0]) / sum(fft[1:16, 0])

                    sum_h[col][row] = sum1

    myarray = np.array(sum_h)
    xmin, xmax, ymin, ymax = 0, 383, 0, 511
    extent = xmin, xmax, ymin, ymax
    plt.subplot(1, 2, 1)
    plt.imshow(im, interpolation='nearest', cmap=plt.cm.gray, extent=extent)
    plt.imshow(myarray, cmap=plt.cm.jet, alpha=0.5, interpolation='bilinear', extent=extent)
    plt.autoscale()

    for col in xrange(0, c / 32):
        for row in xrange(0, r / 32):
            for i in xrange(32):
                for j in xrange(31):
                        v1 = pix[row * 32 + i, col * 32 + j + 1]
                        v2 = pix[row * 32 + i, col * 32 + j]
                        v = v1 - v2
                        arr_v[i][j] = v

            fft2 = np.abs(np.fft.fft2(arr_v))  # FFT of vertical gradient

            if sum(fft2[0, 1:16]) == 0:
                    sum2 = 0
            else:
                    sum2 = (fft2[0, 3] + fft2[0, 7] + fft2[0, 11]) / sum(fft2[0, 1:16])

                    sum_v[col][row] = sum2
        #print sum_H

    myarray2 = np.array(sum_v)
    xmin, xmax, ymin, ymax = 0, 383, 0, 511
    extent = xmin, xmax, ymin, ymax
    plt.subplot(1, 2, 2)
    plt.imshow(im, interpolation='nearest', cmap=plt.cm.gray, extent=extent)
    plt.imshow(myarray2, cmap=plt.cm.jet, alpha=0.5, interpolation='bilinear', extent=extent)
    plt.autoscale()
   # plt.show()
    myarray3 = np.asarray(zip(sum_h, sum_v))
    combined = (myarray + myarray2)/2.0
    g = np.asarray(dtype=np.dtype('float'), a=combined)
    max_g = np.min(np.min(g))
    g = imresize(g, pix.shape, interp='nearest')
    #print g.shape, combined.shape
    i = Image.fromarray(g)
    #i.save('my.png')
    print i.size
    plt.imshow(i)
    i.show()
    return myarray3

userinput = raw_input('Enter the name of a image file you want to read: ')
A = load_3(userinput);
print A
