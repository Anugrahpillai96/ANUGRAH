import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and DataFrame
daq = pd.read_pickle('daq.pkl')
model = pickle.load(open('final_pipeline.pkl', 'rb'))

# Streamlit app
st.title('Particulate Matter Concentration Prediction App')

# Input features
temperature = st.slider('Temperature (degC)', float(daq['AT'].min()), float(daq['AT'].max()))
wind_speed = st.slider('Wind Speed (km/hr)', float(daq['WS'].min()), float(daq['WS'].max()))
relative_humidity = st.slider('Relative Humidity (dec)', float(daq['RH'].min()), float(daq['RH'].max()))
precipitation = st.slider('Precipitation (mm)', float(daq['RF'].min()), float(daq['RF'].max()))

# Prediction button
if st.button('Predict Particulate Matter Concentration'):
    # Prepare input data for prediction
    input_data = [[temperature, wind_speed, relative_humidity, precipitation]]
    input_df = pd.DataFrame(input_data, columns=['AT','WS','RH','RF'])

    # Make prediction
    prediction = model.predict(input_df)

    # Display the result
    st.success(f'Predicted Particulate Matter Concentration: {prediction[0]:.2f} µg/m³')
