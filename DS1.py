from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


iris = load_iris()

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    # random_state=42
)


model = GaussianNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)

print("Accuracy" , accuracy)


# Confusion Matrix
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)


# Classification Report
report = classification_report(y_test, predictions)

print("\nClassification Report:")
print(report)

new_sample = [[5.1, 3.5, 1.4, 0.2]]



prediction = model.predict(new_sample)


# 0 → Setosa
# 1 → Versicolor
# 2 → Virginica
print("New sample prediction : ",prediction
      )


