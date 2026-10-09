# 🩺 Indian Liver Disease Patient Predictor & Clinical Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An end-to-end clinical machine learning decision-support system and interactive web application for early screening of liver disease, trained on the **Indian Liver Patient Dataset (ILPD)** from the UCI Machine Learning Repository.

---

## 📌 Project Overview

Liver disease accounts for substantial global mortality, with early detection critically improving patient survival rates. This project provides:
1. **End-to-End Data Science Workflow**: Exploratory Data Analysis (EDA), log-transformations for skewed biochemical enzymes, data deduplication, and zero-leakage scikit-learn preprocessing pipelines.
2. **Model Training & Evaluation**: Evaluates 5 machine learning models (**Logistic Regression**, **Decision Tree**, **Random Forest**, **K-Nearest Neighbors**, and **Tuned Random Forest with GridSearchCV**) using 5-Fold Stratified Cross-Validation.
3. **Interactive Streamlit Web Application**: An intuitive clinical interface enabling medical practitioners to enter patient blood markers, choose ML models, and receive instant diagnostic risk assessments with confidence levels.

---

## 🔬 Dataset & Clinical Biomarkers

The dataset contains records of **583 patient samples** (416 liver disease patients and 167 non-disease controls) with 10 diagnostic blood and demographic features:

| Feature Name | Clinical Description | Typical Normal Range |
|---|---|---|
| `Age` | Patient Age in years | - |
| `Gender` | Biological sex (`Male: 1`, `Female: 0`) | - |
| `Total_Bilirubin` | Total bilirubin in blood (mg/dL) | 0.1 – 1.2 mg/dL |
| `Direct_Bilirubin` | Conjugated bilirubin (mg/dL) | 0.0 – 0.3 mg/dL |
| `Alkaline_Phosphotase` | ALP enzyme level (IU/L) | 44 – 147 IU/L |
| `Alamine_Aminotransferase` | ALT / SGPT liver enzyme (IU/L) | 7 – 56 IU/L |
| `Aspartate_Aminotransferase` | AST / SGOT liver enzyme (IU/L) | 10 – 40 IU/L |
| `Total_Protiens` | Total serum protein (g/dL) | 6.0 – 8.3 g/dL |
| `Albumin` | Serum albumin level (g/dL) | 3.5 – 5.0 g/dL |
| `Albumin_and_Globulin_Ratio` | A/G ratio | 1.0 – 2.5 |
| **`Dataset` (Target)** | Diagnostic status (`1: Liver Disease`, `0: Healthy`) | - |

---

## 📊 Model Performance Summary

Models were tuned and evaluated using **5-Fold Stratified Cross-Validation** and a holdout test set (20%) with balanced class weighting:

| Model | Test Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| **Logistic Regression** | 64.9% | 79.7% | 67.5% | 0.731 | 0.736 |
| **Decision Tree** | 68.4% | 85.5% | 67.5% | 0.753 | 0.690 |
| **Random Forest (Baseline)** | 73.7% | 81.3% | 81.9% | **0.816** | **0.784** |
| **KNN (k=5)** | 67.5% | 81.2% | 71.1% | 0.757 | 0.718 |
| **Tuned Random Forest (GridSearchCV)** | **75.4%** | **83.1%** | **83.1%** | **0.831** | **0.792** |

> **Clinical Rationale**: In medical diagnostics, **Recall** is prioritized over Precision to minimize False Negatives (preventing undiagnosed liver disease). Tuned Random Forest achieved the highest balanced sensitivity and F1-score.

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/shreyash-hh/liver-disease-app.git
cd liver-disease-app
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows PowerShell
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit Application
```bash
streamlit run App.py
```
Open your browser at `http://localhost:8501`.

---

## 📁 Repository Structure

```text
├── App.py                            # Streamlit web application
├── FA_2_liver_disease_anaysis.ipynb  # Granular Jupyter notebook with full EDA & ML pipeline
├── indian_liver_patient.csv          # UCI Indian Liver Patient Dataset
├── requirements.txt                  # Python dependencies
├── lr_model.joblib                   # Serialized Logistic Regression pipeline
├── dt_model.joblib                   # Serialized Decision Tree pipeline
├── rf_model.joblib                   # Serialized Random Forest pipeline
├── knn_model.joblib                  # Serialized KNN pipeline
├── tuned_rf_model.joblib             # Serialized Tuned Random Forest pipeline
├── .gitignore                        # Git exclusion rules
└── README.md                         # Project documentation
```

---

## 👨‍💻 Author

**Shreyash Thakare**  
PRN: `125M1H048`  
Advanced Data Science Lab [MCA33PE21]  
Course Teacher: **Prof. Prakash Ukhalkar**
