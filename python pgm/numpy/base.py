# Python Program to create
# a data type object
import numpy as np

# First Array
arr1 = np.array([[4, 7], [2, 6]],
				dtype = np.float64)

# Second Array
arr2 = np.array([[3, 6], [2, 8]],
				dtype = np.float64)

# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)

# Addition of all Array elements
# using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)

# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)
