# To create a 4 × 4 random integer array, use NumPy's np.random.randint() function.

import numpy as np

array = np.random.randint(0,100,(4, 4))

print("Original Array:")
print(array)

new_array = array.copy()
new_array[[0, 3]] = new_array[[3, 0]]

print("\nArray after swapping first and last rows:")
print(new_array)