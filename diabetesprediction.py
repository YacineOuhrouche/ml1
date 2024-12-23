# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:50:32 2024

@author: Yacine
"""

import numpy as np

import pickle
import streamlit as st



loaded_model = pickle.load(open('C:/Users/Yacine/OneDrive/Bureau/Personal Projects/trained_model.sav', 'rb'))

#creating a function for prediction 

def diabetes_prediction(input_data):
   

    #changing the input as a numpy array
    input_as_numpy = np.asarray(input_data)

    #reshape the array 
    input_reshape = input_as_numpy.reshape(1,-1)


    prediction = loaded_model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
      return 'You are not diabetic'
    else:
        return 'You are  diabetic'
    
    
  
def main():
    
      
      #title
    st.title('Do You Have Diabetes?')
      
      #getting the input data from the user 
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age  = st.text_input('Age ')
      
      
      
  
      
      #code for prediction 
    diagnosis = ''
      
      
    if st.button('Result'):
          diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
      
        
    st.success(diagnosis)
      
      
if __name__ == '__main__':
          main()