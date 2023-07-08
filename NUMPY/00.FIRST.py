# import numpy

# arr = numpy.array([1,3,4,5,6])

# print(arr)

# numpy as np
# import numpy as np
# arr = np.array([1,3,5,6,8])
# print(arr)

# checking numpy version
# print(np.__version__)

# print(type(arr))

# use tupple to create a numpy array
import numpy as np

# arr = np.array((1,2,3,4,5))

# print(arr)

# create 0-D array
a = np.array(42)
print(a.ndim)

# create 1-D array
b = np.array([1,2,3,4,5])
print(b.ndim)

# create 2-D array
c = np.array([[1,2,3],[4,5,6]])
print(c.ndim)

# create 3-D array
d = np.array([[[1,2,3],[4,5,6]],[[9,8,7],[4,5,6]]])
print(d.ndim)

# create an array witb 5 dimension and verify that it has 5 dimension
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print('number of dimensions :',arr.ndim)
