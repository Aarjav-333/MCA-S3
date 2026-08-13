# Write a Python program to predict diabetes using KNN

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_diabetes

# Load diabetes dataset
diabetics = load_diabetes()

print(diabetics.data.shape)
print(diabetics.target.shape)
print(diabetics.feature_names)