# Iris Classification Pipeline (K-Nearest Neighbors)

An end-to-end Machine Learning workflow that utilizes the classic Iris benchmark dataset to train, scale, evaluate, and optimize a $K$-Nearest Neighbors ($KNN$) classifier. The script features full pipeline transparency from data loading to real-time custom inference and hyperparameter diagnostic plotting.

## Pipeline Architecture & Core Features

*   **Standardized Preprocessing Layer:** Implements a strict `StandardScaler` operational gatekeeper (centering data to $\mu = 0, \sigma^2 = 1$) fitted exclusively on training data to prevent data leakage during testing.
*   **Stratified Data Partitioning:** Shuffles and splits the 150-sample dataset into an **80% Training set** (120 samples) for model fitting and a **20% Testing set** (30 samples) for unbiased validation.
*   **Live Inference Engine:** Features an isolated inference pipeline that processes raw, out-of-sample physical measurements through the saved scaling parameters for instant target class prediction.
*   **Dual-Diagnostic Visualization:** Generates side-by-side performance plots utilizing Matplotlib and Seaborn:
    *   **Confusion Matrix Heatmap:** Maps true vs. predicted classes to visually isolate exact misclassifications.
    *   **Elbow Optimization Curve:** Iterates through hyperparameters ($K = 1$ to $15$) to trace validation error rates and discover the mathematically optimal neighbor count.

## Technical Stack & Dependencies

*   **Core Mechanics:** Python 3.x
*   **Data Processing:** `numpy`, `pandas`
*   **Machine Learning Engine:** `scikit-learn` (Datasets, Metrics, Preprocessing, Neighbors)
*   **Visualization Layer:** `matplotlib`, `seaborn`

## Operational Workflow

The script automatically executes through 5 distinct computational phases:

*   **Phase 1 (Ingestion):** Loads the 4-dimensional feature space (Sepal/Petal lengths and widths) and displays baseline dataset balanced-class summaries.
*   **Phase 2 (Processing):** Executes the shuffle-split, normalizes the feature matrices, and fits the $KNN$ classifier using an initial $K=5$ configuration.
*   **Phase 3 (Validation):** Outputs explicit diagnostic metrics including raw Precision, Recall, and F1-Scores across all three target flower profiles (*Setosa*, *Versicolor*, *Virginica*).
*   **Phase 4 (Inference):** Feeds a live test vector through the transformation pipeline to demonstrate production-ready categorization.
*   **Phase 5 (Optimization):** Loops through hyperparameter variants, computes validation failure averages, and renders the dual diagnostic dashboard.

## Execution

Ensure all dependencies are installed, then run the pipeline directly via terminal:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
python pipeline.py
