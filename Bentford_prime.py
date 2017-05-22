import numpy as np
import matplotlib.pyplot as plt

dimension = 1000000
a = np.ones(dimension)
a[0] = 0
a[1] = 0

for i in range(3, dimension):
    for d in range(2, i/2):
	if i%d == 0:
	    a[i] = 0
	    break

bit = 1
count = np.zeros(9)
for i in range(1, dimension-1):
    if a[i] == 1:
	while (i/bit != 0):
	    bit = bit*10
        num = i/(bit/10)
	count[num-1]+=1

total = np.sum(count)
for i in range(0,9):
    count[i] /= total

xi = [1,2,3,4,5,6,7,8,9]
yi = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
plt.plot(xi, count, 'b')	
plt.plot(xi, yi, 'r')
titl = 'prime under' + str(dimension)
plt.title(titl)
plt.show()
