#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
import streamlit as st


# In[2]:


pickle_in = open("C:\\Users\\balar\\OneDrive\\Desktop\\P285\\rf_model.pkl",'rb')
classifier = pickle.load(pickle_in)


# In[3]:


def predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity):
    prediction = classifier.predict([[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction


# In[4]:


def main():
    st.title('Energy Prediction')
    
    temperature = st.text_input('Temperature')
    exhaust_vacuum = st.text_input('Exhaust Vacuum')
    amb_pressure = st.text_input('Ambient Pressure')
    r_humidity = st.text_input('Relative Humidity')
    result=''
    if st.button('Predict'):
        result = predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity)
    st.success('Energy Produced is {}'.format(result))


# In[ ]:




