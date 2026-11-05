import streamlit as st

# to run file : streamlit run filename 

# basic text
st.write(" st.write -- My name is VISHNU")
st.title(" st.title -- My name is VISHNU")
st.text("st.text -- My name is VISHNU")
st.header(" st.header -- My name is VISHNU")
st.subheader(" st.subheader -- My name is VISHNU")


# for text input 
a = st.text_input("Enter your name")
st.write(a)

# for no inout
a = st.number_input("Enter your name : ", min_value=1, max_value=1000)
st.write(a)


# Buttons 
if st.button("Click me "):
    st.write("clicked")

c = st.selectbox(
    "Choose a course",
    ["None","DA", "DS", "AI", "ML", "DL"],
    index = 0,
)
st.write("You had choosed :", c)

# Radio buttons 
# if st.button("Click me "):
#     st.write("clicked")

b = st.radio(
    "Choose a course",
    ["DA", "DS", "AI", "ML", "DL"]
)
st.write("You had choosed :", b)

# Checkbox
d = st.checkbox("Are you agree ? ")
if d :
    st.write("Allowed")

# Slider 
st.slider("Select Range", 0 ,100, 50, step = 10)

# Read Dataframe 

import streamlit as st
import pandas as pd
df = pd.read_csv("C:\\Users\\vishn\python regular\\Numpy\\employee_data.csv")
st.dataframe(df)

