import numpy as np

# iterate the elements of 1-D 
arr = np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(x)
# for x in arr:
#     print(x)


# iterating 2-D arrays
arr = np.array([[1,2,3],[4,5,6]])

# iterating with different datatypes
for x in np.nditer(arr[:,::2]):
    print(x)
# for x in arr:
#     # print(x)
#     for y in x:
#         print(y)

arr = np.array([[[1,2,3],[4,5,6]],[[3,2,1],[6,5,4]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
print("hello")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)