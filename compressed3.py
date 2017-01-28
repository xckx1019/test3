from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os

def jpeg_detector_3(userinput):
    im = Image.open(userinput).convert('L')
    #pix = im.load()
    pix = np.array(im).astype(np.float)
    r, c = pix.shape

    if r < c:
        # rotate the image
        pix = np.rot90(pix)
        r, c = pix.shape

    arr_h = np.zeros((31, 32))
    sum_h = np.zeros((c/32, r/32))

    #horizontal
    for row in xrange(0, r/32):
        for col in xrange(0, c/32):
            for j in xrange(32):
                for i in xrange(31):

                    h1 = pix[row * 32 + i + 1, col * 32 + j]
                    h2 = pix[row * 32 + i, col * 32 + j]
                    h = h1 - h2
                    arr_h[i][j] = h
            arr_h = np.abs(arr_h)
            fft = np.abs(np.fft.fft2(arr_h, [32, 32]))  #FFT of horizontal gradient
            #plt.imshow(fft)
            #plt.show()
            if sum(fft[1:16, 0]) == 0:
                sum1 = 0
            else:
                sum1 = (fft[4, 0] + fft[8, 0] + fft[12, 0]) / sum(fft[1:16, 0])

            sum_h[col][row] = sum1
    #print sum_H
    #plt.imshow(sum_h)
    #plt.show()
    myarray2 = np.asarray(sum_h)
    return myarray2

spath ="C:/temp/compress_100"
a = []
a = os.listdir(spath)
#print a

source = "C:/temp/compress_100/"
list_k = []
for i in a:
    userinput = source + i
    A = jpeg_detector_3(userinput);
    list_k.append(A)
b = np.array(list_k)
np.save('detector3_compressed_100.npy', b)
print b