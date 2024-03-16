import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import joblib

loaded_model = joblib.load(open("Personal_loan_model", 'rb'))

st.title("Pesonal Loan prediction app")
with st.form(key="form1"):
    left_column,mid,right_column = st.columns(3)
    with right_column:
        Age=st.number_input(label="Enter your age")
        Family=st.number_input(label="Enter your family")
        CCAvg=st.number_input(label="Enter your CCAvg")
        SecuritiesAccount=st.checkbox('account secured')
        if SecuritiesAccount:
            SecuritiesAccount=1
        else:
            SecuritiesAccount=0
        Online=st.checkbox('online')
        if Online:
            Online=1
        else:
            Online=0
        CreditCard=st.checkbox('cridit card')
        if CreditCard:
            CreditCard=1
        else:
            CreditCard=0
        Predict=st.form_submit_button(label="Predict")    
    with left_column:
        Name=st.text_input(label="Enter your Name")
        ID=st.number_input(label="Enter your ID")
        Experience=st.number_input(label="Enter your Experience")
        Education=st.number_input(label="Enter your Education")
        
        
    with mid :
        Income=st.number_input(label="Enter your income") 
        ZIPCode=st.number_input(label="Enter your ZIP Code")
        Mortgage=st.number_input(label="Enter your Mortgage")
        CDAccount=st.number_input(label="Enter your CD Account")
        
def prepare_input_data_for_model(Income,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard):
    Income_Norm=np.log(Income+1)
    Income_Norm=(Income_Norm-2.397895)/(5.416100-2.397895)
    CCAvg_Norm=np.log(CCAvg+1)
    CCAvg_Norm=(CCAvg_Norm)/(2.197225)
    Mortgage_Norm=Mortgage/635
    A = [Income,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard,Income_Norm,CCAvg_Norm,Mortgage_Norm]
    sample = np.array(A).reshape(-1,len(A))

    return sample        

if Predict:
            sample=prepare_input_data_for_model(Income,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard)
            pred_Y = loaded_model.predict(sample)

            if pred_Y == 1:
                #st.write("## Predicted Status : ", result)
                st.write('### You can get the loan MR.', Name)
                st.balloons()
                st.balloons()
                st.balloons()
            else:
                st.write("### You cann't get the loan MR.", Name)        

        









    
  
        
   
