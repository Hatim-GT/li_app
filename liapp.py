import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt


st.markdown("# LinkedIn User Prediction App")


Age = st.slider(label="Enter Your Age", 
        min_value=1,
        max_value=100,
        value=50)



education = st.selectbox(label="Highest Level of Education",
options=("No education",
    "Some High School",  
"High School Graduate", 
"Some College, no Degree", 
"Two -year College or University", 
"Bachelor's degree (BA,BS,etc.)", 
"Postgraduate Degree (MA, MS, PhD, MD, ect.)"))

if education == "No education":
    education = 1
elif education == "High School Graduate":
    education = 2
elif education == "Some College, no Degree":
    education = 3
elif education == "Two -year College or University":
    education = 4
elif education == "Bachelor's degree (BA,BS,etc.)":
    education = 5
elif education == "Postgraduate Degree (MA, MS, PhD, MD, ect.)":
    education = 6
elif education == "Some High School":
    education = 7
else:
    education = 8


Income = st.selectbox(label="Household Income",
options=("$10,000 to $20,000", 
"$20,000 to $30,000", 
"$40,000 to $50,000", 
"$50,000 to $100,000", 
"$100,000 to $150,000", 
"$150,000 to $200,000", 
"$200,000 to $300,000",
"$300,000+",
"Don't Know"))

if Income == "$10,000 to $20,000":
    Income =2
elif Income == "$20,000 to $30,000":
    Income =3
elif Income == "$30,000 to $40,000":
    Income =4
elif Income == "$50,000 to $100,000":
    Income =5
elif Income == "$150,000 to $200,000":
    Income =6
elif Income== "$200,000 to $300,000":
    Income =7
elif Income== "$300,000+":
    Income =8
else:
    Income= 9   



female = st.selectbox(label="Are you a male or female?",
options=("Female", 
"Male"))

if female == "Yes":
    female = 1
else:
    female = 0



    Parent = st.selectbox(label="Are you a parent?",
options=("Yes", 
"No"))

if Parent == "Yes":
    Parent = 1
else:
    Parent = 0



st.button("Submit")



st.write("You are a LinkedIN user")



