import numpy as np

new_matrix = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(new_matrix)

arr = np.array([1, 2, 3, 4, 5])

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr.dtype)

arr = np.array([10, 20, 30, 40, 50])
print(arr[0:4])

arr = np.array([1, 2, 3, 4], ndmin=3) #numpy array with 2dimensions