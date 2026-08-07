# You can use NumPy's savetxt() function to save an array to a text file and loadtxt() to load it back.

import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

np.savetxt("array.txt", array, fmt="%d")

print("Array saved successfully.")

loaded_array = np.loadtxt("array.txt", dtype=int)

print("\nLoaded Array:")
print(loaded_array)