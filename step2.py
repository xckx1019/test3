from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im = Image.open('I_50.jpg').convert('L') #load gray image
pix = im.load()
I, J = im.size
#initialize the array for 32*32 size of blocks
arr_H = np.zeros((31, 32))  #arr for horizontal
arr_V = np.zeros((32, 31))  #arr for vertical
sum_H = np.zeros((J/32, I/32))
sum_V = np.zeros((J/32, I/32))
sum3 = 0
#horizontal
for row in range(0, I/32):
        for col in range(0, J/32):
                for j in range(32):
                          for i in range(31):

                                    H1 = pix[row * 32 + i + 1, col * 32 + j]
                                    H2 = pix[row * 32 + i, col * 32 + j]
                                    H = H1 - H2
                                    arr_H[i][j] = H

                fft = np.abs(np.fft.fft2(arr_H, [32, 32]))  #FFT of horizontal gradient
                #plt.imshow(fft)
                #plt.show()
                sum1 = (fft[3, 0] + fft[7, 0] + fft[11, 0]) / sum(fft[1:16, 0])

                sum_H[col][row] = sum1
#print sum_H

#vertical
for col in range(0, J/32):
    for row in range(0, I/32):
        for i in range(32):
            for j in range(31):

                V1 = pix[row * 32 + i, col * 32 + j + 1]
                V2 = pix[row * 32 + i, col * 32 + j]
                V = V1 - V2
                arr_V[i][j] = V

            fft2 = np.abs(np.fft.fft2(arr_V))  # FFT of vertical gradient
            sum2 = (fft2[0, 3] + fft2[0, 7] + fft2[0, 11]) / sum(fft2[0, 1:16])

        sum_V[col][row] = sum2
#print sum_V

myarray2 = np.asarray(zip(sum_H, sum_V))
print myarray2