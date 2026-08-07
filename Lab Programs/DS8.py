import numpy as np

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])


matrix = np.array([1, 2, 3, 4, 5, 6, 7 ,8, 9])
matrix = matrix.reshape(3,3)

print("Matrix:")
print(matrix)

print("\nSum of all elements:", np.sum(matrix))

print("\nSum of each column:")
print(np.sum(matrix, axis=0))

print("\nSum of each row:")
print(np.sum(matrix, axis=1))