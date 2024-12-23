# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import pickle 

loaded_model = pickle.load(open('C:/Users/Yacine/OneDrive/Bureau/Personal Projects/trained_model.sav', 'rb'))

input_data = (4,110,92,0,0,37.6, 0.191, 30)

#changing the input as a numpy array
input_as_numpy = np.asarray(input_data)

#reshape the array 
input_reshape = input_as_numpy.reshape(1,-1)


prediction = loaded_model.predict(input_reshape)
print(prediction)

if(prediction[0]==0):
  print('You are not diabetic')
else:
    print('You are  diabetic')

