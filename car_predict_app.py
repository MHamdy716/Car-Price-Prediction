import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import joblib

# building the interface
st.title("Car Sell Price Prediction App")
st.image("car_project.png")
st.text("""This application is biult to predict the car pricing base on the manufcure company , production year , 
        number km has car driven , type of fuel, seller type, mileage (KM/L),  transmisstion, Past owner Engine CC , Max power 
        of the motor,and finaly the number of seats.""")
st.text("Please fill-in the following data")

company_list = ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Fiat', 'Datsun', 'Volkswagen',
       'Nissan', 'BMW', 'Mercedes-Benz']
company = st.selectbox("company name", company_list)

year = st.slider( "production year", 1983 ,2020)

km_driven = st.slider("Driven Km", 10.00 ,300.00)

mileage = st.slider( "mileage(km/l)", 10.00 ,30.72)

engine = st.number_input( "engine(CC)")

max_power = st.number_input( "max_power(bhp)")

seats = st.number_input("No. of seats")

fuel_type = st.radio("fuel type", ['Diesel', 'Petrol', 'LPG', 'CNG'])

seller_type_list = ['Individual', 'Dealer', 'Trustmark Dealer']
seller_type = st.selectbox("Seller", seller_type_list)

transmission = st.radio("transnission type", ['Manual', 'Automatic'])

owner_list = ['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner']
owner = st.selectbox("owner", owner_list)

btn = st.button("submit")

if btn == True:
    scaler = joblib.load("Scaler.pkl")
    Target_scaler = joblib.load("Target_scaler.pkl")
    model = joblib.load("Model.pkl")

    # encoding categoriacl data

    company_map  = {'BMW': 0,  'Chevrolet': 1,  'Datsun': 2,  'Fiat': 3,
    'Ford': 4,  'Honda': 5,  'Hyundai': 6, 'Mahindra': 7,
    'Maruti': 8,  'Mercedes-Benz': 9, 'Nissan': 10,'Renault': 11,
    "Skoda": 12,  'Tata': 13,  'Toyota': 14,  'Volkswagen': 15}

    fuel_map = {'Diesel':1, 'Petrol':3, 'LPG':2, 'CNG':0}
    seller_map = {'Individual':1, 'Trustmark Dealer':2, 'Dealer':0}
    transmission_map = {'Manual':1, 'Automatic':0}
    owner_map = {'First Owner':0 ,'Fourth & Above Owner':1,  'Second Owner':2, 'Third Owner':3}

    company_encoded = company_map[company]
    fuel_encoded = fuel_map[fuel_type]
    seller_encoded = seller_map[seller_type]
    transmission_encoded = transmission_map[transmission]
    owner_encoded = owner_map[owner]

    # st.write(fuel_encoded,seller_encoded,transmission_encoded,owner_encoded)

    input_data = np.array([[year, km_driven, mileage, engine, max_power, seats,
                             company_encoded, fuel_encoded, seller_encoded,
                               transmission_encoded, owner_encoded]])
    # st.write(input_data)
    # st.write(scaler.transform(input_data))
    input_data_scaled = scaler.transform(input_data)

    pred_scaled = model.predict(input_data_scaled)
    # st.write(pred_scaled)

    pred_org = Target_scaler.inverse_transform(pred_scaled.reshape(-1,1))
    st.write("the predicted selling price will be",pred_org)