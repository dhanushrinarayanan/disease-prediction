import pickle
import streamlit as st

# tittle
st.markdown("<h1 style='text-align: center; color: red;'>MULTIPLE DISEASE PREDICTION BY USING ML </h1>", unsafe_allow_html=True)

#load the picke file

diabetes_model = pickle.load(open("diabetes_model.sav","rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav","rb"))



#disease choice
with st.sidebar:
	
	selected = option_menu("Multiple Diseas Prediction System",["Diabetes Prediction","Heart Disease Prediction",],
	icons = ["activity","heart",],default_index=1)

# diabetes prediction
try:
    if (selected == "Diabetes Prediction"):
        st.title("Diabetes Prediction using ML")
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        with col2:
            Glucose = st.text_input('Glucose Level')
        with col1:
            BloodPressure = st.text_input('Blood Pressure value')
        with col2:
            SkinThickness = st.text_input('Skin Thickness value')
        with col1:
            Insulin = st.text_input('Insulin Level')
        with col2:
            BMI = st.text_input('BMI value')
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        with col2:
            Age = st.text_input('Age of the Person')
        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if (diabetes_prediction[0] == 1):
                diabetes_diagnosis = 'The person is diabetic'
            else:
                diabetes_diagnosis = 'The person is not diabetic'
        st.success(diabetes_diagnosis)
        
except:
    st.error(f"PLEASE ENTER THE CORRECT VALUE")

# heart disease prediction
if (selected == 'Heart Disease Prediction'):
	st.title('Heart Diseas Prediction using ML')
	col1, col2, col3 = st.columns(3)
	with col1:
		age = st.text_input('Age')
	with col2:
		sex = st.text_input('Sex')
	with col3:
		cp = st.text_input('Chest Pain types')
	with col1:
		trestbps = st.text_input('Resting Blood Pressure')
	with col2:
		chol = st.text_input('Serum Cholestoral in mg/dl')
	with col3:
		fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
	with col1:
		restecg = st.text_input('Resting Electrocardiographic results')
	with col2:
		thalach = st.text_input('Maximum Heart Rate achieved')
	with col3:
		exang = st.text_input('Exercise Induced Angina')
	with col1:
		oldpeak = st.text_input('ST depression induced by exercise')
	with col2:
		slope = st.text_input('Slope of the peak exercise ST segment')
	with col3:
		ca = st.text_input('Major vessels colored by flourosopy')
	with col1:
		thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
	heart_diagnosis = ''
	if st.button('Heart Disease Test Result'):
		heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
		if (heart_prediction[0] == 1):
			heart_diagnosis = 'The person is having heart disease'
		else:
			heart_diagnosis = 'The person does not have any heart disease'
	st.success(heart_diagnosis)
        
