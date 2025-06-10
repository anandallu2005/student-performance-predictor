import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load dataset
df = pd.read_csv("student_data.csv")
df['passed'] = df['passed'].map({'Yes': 1, 'No': 0})

X = df.drop('passed', axis=1)
y = df['passed']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Streamlit app
st.title("🎓 Student Performance Predictor")

st.write("Enter the details below to predict whether the student will pass or fail:")

study_hours = st.slider("Study Hours per Day", 0, 10, 3)
previous_score = st.slider("Previous Exam Score", 0, 100, 60)
attendance = st.slider("Attendance (%)", 0, 100, 75)
sleep_hours = st.slider("Sleep Hours per Day", 0, 12, 6)
extracurricular = st.selectbox("Participates in Extracurricular Activities?", ("Yes", "No"))
extra_val = 1 if extracurricular == "Yes" else 0

input_data = np.array([[study_hours, previous_score, attendance, sleep_hours, extra_val]])
prediction = model.predict(input_data)

if st.button("Predict"):
    if prediction[0] == 1:
        st.success("✅ The student is likely to PASS.")
    else:
        st.error("❌ The student is likely to FAIL.")
