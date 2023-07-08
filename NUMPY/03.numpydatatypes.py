# default data types of python
# strings 
# integer
# float 
# boolean
# complex
# extra data TYPES IN NUMPY
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of meamory for other type(void)

# checking the type of an array data type

import numpy as np
# arr = np.array([1,3,4,5])
# print(arr.dtype)

arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)

# if a value cannot be converted or type cast into any other datatype then will raise error

# arr = np.array(['a','2','3'], dtype='i')

# converting data type on existing arrays

arr = np.array([1.1,2.1,3.4])

# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)

# changing data type from integer to boolean

arra = np.array([1,0,3])
newarr = arra.astype(bool)

print(newarr)
print(newarr.dtype)