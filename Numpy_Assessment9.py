#Generate a 4x4 matrix of random numbers between 0 and 1.
#Find its mean, median, and standard deviation.

import numpy as np
arr=np.random.randint(0,2,(4,4))
print("Mean:",np.mean(arr,axis=0))
print("Mean:",np.mean(arr,axis=1))
print("Median:",np.median(arr,axis=0))
print("Median:",np.median(arr,axis=1))
print("StandardDeviation:",np.std(arr,axis=0))
print("StandardDeviation:",np.std(arr,axis=1))
