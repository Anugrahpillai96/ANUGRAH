import streamlit as st
import pandas as pd
import joblib
# Load the modified DataFrame
delaq = pd.read_csv('delaq.csv')
# Load the pre-trained model
PM_predictor = joblib.load('PM_predictor.joblib')

# Streamlit app
st.title('Particulate Matter Concentration Prediction App')

# Input features from the existing DataFrame
temperature = st.slider('Temperature (degC)', float(delaq['AT'].min()), float(delaq['AT'].max()), float(delaq['AT'].mean()))
wind_speed = st.slider('Wind Speed (km/hr)', float(delaq['WS'].min()), float(delaq['WS'].max()), float(delaq['WS'].mean()))
relative_humidity = st.slider('Relative Humidity (%)', float(delaq['RH'].min()), float(delaq['RH'].max()), float(delaq['RH'].mean()))
precipitation = st.slider('Precipitation (mm)', float(delaq['RF'].min()), float(delaq['RF'].max()), float(delaq['RF'].mean()))
wind_direction = st.slider('Wind Direction (degrees)', float(delaq['WD'].min()), float(delaq['WD'].max()), float(delaq['WD'].mean()))

# Prediction button
if st.button('Predict Particulate Matter Concentration'):
    # Prepare input data for prediction
    input_data = [[temperature, wind_speed, relative_humidity, precipitation, wind_direction]]
    input_df = pd.DataFrame(input_data, columns=['AT', 'WS', 'RH', 'RF', 'WD'])

    # Make prediction
    prediction = PM_predictor.predict(input_df)

    # Display the result
    st.success(f'Predicted Particulate Matter Concentration: {prediction[0]:.2f} µg/m³')
