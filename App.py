import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Indian Liver Disease Patient Predictor",
    page_icon="🩺",
    layout="wide"
)

# App Title and Description
st.title("🩺 Indian Liver Disease Patient Predictor")
st.markdown("""
This clinical decision-support application uses machine learning models trained on the **Indian Liver Patient Dataset (ILPD)**.
Select an algorithm from the sidebar, enter the patient's biochemical blood test values, and click **Predict** to assess liver disease risk.
""")

# Load models with st.cache_resource
@st.cache_resource
def load_models():
    model_files = {
        "Logistic Regression": "lr_model.joblib",
        "Decision Tree": "dt_model.joblib",
        "Random Forest (Baseline)": "rf_model.joblib",
        "K-Nearest Neighbors (KNN)": "knn_model.joblib",
        "Tuned Random Forest (GridSearchCV)": "tuned_rf_model.joblib"
    }
    loaded = {}
    for name, filename in model_files.items():
        if os.path.exists(filename):
            loaded[name] = joblib.load(filename)
        elif os.path.exists(os.path.join("liver-disease-app", filename)):
            loaded[name] = joblib.load(os.path.join("liver-disease-app", filename))
        else:
            st.error(f"Model file `{filename}` not found. Please train and save models first.")
    return loaded

models = load_models()

# Sidebar: Model Selection & Info
st.sidebar.header("⚙️ Model Configuration")
selected_model_name = st.sidebar.selectbox(
    "Choose Machine Learning Model:",
    list(models.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Model Training Info:**
- **Training Source**: UCI ILPD Dataset (570 records)
- **Validation**: 5-Fold Stratified Cross Validation
- **Metric Focus**: Recall & F1-score (minimizing false negatives)
""")

# Patient Input Form
st.subheader("📋 Enter Patient Biochemical Test Values")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=100, value=45, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", min_value=0.1, max_value=80.0, value=1.0, step=0.1, format="%.2f")
    direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", min_value=0.0, max_value=30.0, value=0.3, step=0.1, format="%.2f")

with col2:
    alkphos = st.number_input("Alkaline Phosphatase - ALP (IU/L)", min_value=10, max_value=2500, value=200, step=5)
    sgpt = st.number_input("Alamine Aminotransferase - ALT/SGPT (IU/L)", min_value=5, max_value=2000, value=35, step=5)
    sgot = st.number_input("Aspartate Aminotransferase - AST/SGOT (IU/L)", min_value=5, max_value=5000, value=40, step=5)

with col3:
    total_proteins = st.number_input("Total Proteins (g/dL)", min_value=1.0, max_value=12.0, value=6.5, step=0.1, format="%.2f")
    albumin = st.number_input("Albumin (g/dL)", min_value=0.5, max_value=6.0, value=3.2, step=0.1, format="%.2f")
    ag_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.1, max_value=3.0, value=0.95, step=0.05, format="%.2f")

# Prediction logic
st.markdown("---")
predict_btn = st.button("🔍 Run Liver Disease Prediction", type="primary", use_container_width=True)

if predict_btn:
    if selected_model_name not in models:
        st.error("Selected model is not currently loaded.")
    else:
        # Preprocess input matching exact training order
        gender_encoded = 1 if gender == "Male" else 0
        
        input_data = pd.DataFrame([{
            'Age': age,
            'Gender': gender_encoded,
            'Total_Bilirubin': total_bilirubin,
            'Direct_Bilirubin': direct_bilirubin,
            'Alkaline_Phosphotase': alkphos,
            'Alamine_Aminotransferase': sgpt,
            'Aspartate_Aminotransferase': sgot,
            'Total_Protiens': total_proteins,
            'Albumin': albumin,
            'Albumin_and_Globulin_Ratio': ag_ratio
        }])

        model = models[selected_model_name]

        try:
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0] if hasattr(model, "predict_proba") else None

            st.subheader("🎯 Diagnostic Result")
            res_col1, res_col2 = st.columns([2, 1])

            with res_col1:
                if prediction == 1:
                    st.error("⚠️ **High Risk: Indicator of Liver Disease Detected**")
                    st.write("The model predicts biochemical indicators consistent with liver impairment. Clinical follow-up is recommended.")
                else:
                    st.success("✅ **Low Risk: No Significant Liver Disease Detected**")
                    st.write("The model predicts blood test parameters within standard non-disease patterns.")

            with res_col2:
                if probabilities is not None:
                    disease_prob = probabilities[1] * 100
                    st.metric(label="Disease Probability", value=f"{disease_prob:.1f}%")
                    st.progress(probabilities[1])

            # Expandable feature summary
            with st.expander("🔍 View Processed Input Data"):
                st.dataframe(input_data)

        except Exception as e:
            st.error(f"Error occurred during inference: {str(e)}")

# Medical disclaimer footer
st.markdown("---")
st.caption("""
⚠️ **Educational & Academic Disclaimer**: 
This web application is developed solely as part of an academic case study for Advanced Data Science (MCA33PE17). 
It is NOT a certified medical diagnostic device and must not be used for actual clinical decision-making.
""")
