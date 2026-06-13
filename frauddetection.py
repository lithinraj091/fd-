import streamlit as st
import joblib
import pandas as pd 
model=joblib.load("fraud_detection_model.pkl")
st.title("FRAUD DETECTION MODEL")
st.markdown("enter transaction details and use predict button")
st.divider()
TRANSACTION_TYPE=st.selectbox("Select Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"],key="type")
AMOUNT=st.number_input("Enter Transaction Amount",key="amount",min_value=0.0,value=0.0)
oldbalance=st.number_input("Enter Old Balance(sender)",key="old_balance(sender)",min_value=0.0,value=0.0)
newbalance=st.number_input("Enter New Balance(sender)",key="new_balance(sender)",min_value=0.0,value=0.0)
oldbalance_dest=st.number_input("Enter Old Balance(receiver)",key="old_balance(receiver)",min_value=0.0,value=0.0)
newbalance_dest=st.number_input("Enter New Balance(receiver)",key="new_balance(receiver)",min_value=0.0,value=0.0)
if st.button("predict"):
    input_data=pd.DataFrame({"type":[TRANSACTION_TYPE],"amount":[AMOUNT],"oldbalanceOrg":[oldbalance],"newbalanceOrig":[newbalance],"oldbalanceDest":[oldbalance_dest],"newbalanceDest":[newbalance_dest]})
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")    