import numpy as np
from matplotlib import pyplot as plt

a = []
b = []
c = []
d = []
e = []
f = []

a = np.load('detector2_compressed_10.npy')
b = np.load('detector2_compressed_30.npy')
c = np.load('detector2_compressed_50.npy')
d = np.load('detector2_compressed_70.npy')
e = np.load('detector2_compressed_90.npy')
f = np.load('detector2_compressed_100.npy')

a1 = a[:, 1]
a2 = a[:, 0]
b1 = b[:, 1]
b2 = b[:, 0]
c1 = c[:, 1]
c2 = c[:, 0]
d1 = d[:, 1]
d2 = d[:, 0]
e1 = e[:, 1]
e2 = e[:, 0]
f1 = f[:, 1]
f2 = f[:, 0]
bins = np.arange(9)-.5
plt.subplot(2, 3, 1)
plt.hist(a1, bins, histtype='step')
plt.hist(a2, bins, histtype='step')
plt.xlabel("Compressed 10 Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.subplot(2, 3, 2)
plt.hist(b1, bins, histtype='step')
plt.hist(b2, bins, histtype='step')
plt.xlabel("Compressed 30 Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.subplot(2, 3, 3)
plt.hist(c1, bins, histtype='step')
plt.hist(c2, bins, histtype='step')
plt.xlabel("Compressed 50 Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.subplot(2, 3, 4)
plt.hist(d1, bins, histtype='step')
plt.hist(d2, bins, histtype='step')
plt.xlabel("Compressed 70 Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.subplot(2, 3, 5)
plt.hist(e1, bins, histtype='step')
plt.hist(e2, bins, histtype='step')
plt.xlabel("Compressed 90 Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.subplot(2, 3, 6)
plt.hist(f1, bins, histtype='step')
plt.hist(f2, bins, histtype='step')
plt.xlabel("No Compressed Image Value")
plt.ylabel("Frequency")
plt.legend(('1st col', '2nd col'))

plt.show()
print a.shape
