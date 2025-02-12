#Given an array arr = np.array([10, 20, 30, 40, 50]), retrieve:
#a) The first three elements.
#b) The last two elements.
#c) Elements from index 1 to 4 with a step of 2.

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(np.array(arr[0:3]))
print(np.array(arr[-1:-3:-1]))
print(np.array(arr[1:4:2]))