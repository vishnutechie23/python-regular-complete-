import numpy as np 
import pandas as pd 
from datetime import time,datetime

import streamlit as st 

st.set_page_config(layout = 'centered') 

st.title("Interactive Input Elements")

name = st.text_input("Enter your Name ")

if name:
    st.write(f"Welcome {name}")
    
description = st.text_area("Enter Person's Description ")

if description:
    st.write(description) 
    
age = st.number_input("Enter the Age ", min_value = 0, max_value = 120, step = 1) 

st.write(f"{name} is {age} years old")

rating = st.slider(f"Rate {name}", min_value= 1, max_value = 5)
st.write(f"Rating : {rating}")

subscribe = st.checkbox("Subscribe ")

if subscribe:
    st.write("Welcome to Narutoverse")
    
gender = st.radio("Select Gender : ", options=['Male', 'Female', 'Others']) 
st.write(f"Selected : {gender}")

favorite_list = st.selectbox('Choose Favorite Character : ',options=['Naruto','Sasuke', 'Itachi','Kakashi','Madara','Minato','Pain'])

ninja_squad = st.multiselect("Select your Squad", ['Naruto','Sasuke', 'Itachi','Kakashi','Madara','Minato','Pain'])

if st.button("Click Me"):
    st.success("Welcome")
    
selected_date = st.date_input("Pick A Date : ", value = datetime.today()) 
st.write(f"Selected Data : {selected_date}")

selected_time = st.time_input("Pick A Time : ", value =time(12, 0)) 
st.write(f"Selected Time : {selected_time}")