#New sample with 4 inputs -----> predict class

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Create array
new_flower = np.array([
    [sepal_length, sepal_width, petal_length, petal_width]
])

# Predict
prediction = knn.predict(new_flower)

# Print class
print("Predicted Class:", iris.target_names[prediction[0]])