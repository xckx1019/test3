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

seven_seven = 7 * np.ones((1338, 2))
x_c = seven_seven - f1
error_sum = 0
for m in range(1338):
    p = x_c[m][0] - l[m][0]
    q = x_c[m][1] - l[m][1]
    error = (p**2 + q**2)**0.5
    error_sum = error_sum + error
print error_sum

a10 = 35.0
a30 = 189.0
a50 = 488.0
a70 = 1337.0
a90 = 3104.50069359
a100 = 5492.21401389

a1_10 = 8.0
a1_30 = 0.0
a1_50 = 0.0
a1_70 = 1.0
a1_90 = 433.626398898
a1_100 = 5601.5865475

x = (np.array([a10, a30, a50, a70, a90, a100]))/1338.0
x1 = (np.array([a1_10, a1_30, a1_50, a1_70, a1_90, a1_100]))/1338.0
y = [10, 30, 50, 70, 90, 100]

plt.figure(1)
plt.plot(y, x)
plt.plot(y, x1)
plt.legend(('alternative1', 'alternative2'))
plt.show()