# Student Performance Predictor 🎓

This is a simple AI/ML project to predict whether a student will pass or fail based on their study hours, previous scores, attendance, sleep habits, and extracurricular involvement.

## Features Used
- `study_hours`: Daily study hours
- `previous_score`: Previous exam score
- `attendance`: Attendance percentage
- `sleep_hours`: Daily sleep duration
- `extracurricular`: Participation in extracurricular activities (1 = Yes, 0 = No)

## Model Used
- Random Forest Classifier

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas scikit-learn
   ```

2. Run the script:
   ```bash
   python student_predictor.py
   ```

## Output
- The model prints the accuracy of prediction on test data.
