import streamlit as st
import pandas as pd
import pickle
import os

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the pre-trained model and DataFrame
delaq_path = os.path.join(script_dir, 'delaq.pkl')
PM_predictor_path = os.path.join(script_dir, 'PM_predictor.pkl')

delaq = pd.read_pickle(delaq_path)
PM_predictor = pickle.load(open(PM_predictor_path, 'rb'))

# Streamlit app
st.title('Particulate Matter Concentration Prediction App')

# Input features
AT = st.slider('Temperature (degC)', float(delaq['AT'].min()), float(delaq['AT'].max()))
WS = st.slider('Wind Speed (km/hr)', float(delaq['WS'].min()), float(delaq['WS'].max()))
RH = st.slider('Relative Humidity (%)', float(delaq['RH'].min()), float(delaq['RH'].max()))
RF = st.slider('Daily Rainfall (mm)', float(delaq['RF'].min()), float(delaq['RF'].max()))
WD = st.slider('Wind Direction (degree)', float(delaq['WD'].min()), float(delaq['WD'].max()))

# Prediction button
if st.button('Predict Particulate Matter Concentration'):
    # Prepare input data for prediction
    input_data = [[AT, WS, RH, RF, WD]]
    input_df = pd.DataFrame(input_data, columns=['AT', 'WS', 'RH', 'RF', 'WD'])

    # Make prediction
    prediction = PM_predictor.predict(input_df)

    # Display the result
    st.success(f'Predicted Particulate Matter Concentration: {prediction[0]:.2f} µg/m³')
