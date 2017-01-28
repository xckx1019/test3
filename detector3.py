from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def jpeg_detector_3(userinput):
    im = Image.open(userinput).convert('L')
    pix = im.load()
    r, c = im.size

    arr_h = np.zeros((31, 32))
    arr_v = np.zeros((32, 31))
    sum_h = np.zeros((c/32, r/32))
    sum_v = np.zeros((c/32, r/32))

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
            plt.subplot(1, 2, 1)
            plt.imshow(fft, interpolation='none')
            if sum(fft[1:16, 0]) == 0:
                sum1 = 0
            else:
                #sum1 = (fft[3, 0] + fft[7, 0] + fft[11, 0]) / sum(fft[1:16, 0]) #check with Luca
                sum1 = (fft[4, 0] + fft[8, 0] + fft[12, 0]) / sum(fft[1:16, 0])

            sum_h[col][row] = sum1
    print sum_h
    #plt.subplot(1, 2, 1)
    #plt.imshow(sum_h)


    #vertical
    for col in xrange(0, c/32):
        for row in xrange(0, r/32):
            for i in xrange(32):
                for j in xrange(31):

                    v1 = pix[row * 32 + i, col * 32 + j + 1]
                    v2 = pix[row * 32 + i, col * 32 + j]
                    v = v1 - v2
                    arr_v[i][j] = v

            arr_v = np.abs(arr_v)

            fft2 = np.abs(np.fft.fft2(arr_v, [32, 32]))  # FFT of vertical gradient
            plt.subplot(1, 2, 2)
            plt.imshow(fft2, interpolation='none')
            plt.show()
            if sum(fft2[0, 1:16]) == 0:
                sum2 = 0
            else:
                #sum2 = (fft2[0, 3] + fft2[0, 7] + fft2[0, 11]) / sum(fft2[0, 1:16]) Ask Luca
                sum2 = (fft2[0, 4] + fft2[0, 8] + fft2[0, 12]) / sum(fft2[0, 1:16])

            sum_v[col][row] = sum2
    print sum_v
    #plt.subplot(1, 2, 2)
    #plt.imshow(sum_v)
    #plt.show()

    myarray2 = np.asarray(zip(sum_h, sum_v))
    return myarray2

#userinput = raw_input('Enter the name of a image file you want to read: ')
userinput = "checker.jpg"
A = jpeg_detector_3(userinput);
print A