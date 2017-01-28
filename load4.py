import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('I_50.jpg').convert('L')
pix = im.load()
r, c = im.size

arr_h = np.zeros((31, 32))
arr_v = np.zeros((32, 31))
sum_h = np.zeros((c / 32, r / 32))
sum_v = np.zeros((c / 32, r / 32))
for row in xrange(0, r / 32):
    for col in xrange(0, c / 32):
        for j in xrange(32):
            for i in xrange(31):
                h1 = pix[row * 32 + i + 1, col * 32 + j]
                h2 = pix[row * 32 + i, col * 32 + j]
                h = h1 - h2
                arr_h[i][j] = h

        fft = np.abs(np.fft.fft2(arr_h, [32, 32]))  # FFT of horizontal gradient

        if sum(fft[1:16, 0]) == 0:
            sum1 = 0
        else:
            sum1 = (fft[3, 0] + fft[7, 0] + fft[11, 0]) / sum(fft[1:16, 0])

            sum_h[col][row] = sum1

myarray = np.array(sum_h)
xmin, xmax, ymin, ymax = 0, 383, 0, 511
extent = xmin, xmax, ymin, ymax
plt.subplot(2, 1, 1)
plt.imshow(im, interpolation='nearest', cmap=plt.cm.gray, extent=extent)
plt.imshow(myarray, cmap=plt.cm.jet, alpha=0.5, interpolation='bilinear', extent=extent)
plt.autoscale()