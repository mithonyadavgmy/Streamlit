import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import streamlit as st
import time
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

st.title("Machine Learning")
res = st.file_uploader("Upload the Dataset: ")
if res != None:
    df = pd.read_csv(res)
    if df.isnull().sum().sum() != 0:
        for i in df.columns[df.isnull().any(axis=0)]:     #Nan Values with mean
            df[i].fillna(df[i].mean(),inplace=True)
    r1 = st.checkbox("Show DataFrame", value=False)
    if r1 == True:
        st.dataframe(df, width=500, height=500)
    trainData = df.iloc[:,:-1]
    testData = df.iloc[:,-1]
    st.markdown("""
## Train Test Split
""")

    testSize = st.slider("Test Size", min_value=0.1, max_value=1.0, step=0.1, value=0.2)
    x_train,x_test,y_train,y_test = train_test_split(trainData, testData, test_size=testSize)

    st.markdown("""
## Model Selection
""")
    model = st.selectbox("Select an Algorithm: ",["Linear Regression","Ridge Regression","Lasso Regression",'ElasticNet',"Support Vector Regression","Decision Tree Regreesor"],index=0)
    if model == "Linear Regression":
        machine = LinearRegression()
        cross = LinearRegression()
    if model == "Ridge Regression":
        machine = Ridge()
        cross = Ridge()
    if model == "Lasso Regression":
        machine= Lasso()
        cross = Lasso()
    if model == "ElasticNet":
        machine = ElasticNet()
        cross = ElasticNet()
    if model == "Support Vector Regression":
        machine = SVR()
        cross = SVR()
    if model == "Decision Tree Regreesor":
        machine = DecisionTreeRegressor()
        cross = DecisionTreeRegressor()

    r2 = machine.fit(x_train,y_train)
    st.write(r2)
    st.success("Model trained Successfully")
    st.balloons()

    st.markdown("""
## Performance
""")
    score1 = machine.score(x_test,y_test)
    st.write("Accuracy Score:",score1)
    score2 = cross_val_score(cross, trainData, testData)
    st.write("Cross Val Score:",score2.mean())

    st.markdown("""
## Predict Value
""")
    cols = df.shape[1]-1
    values = []
    for i in range(cols):
        v1 = st.number_input("Enter value",i)
        values.append(v1)
    values = np.array(values)
    value = values.reshape(-1,1)
    pred = machine.predict([values])
    st.write("Predicted Values: ",pred)




