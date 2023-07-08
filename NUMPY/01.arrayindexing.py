import numpy as np

arr = np.array([1,2,4,3])

print(arr[1])#get second element from array

print(arr[2] + arr[3])#get second and third element from array and add them


# accessing 2-D arrays

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('second element on 1st row: ',arr[0,1])
print('5th element on 2nd row: ', arr[1,4])


# accessing 3-D element
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])#third element of second arrray of first array

# use negative indexing to access an array form the end
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('last element from 2nd dim: ',arr[1,-1])