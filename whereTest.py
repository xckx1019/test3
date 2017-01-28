from PIL import Image
import random
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os

gt = []
for j in range(1338):
    b = random.randint(0, 7)
    c = random.randint(0, 7)
    gt.append([b, c])
print gt
np.save('random_90.npy', gt)
spath = ('C:/temp/compress_90')
a = []
a = os.listdir(spath)
for i in range(1338):
    im = cv2.imread(os.path.join(spath, a[i]))
    pix_crop = im[gt[i][0]:, gt[i][1]:]
    cv2.imwrite(a[i].replace(".jpg", "_cropped") + '.png', pix_crop)

