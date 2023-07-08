# shape of array is the number of element in each dimension.

# there is keyword shape that returns a tuple with each index having the numbers of corresponding elements

import numpy as np

# arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr.shape)

# arr = np.array([1,2,3,4],ndmin=5)
# print(arr)
# print('shape of array :',arr.shape)
# newarr = arr.reshape(2,1,2)

# print(newarr.base)
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)

# flattening array reshape array to single dimension

arr = np.array([[1,2,3],[2,3,4]])
newarr = arr.reshape(-1)
print(newarr)