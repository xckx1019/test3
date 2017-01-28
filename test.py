from PIL import Image
import random
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os



cropped_num = []


b = np.load('random_10.npy')
spath = ('C:/temp/cropped_10')
a = []
a = os.listdir(spath)
print b[0]
'''
for i in range(1338):
    im = cv2.imread(os.path.join(spath, a[i]))
    myVariable = b[i][0]
    myVariable2 = b[i][1]
    cv2.imwrite(a[i].replace("_cropped", "_QF10_CropX{var1}_CropY{var2}").format(var1=myVariable, var2=myVariable2) + '.png',im)
'''