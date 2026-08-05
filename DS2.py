from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

data = load_breast_cancer()


print(data.feature_names)
print("="*40)
X = data.data
y = data.target

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = GaussianNB()


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)


cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)


print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=data.target_names
))



new_patient = np.array([
    14.2,   # mean radius
    20.5,   # mean texture
    92.1,   # mean perimeter
    654.0,  # mean area
    0.105,  # mean smoothness
    0.185,  # mean compactness
    0.155,  # mean concavity
    0.085,  # mean concave points
    0.205,  # mean symmetry
    0.065,  # mean fractal dimension
    0.40,   # radius error
    1.20,   # texture error
    2.80,   # perimeter error
    35.0,   # area error
    0.006,  # smoothness error
    0.030,  # compactness error
    0.040,  # concavity error
    0.015,  # concave points error
    0.020,  # symmetry error
    0.004,  # fractal dimension error
    16.5,   # worst radius
    28.0,   # worst texture
    108.0,  # worst perimeter
    820.0,  # worst area
    0.140,  # worst smoothness
    0.350,  # worst compactness
    0.400,  # worst concavity
    0.150,  # worst concave points
    0.300,  # worst symmetry
    0.080   # worst fractal dimension
])


print(new_patient.shape)

new_patient = new_patient.reshape(1, -1)
# print(new_patient)

print(new_patient.shape)

prediction = model.predict(new_patient)

print("Prediction:", prediction)
print("Class:", data.target_names[prediction[0]])