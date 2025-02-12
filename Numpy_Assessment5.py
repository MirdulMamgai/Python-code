#Convert a 1D array of 12 elements into a 3x4 matrix.

import numpy as np
arr=np.arange(1,13)
np=np.reshape(arr,(3,4))
print(np)