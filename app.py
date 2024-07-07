import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():

    st.set_page_config(
        layout="wide", page_title="Stroke Possibility Checker using Machine Learning App", page_icon="🧠")

    st.title("Stroke Possibility Checker using Machine Learning")
    st.write("Created by Divyansh Bhandari and Arnav Agarwal")
    st.write("This is a simple web app to check the possibility of stroke based on the patient's details. Please enter the patient's details below and click on the button below to check the possibility of stroke.")
    st.subheader("Add Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=0.0, format="%.2f")
        hypertension = st.selectbox("Hypertension", ["No", "Yes"])
        heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
        ever_married = st.selectbox("Ever Married", ["No", "Yes"])

    with col2:
        avg_glucose_level = st.number_input(
            "Average Glucose Level", min_value=0.0, format="%.2f")
        bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
        work_type = st.selectbox(
            "Work Type", ["Govt Job", "Never Worked", "Private", "Self-employed", "Children"])
        smoking_status = st.selectbox(
            "Smoking Status", ["Unknown", "Formerly Smoked", "Never Smoked", "Smokes"])
        residence_type = st.selectbox("Residence Type", ["Rural", "Urban"])

    gender = 1 if gender == "Male" else 0
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0
    ever_married = 1 if ever_married == "Yes" else 0
    residence_type = 1 if residence_type == "Urban" else 0

    work_type_mapping = {
        "Govt Job": 0,
        "Never Worked": 1,
        "Private": 2,
        "Self-employed": 3,
        "Children": 4
    }

    s_s_mapping = {
        "Unknown": 0,
        "Formerly Smoked": 1,
        "Never Smoked": 2,
        "Smokes": 3
    }

    work_type_encoded = np.array([False, False, False, False, False])
    work_type_encoded[work_type_mapping[work_type]] = True

    s_s_encoded = np.array([False, False, False, False])
    s_s_encoded[s_s_mapping[smoking_status]] = True
    patient_details = np.array([gender, age, hypertension, heart_disease,
                                ever_married, residence_type, avg_glucose_level, bmi])
    patient_details = np.concatenate(
        (patient_details, work_type_encoded, s_s_encoded))

    if st.button("Check possibility of Stroke"):
        input_data = {
            "gender": [gender],
            "age": [age],
            "hypertension": [hypertension],
            "heart_disease": [heart_disease],
            "ever_married": [ever_married],
            "Residence_type": [residence_type],
            "avg_glucose_level": [avg_glucose_level],
            "bmi": [bmi],
            "work_type_Govt_job": [work_type_encoded[0]],
            "work_type_Never_worked": [work_type_encoded[1]],
            "work_type_Private": [work_type_encoded[2]],
            "work_type_Self-employed": [work_type_encoded[3]],
            "work_type_children": [work_type_encoded[4]],
            "s_s_Unknown": [s_s_encoded[0]],
            "s_s_formerly smoked": [s_s_encoded[1]],
            "s_s_never smoked": [s_s_encoded[2]],
            "s_s_smokes": [s_s_encoded[3]]
        }
        input_df = pd.DataFrame(input_data)

        scaler_path = "scaler.pickle"
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        input_scaled = scaler.transform(input_df)

        model_path = "model.pickle"
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

        predictions = model.predict(input_scaled)

        prediction = predictions[0]

        st.subheader("Possibility of Stroke:")

        if prediction == 1:
            st.error("Somewhat Possible 😟, please consider consulting a doctor")
        else:
            st.success(
                "Stroke Unlikely 😊, but its good to consult a doctor if you have any symptoms")

        st.write("Note: This is a prediction based on the data you provided. Please consult a doctor for accurate diagnosis. We do not take any responsibility for the accuracy of the prediction.")

        st.write("The predictions made by this web app are based solely on the data provided by the user and should not be considered medical advice. This tool is for informational purposes only and is not intended to replace professional medical consultation, diagnosis, or treatment. Always seek the advice of your physician or other qualified health providers with any questions you may have regarding a medical condition. We (the authors/creators of this application) do not take any responsibility for the accuracy or reliability of the predictions made by this application.")


if __name__ == "__main__":
    run()
