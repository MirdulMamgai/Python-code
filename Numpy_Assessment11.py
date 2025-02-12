#Given an array arr = np.array([5, 15, 25, 35, 45, 55]), filter out elements greater than 30.
import numpy as np
arr = np.array([5, 15, 25, 35, 45, 55])
arr1=arr[arr>30]
print(arr1)