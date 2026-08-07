import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([15, 20, 25, 50])

print("Array 1:", array1)
print("Array 2:", array2)

print("\nGreater than:")
print(np.greater(array1, array2))

print("\nGreater than or equal to:")
print(np.greater_equal(array1, array2))

print("\nLess than:")
print(np.less(array1, array2))

print("\nLess than or equal to:")
print(np.less_equal(array1, array2))