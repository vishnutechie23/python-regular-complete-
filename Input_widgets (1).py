import numpy as np 
import pandas as pd 

import streamlit as st 

import warnings 
warnings.filterwarnings("ignore") 

import datetime

st.title("Streamlit Input Widgets Demo") 

st.header("Interactive Input Elements")

# Text Elements 

name = st.text_input("Enter your name : ")

if name:
    st.write(f"Hello {name}")
    
feedback = st.text_area("Enter your Freedback : ") 

if feedback:
    st.write(f"Thank you for your Feedback!")
    
# Numeric Inputs

st.header("Numberic Input") 

age = st.number_input("Enter your age : ", min_value= 0, max_value = 1000, step = 1) 

st.write(f"Your Age Is {age}")

rating = st.slider(f"Rate {name} : ",min_value=1, max_value=5)

st.write(f"You Rated : {rating}/5")

# Selection Widgets 

st.subheader("Selection Widets") 

subscribe = st.checkbox("Subscribe To Vampire Diaries") 

girlfriend = st.radio("Select Girlfriend (one at a time) : ", options= ['Elena', 'Caroline', 'Andy', 'Katherine', 'Rebecca', 'Lexi', 'Vicki'])

# Dropdown 
team_member = st.selectbox("Choose Team Member : ", options= ['Ric', 'Enzo', 'Stefan', 'Geremy', 'Elijah', 'Klaus']) 

st.write(f"Team Member Selected : {team_member}")

team = st.multiselect("Choose Team Member", options= ['Ric', 'Enzo', 'Stefan', 'Geremy', 'Elijah', 'Klaus'])

st.write(f"Team Selected : {team}")


# Buttons 

if st.button("Click Me"):
    st.success("Congratuations!")
    st.warning("adsjlfjd") 
    st.error("dflajsdfl;j") 
    
    
# Date & Time Elements

selected_date = st.date_input("Pick Data : ", 
value = datetime.date.today()) 
st.write(f"Selected Date : {selected_date}")

selected_time = st.time_input("Pick time : ", value= datetime.time(12, 0))
st.write(f"Selected Time : {selected_time}")