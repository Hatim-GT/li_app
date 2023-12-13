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











s = pd.read_csv(r'C:\Users\zooke\Desktop\Final Project\social_media_usage.csv')

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "DatabaseSample.xlsx"


import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

ss = pd.DataFrame({
    "sm_li":np.where(s["web1h"] == 1, 1, 0),
    "Income":np.where(s["income"]==9, np.nan, s["income"]),
    "Age":np.where(s["age"]>98, np.nan, s["age"]),
    "education":np.where(s["educ2"] >8,np.nan, s["educ2"]),
    "marital":np.where(s["marital"] == 1, 1, 0),
    "Parent":np.where(s["par"]==1,1,0),
    "female":np.where(s["gender"] == 2, 1, 0)})

ss.dropna(inplace=True)



# Target (y) and feature(s) selection (X)
y = ss["sm_li"]
X = ss[["Age", "education", "Income", "female", "Parent"]]

# Split data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    stratify=y,       # same number of target in training & test set
                                                    test_size=0.2,    # hold out 20% of data for testing
                                                    random_state=987) # set for reproducibility

# X_train contains 80% of the data and contains the features used to predict the target when training the model. 
# X_test contains 20% of the data and contains the features used to test the model on unseen data to evaluate performance. 
# y_train contains 80% of the the data and contains the target that we will predict using the features when training the model. 
# y_test contains 20% of the data and contains the target we will predict when testing the model on unseen data to evaluate performance.


# Initialize algorithm 
lr = LogisticRegression(class_weight="balanced")

# Fit algorithm to training data
lr.fit(X_train, y_train)

# Make predictions using the model and the testing data
y_pred = lr.predict(X_test)




# New data for features: age, education, Income, female, Parent
person = [Age, education, Income, female, Parent]

# Predict class, given input features
predicted_class = lr.predict([person])

# Generate probability of positive class (=1)
probs = lr.predict_proba([person])


st.write(f"Prediction: {predicted_class[0]}")
st.write("(1 = LinkedIn User, 0 = Not a LinkedIn User)")

st.write(f"Probability that you are a LinkedIn User: {probs[0][1]}")









