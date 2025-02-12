#Find the maximum and minimum values in a 3x3 matrix along with their indices.

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print("Maximum value verically",np.max(arr,axis=0))
print("Indice of maximum value is",np.argmax(arr,axis=0))
print("Maximum value horizontally",np.max(arr,axis=1))
print("Indice of maximum value is",np.argmax(arr,axis=1))
print("Minimum value verically",np.min(arr,axis=0))
print("Indice of minimum value is",np.argmin(arr,axis=0))
print("Minimum value horizontally",np.min(arr,axis=1))
print("Indice of minimum value is",np.argmin(arr,axis=1))