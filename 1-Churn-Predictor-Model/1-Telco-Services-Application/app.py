#Import libraries
import streamlit as st
  import pandas as pd
  import numpy as np from PIL import Image import joblib import os
#Import python scripts
  from preprocessing import preprocess def
main ():
#Setting Application title
st.
title ("Telco Customer Churn Prediction App")
#Setting Application description
st.
markdown ("" "
     :dart:  This Streamlit app is made to predict customer churn in a ficitional telecommunication use case.
    The application is functional for both online prediction and batch data prediction. \n
    " "")
  st.
markdown ("<h3></h3>", unsafe_allow_html = True)
#Setting Application sidebar default
  imager =
  Image.
open ("1-Churn-Predictor-Model/1-Telco-Services-Application/images/App.png")
add_selectbox =
st.sidebar.selectbox ("How would you like to predict?",
		("Online",
		 "Batch")) st.sidebar.
info ("This app is created to predict Customer Churn") st.sidebar.image (imager)
#load the model from disk
  st.subheader ("Upload The Secure Model")
  uploaded_model = st.file_uploader ("Choose a file", key = 1)
  if uploaded_model
is not None:
  model = joblib.load (uploaded_model) if add_selectbox
  == "Online":
    st.info ("Input data below")
#Based on our optimal features selection
      st.subheader ("Demographic data")
      gender = st.selectbox ("Gender:", ("Male", "Female"))
      married = st.selectbox ("Married:", ("Yes", "No"))
      dependents = st.number_input ("Number of dependents", min_value =
				    0, max_value = 100, value =
				    0) st.subheader ("Payment data")
#"""
      tenure =
      st.slider ("Number of months the customer has stayed with the company",
		 min_value = 0, max_value = 72, value = 0,) paperlessbilling =
      st.selectbox ("Paperless Billing", ("Yes", "No")) monthlycharges =
      st.number_input ("The amount charged to the customer monthly",
		       min_value = 0, max_value = 1000, value = 0,)
#"""
      st.subheader ("Services signed up for")
#"""
      mutliplelines =
      st.selectbox ("Does the customer have multiple lines",
		    ("Yes", "No")) phoneservice =
      st.selectbox ("Phone Service:", ("Yes", "No"))
#internetservice = st.selectbox("Does the customer have internet service", ("Yes", "No"))
      onlinesecurity =
      st.selectbox ("Does the customer have online security",
		    ("Yes", "No")) onlinebackup =
      st.selectbox ("Does the customer have online backup",
		    ("Yes", "No")) techsupport =
      st.selectbox ("Does the customer have technology support",
		    ("Yes", "No")) streamingtv =
      st.selectbox ("Does the customer stream TV", ("Yes", "No")) dpp =
      st.selectbox ("Does the customer have Device Protection Plan",
		    ("Yes", "No")) nofref =
      st.number_input ("Number of Referrals made by the customer", min_value =
		       0, max_value = 100, value = 0,) offer =
      st.selectbox ("Offer type subscribed by the customer ",
		    ("Offer_Offer A", "Offer_Offer B", "Offer_Offer C",
		     "Offer_Offer D", "Offer_Offer E",),) intype =
      st.selectbox ("Internet type subscribed by the customer",
		    ("Internet Type_Cable", "Internet Type_DSL",
		     "Internet Type_Fiber Optic",
		     "Internet Type_None",),) contract =
      st.selectbox ("Contract",
		    ("Month-To-Month", "One Year",
		     "Two Year")) paymentmethod =
      st.selectbox ("Payment Method",
		    ("Bank Withdrawl", "Credit Card", "Mailed Check"))
#"""
      data =
    {
  "Gender": gender, "Married": married, "Number_of_Dependents": dependents, "Tenure_in_Months": tenure, "Contract": contract, "Paperless_Billing": paperlessbilling, "Payment_Method": paymentmethod, "Monthly_Charge": monthlycharges, "Multiple_Lines": mutliplelines, "Phone_Service": phoneservice, "Online_Security": onlinesecurity, "Online_Backup": onlinebackup, "Premium_Tech_Support": techsupport, "Streaming_TV": streamingtv, "Device_Protection_Plan": dpp, "Number_of_Referrals": nofref, "Offer": offer, "Internet_Type":intype,}
features_df = pd.DataFrame.from_dict ([data])
  st.markdown ("<h3></h3>", unsafe_allow_html = True)
  st.write ("Overview of input is shown below")
  st.markdown ("<h3></h3>", unsafe_allow_html = True)
  st.dataframe (features_df)
#Preprocess inputs
  preprocess_df = preprocess (features_df, "Online")
  prediction = model.predict (preprocess_df) if st
.button ("Predict"):
  if prediction
  == 1:
    st.warning ("Yes, the customer will terminate the service.")
    else
  :
    st.success ("No, the customer is happy with Telco Services.")
    else
  :
    st.subheader ("Dataset upload")
      uploaded_file = st.file_uploader ("Choose a file", key = 2)
      if uploaded_file
    is not None:
      data = pd.read_csv (uploaded_file)
#Get overview of data
	st.write (data.head ())st.markdown ("<h3></h3>", unsafe_allow_html =
					    True)
#Preprocess inputs
	preprocess_df = preprocess (data, "Batch") if st
      .button ("Predict"):
#Get batch prediction
#prediction = model[0].predict(preprocess_df)
	if uploaded_model
	is not None:
	  prediction = model.predict (preprocess_df)
	    prediction_df = pd.DataFrame (prediction, columns =
					  ["Predictions"]) prediction_df =
	    prediction_df.replace (
				       {
	1: "Yes, the customer will terminate the service.", 0:"No, the customer is happy with Telco Services.",}
)
	else
	:
	st.write ("Proceed To Upload Indispensable Model")
	    st.markdown ("<h3></h3>", unsafe_allow_html = True)
	    st.subheader ("Prediction") st.write (prediction_df) if __name__
	== "__main__":
	  main ()
