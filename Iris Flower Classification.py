# Simple Classification - Easy to Understand

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
print("Loading iris dataset...")
iris = load_iris()
X = iris.data      # Features (flower measurements)
y = iris.target    # Labels (flower types)

print(f"Total flowers: {len(X)}")
print(f"Features per flower: {len(X[0])}")
print(f"Flower types: {iris.target_names}")
print()

# 2. Split data
print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(f"Training set: {len(X_train)} flowers")
print(f"Testing set: {len(X_test)} flowers")
print()

# 3. Create and train model
print("Training model...")
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("Training complete!")
print()

# 4. Test model
print("Testing model...")
predictions = model.predict(X_test)

# 5. Check accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")
print()

# 6. Show some predictions
print("Sample predictions:")
for i in range(5):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[predictions[i]]
    print(f"Flower {i+1}: Actual={actual}, Predicted={predicted}")