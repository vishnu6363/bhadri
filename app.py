import pickle
import streamlit as st
import numpy as np
import pandas as pd
#from flask import jsonify
import json




#loding the saved model
model=pickle.load(open('RandomForest.pkl','rb'))



#silde bar for navigation


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.pinimg.com/originals/7b/01/e6/7b01e6ddedddc9d10b24e7b73a06fd1a.gif");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


                 
 

  

   
  
  

    
'''-------------------------------------------------------------------''' 
def main():
    st.title('Find Which Crop Is Best For Your Farm')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">CROP YIELD PREDICTION </h2>
    </div>
   
     """
    st.markdown(html_temp,unsafe_allow_html=True)
   
    n=st.text_input('Enter the Value of Nitrogen')
    P=st.text_input('Enter the Value of Phosphorus')
    K=st.text_input('Enter the Value of Potassium')
    rainfall=st.text_input('Enter the Value of Rain Fall')
    ph=st.text_input('Enter the Value of PH Level') 
    temp=st.text_input('Enter the Value of Temperature') 
    humidity=st.text_input('Enter the Value of humidity')
    
    data = np.array([[n, P, K, temp, humidity, ph, rainfall]])
    
    
    result=''
   
    if st.button('Enter here to predict crop'):
        my_prediction = model.predict(data)
        final_prediction = my_prediction[0]       
        result= final_prediction
    st.success("The Crop is  {} \-".format(result))
    
    
if __name__=='__main__':
    main()    
    
    