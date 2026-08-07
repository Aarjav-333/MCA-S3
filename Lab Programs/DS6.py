import numpy as np

# Create a vector with values from 0 to 20
vector = np.arange(21)

# Change the sign of numbers from 9 to 15
vector[9:16] = -vector[9:16]

print("Modified vector:")
print(vector)