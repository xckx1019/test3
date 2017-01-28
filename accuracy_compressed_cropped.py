import numpy as np
from matplotlib import pyplot as plt


a = np.load('detector2_cropped_10.npy')
b = np.load('detector2_cropped_30.npy')
c = np.load('detector2_cropped_50.npy')
d = np.load('detector2_cropped_70.npy')
e = np.load('detector2_cropped_90.npy')
f = np.load('detector2_cropped_100.npy')

a1 = np.load('detector2_cropped_alter_10.npy')
b1 = np.load('detector2_cropped_alter_30.npy')
c1 = np.load('detector2_cropped_alter_50.npy')
d1 = np.load('detector2_cropped_alter_70.npy')
e1 = np.load('detector2_cropped_alter_90.npy')
f1 = np.load('detector2_cropped_alter_100.npy')


g = np.load('random_10.npy')
h = np.load('random_30.npy')
i = np.load('random_50.npy')
j = np.load('random_70.npy')
k = np.load('random_90.npy')
l = np.load('random_100.npy')

a10 = 1321
a30 = 1269
a50 = 1065
a70 = 642
a90 = 189
a100 = 14

a1_10 = 1336
a1_30 = 1338
a1_50 = 1338
a1_70 = 1337
a1_90 = 1213
a1_100 = 22

x = (np.array([a10, a30, a50, a70, a90, a100]))/1338.0
x1 = (np.array([a1_10, a1_30, a1_50, a1_70, a1_90, a1_100]))/1338.0
y = [10, 30, 50, 70, 90, 100]
'''
seven_seven = 7 * np.ones((1338, 2))
for m in range(1338):
    n = seven_seven[m] - c1[m]
    q = n == i[m]
    #print (a[m] == g[m]).astype(int)
    print q.astype(int)
    '''
plt.figure(1)
plt.plot(y, x)
plt.plot(y, x1)
plt.legend(('alternative1', 'alternative2'))
plt.show()


