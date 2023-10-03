# -*- coding: utf-8 -*-
"""
Created on Tue Oct 3 00:12:27 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('CatboostClassifier.pkl', 'rb'))


st.title('Prostate Cancer Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;">By Jatau Abel</h3>
    <div style="background-color:brown;padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            Prostate cancer is a cancer that develops in the Prostate Gland, which controls the flow of urine or semen from the reproductive organ of the male reproductive system. <br> 
                <br>
                This system can predict between the two types of Prostate cancer (Benign = B, Malignant = M), all you need do is to supply the required information. <br>
                All you need to do is fill the form below:
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

# Input field for column1
radius = st.text_input("Enter Radius (an integer)")
texture = st.text_input("Enter Texture (an integer)")
perimeter = st.text_input("Enter Perimeter (an integer)")
area = st.text_input("Enter Area (an integer)")
smoothness = st.text_input("Enter Smoothness (a float)")
compactness = st.text_input("Enter Compactness (a float)")
symmetry = st.text_input("Enter Symmetry (a float)")
fd = st.text_input("Enter Fractal Dimension (a float)")


cancer_pred = ''

results = ''


if st.button('Submit'):
    cancer_pred = model.predict([[radius, texture, perimeter, area, smoothness, compactness, symmetry, fd]])
    if cancer_pred[0] == 1:
        results = 'Malignant'
    else:
        results = 'Benign'
        
    st.write(f"The type of cancer is: {results}")
    




