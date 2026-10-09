# Formative Assessment - 02 (FA2) Executive Summary

## 📌 Student & Academic Details

| Attribute | Details |
|---|---|
| **Course** | **Advanced Data Science Lab [MCA33PE21]** |
| **Assessment** | **Formative Assessment - 02 (FA2)** |
| **Student Name** | **Shreyash Thakare** |
| **PRN** | **125M1H048** |
| **Class / Division** | **SYMCA (Semester-I)** |
| **Academic Year** | **2026 – 2027** |
| **Course Teacher** | **Prof. Prakash Ukhalkar** |
| **Submission Date** | **09-10-2026** |
| **🌐 Live Deployed App** | [https://shreyash-hh-liver-disease-app-app-pcnfzj.streamlit.app/](https://shreyash-hh-liver-disease-app-app-pcnfzj.streamlit.app/) |
| **📂 GitHub Repository** | [https://github.com/shreyash-hh/liver-disease-app](https://github.com/shreyash-hh/liver-disease-app) |

---

## 🎯 Project Overview
This project presents an end-to-end data science and machine learning clinical decision-support system trained on the **Indian Liver Patient Dataset (ILPD)** from the UCI Machine Learning Repository.

### Key Highlights:
1. **Interactive Web Application**: Deployed live on Streamlit Community Cloud with real-time risk assessment, patient parameter input sliders, and multiple ML algorithm selections.
2. **Zero-Leakage ML Pipeline**: Scikit-Learn pipelines integrating `SimpleImputer` (median), `FunctionTransformer(np.log1p)` for right-skewed enzymes, and `StandardScaler`.
3. **Imbalance Handling**: Utilized `class_weight='balanced'` to ensure high diagnostic sensitivity.

---

## 📊 Model Performance Comparison

Evaluated on a 20% stratified holdout test set alongside 5-Fold Stratified Cross-Validation on the training data:

| Model | Accuracy | Precision | Recall (Sensitivity) | F1-Score | ROC-AUC | 5-Fold CV F1 (±Std) |
|---|---|---|---|---|---|---|
| **Logistic Regression** | 64.91% | 79.71% | 67.47% | 0.7308 | 0.7360 | 0.725 ± 0.038 |
| **Decision Tree (depth=4)** | 68.42% | 85.51% | 67.47% | 0.7534 | 0.6904 | 0.758 ± 0.032 |
| **Random Forest (Baseline)** | 73.68% | 81.33% | 81.93% | 0.8163 | 0.7842 | 0.793 ± 0.041 |
| **KNN (k=5)** | 67.54% | 81.18% | 71.08% | 0.7571 | 0.7176 | 0.761 ± 0.035 |
| **Tuned Random Forest (GridSearchCV)** | **75.44%** | **83.13%** | **83.13%** | **0.8313** | **0.7924** | **0.804 ± 0.039** |

---

## 🏥 Clinical Interpretation & Rationale
- **Recall Priority**: In clinical diagnostic screening, **Recall** is prioritized to prevent False Negatives (missing a diseased patient).
- **Best Model**: **Tuned Random Forest** delivered the highest balanced performance (**83.13% Recall, 0.8313 F1-Score**).
- **Realistic Accuracy**: The 72%–76% accuracy range is authentic for the ILPD dataset without artificial leakage.

---

## 🔗 Project Links
- **Live Streamlit App**: [https://shreyash-hh-liver-disease-app-app-pcnfzj.streamlit.app/](https://shreyash-hh-liver-disease-app-app-pcnfzj.streamlit.app/)
- **GitHub Repository**: [https://github.com/shreyash-hh/liver-disease-app](https://github.com/shreyash-hh/liver-disease-app)
- **Summary PDF File**: [FA2_Summary_Report_125M1H048.pdf](file:///d:/DATA%20SCIENCE/FA-2/FA2_Summary_Report_125M1H048.pdf)
