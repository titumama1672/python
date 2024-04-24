#Write a python program to understand various methods of array class.

# Import the NumPy module
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Shape of array:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Total number of elements:", arr.size)
print("Data type of array elements:", arr.dtype)
print("Size of each array element in bytes:", arr.itemsize)
new_shape = (5, 2)
new_arr = arr.reshape(new_shape)
print("New array with shape", new_shape, ":\n", new_arr)
print("Maximum element in array:", arr.max())
print("Minimum element in array:", arr.min())
arr.sort()
print("Sorted array in ascending order:\n", arr)



#Write a python program to store 5 subject marks in an array and calculate total marks and percentage of marks.

import numpy as np
marks = np.array([75, 85, 90, 80, 95])
total_marks = np.sum(marks)
percentage = (total_marks / (marks.shape[0] * 100)) * 100
print("Subject marks:", marks)
print("Total marks:", total_marks)
print("Percentage of marks:", percentage, "%")



#iii. Write a python program to create an array using NumPy.

import numpy as np
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)
print(arr1d.shape)
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr2d)
print(arr2d.shape)


#iv. Write a python program to calculate matrix addition.

def matrix_addition(A, B):

    rows = len(A)
    cols = len(A[0])
    C = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    return C
A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
B = [[9, 8, 7],
[6, 5, 4],
[3, 2, 1]]
C = matrix_addition(A, B)
print(C)
