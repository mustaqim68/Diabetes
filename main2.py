import pickle
import streamlit as st

# Memperbaiki cara memuat model dari file
with open('diabetesmodel2.sav', 'rb') as file:
    diabetesmodel2 = pickle.load(file)

st.write('Data Mining Prediksi Diabetes')

Pregnancies = st.text_input('Input Nilai Pregnancies')
Glucose = st.text_input('Input Nilai Glucose')
Skinthicknes = st.text_input('Input Nilai Skinthicknes')
Insulin = st.text_input('Input Nilai Insulin')
BMI = st.text_input('Input Nilai BMI')
DiabetesPredigreeFunction = st.text_input('Input Nilai Diabetes Predigree Function')
Age = st.text_input('Input Nilai Age')

# code prediksi
if st.button ('Tes Prediksi Diabetes'):
    diab_prediction = diabetesmodel2.predict([[Pregnancies, Glucose, Skinthicknes, Insulin, BMI,DiabetesPredigreeFunction, Age]] )
    if(diab_prediction[0] == 1) : 
        diab_diagnosis = 'Pasien terkena diabetes'
    else :
        diab_diagnosis = 'Pasian tidak terkena Diabetes'
    st.success(diab_diagnosis)


