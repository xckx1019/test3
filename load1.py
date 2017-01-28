import numpy as np
from matplotlib import pyplot as plt

a = []
b = []
c = []
d = []
e = []
f = []

a = np.load('detector1_compressed_10.npy')
b = np.load('detector1_compressed_30.npy')
c = np.load('detector1_compressed_50.npy')
d = np.load('detector1_compressed_70.npy')
e = np.load('detector1_compressed_90.npy')
f = np.load('detector1_compressed_100.npy')
print a.min()
'''
x, binEdges = np.histogram(a)
y, binEdges = np.histogram(b)
m, binEdges = np.histogram(c)
n, binEdges = np.histogram(d)
w, binEdges = np.histogram(e)
z, binEdges = np.histogram(f)

#bincenters = (binEdges[1:]+binEdges[:-1])

plt.plot(bincenters,x,'-')
plt.plot(bincenters,y,'-')
plt.plot(bincenters,m,'-')
plt.plot(bincenters,n,'-')
plt.plot(bincenters,w,'-')
plt.plot(bincenters,z,'-')
'''


plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.plot(d)
plt.plot(e)
plt.plot(f)

plt.xlabel("Image Value")
plt.ylabel("Frequency")

plt.legend(('10', '30', '50', '70', '90', '100'))
plt.show()

'''
# fixed bin size
bins = np.arange(0, 2, 0.05) # fixed bin size

plt.xlim([min(a)-0.1, max(a)+0.1])


plt.hist(a, bins=bins, alpha=0.5, histtype='step')
plt.hist(b, bins=bins, alpha=0.5, histtype='step')
plt.hist(c, bins=bins, alpha=0.5, histtype='step')
plt.hist(d, bins=bins, alpha=0.5, histtype='step')
plt.hist(e, bins=bins, alpha=0.5, histtype='step')
plt.hist(f, bins=bins, alpha=0.5, histtype='step')
plt.title('Random Gaussian data (fixed bin size)')
plt.xlabel('variable X (bin size = 5)')
plt.ylabel('count')

plt.show()
'''