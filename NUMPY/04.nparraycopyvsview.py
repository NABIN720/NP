# import numpy as np

# arr = np.array([1,2,3,4,5])

# # x = arr.copy()
# x= arr.view()#The view SHOULD be affected by the changes made to the original array.

# arr[0] = 42

# print(arr)
# print(x)

# make a view , change the view and display both arrays
import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.view()#The original array SHOULD be affected by the changes made to the view.
x[0] = 31

print(arr)
print(x)

# check if array owns its data
arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()
# The copy returns None.
# The view returns the original array.
print(x.base)
print(y.base)