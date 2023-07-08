import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5])#includes start index but excludes end index

print(arr[4:])#default end index is last index

print(arr[:4]) #upto index 4 and index 4 not included

print(arr[-3:-1])#negative slicing

print(arr[1:5:2])#use of step here 2 is step which prints 2,4

print(arr[::2])#slice everyitems with step 2

# slicing 2-D array

ara = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(ara[1,1:4])#second row ko index 1 dekhi 4 index samma ko element(1,2,3)rd column of second row

print(ara[0:2,2])#slicing the element of 3rd coloumn ie of index 2

print(ara[0:2,1:4])