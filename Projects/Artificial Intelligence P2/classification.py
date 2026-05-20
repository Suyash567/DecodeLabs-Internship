import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import Scikit-Learn utilities
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# =====================================================================
# 1. INPUT PHASE: Load and Explore the Iris Benchmark
# =====================================================================
# Load the dataset (150 balanced samples, 3 classes, 4 dimensions)
iris = load_iris()
X = iris.data  # Features: Sepal Length/Width, Petal Length/Width
y = iris.target  # Targets: 0 (Setosa), 1 (Versicolor), 2 (Virginica)

print("="*50)
print("PHASE 1: DATASET SUMMARY")
print("="*50)
print(f"Total Samples: {X.shape[0]}")
print(f"Features Per Sample: {X.shape[1]} -> {iris.feature_names}")
print(f"Target Classes: {len(np.unique(y))} -> {iris.target_names}\n")


# =====================================================================
# 2. PROCESS PHASE: Split, Scale, and Model Workflow
# =====================================================================
print("="*50)
print("PHASE 2: PIPELINE PROCESSING")
print("="*50)

# Step A: Shuffle and split into 80% Training and 20% Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, shuffle=True
)
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Step B: Feature Scaling via StandardScaler (Mean=0, Variance=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Feature scaling successfully applied.\n")

# Step C & D: Instantiate and Fit the Model (K=5)
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
print("Model trained using K=5 neighbors.\n")

# Step E: Predict on unseen testing data
y_pred = knn_model.predict(X_test_scaled)


# =====================================================================
# 3. OUTPUT PHASE: Diagnostic Validation
# =====================================================================
print("="*50)
print("PHASE 3: METRIC VALIDATION & EVALUATION")
print("="*50)

# Generate detailed performance breakdown (Precision, Recall, F1-Score)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Compute the raw Confusion Matrix metrics (TP, FP, FN, TN check)
conf_matrix = confusion_matrix(y_test, y_pred)


# =====================================================================
# 4. CUSTOM INFERENCE: Live Test Vector
# =====================================================================
print("="*50)
print("PHASE 4: LIVE INFERENCE TEST")
print("="*50)

# Provide a raw sample matrix: [Sepal Length, Sepal Width, Petal Length, Petal Width]
custom_flower = np.array([[5.1, 3.5, 1.4, 0.2]]) 

# Pass sample through the gatekeeper scaler using training parameters
custom_scaled = scaler.transform(custom_flower)
prediction = knn_model.predict(custom_scaled)

print(f"Raw Input Dimensions: {custom_flower[0]}")
print(f"Predicted Output Class: {iris.target_names[prediction[0]]}\n")


# =====================================================================
# 5. HYPERPARAMETER TUNING: Plotting the Engine Elbow
# =====================================================================
print("="*50)
print("PHASE 5: OPTIMIZING HYPERPARAMETERS (THE ELBOW METHOD)")
print("="*50)
print("Calculating error rates for K values 1 through 15...")

error_rates = []

for k in range(1, 16):
    knn_tuning = KNeighborsClassifier(n_neighbors=k)
    knn_tuning.fit(X_train_scaled, y_train)
    preds = knn_tuning.predict(X_test_scaled)
    # Average instances where prediction logic failed
    error_rates.append(np.mean(preds != y_test))

print("Plotting diagnostics...")

# Create subplots to show Confusion Matrix and Elbow Curve simultaneously
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot A: Seaborn Confusion Matrix Heatmap
sns.heatmap(
    conf_matrix, 
    annot=True, 
    fmt='d', 
    cmap='Blues', 
    xticklabels=iris.target_names, 
    yticklabels=iris.target_names,
    ax=axes[0]
)
axes[0].set_title('Confusion Matrix Diagnostics')
axes[0].set_xlabel('Predicted Classes')
axes[0].set_ylabel('True Reality Classes')

# Plot B: Error Rate vs K Value line graph to spot "The Elbow"
axes[1].plot(range(1, 16), error_rates, color='crimson', linestyle='--', marker='o', markersize=8)
axes[1].set_title('Tuning Curve: Finding the Optimal K')
axes[1].set_xlabel('Hyperparameter K Value')
axes[1].set_ylabel('Validation Error Rate')
axes[1].set_xticks(range(1, 16))
axes[1].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
print("Pipeline complete!")