import pandas as pd
import streamlit as st
import numpy as np


a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic= {
    "Name": "Mithon",
    "Age": 20,
    "City": "Hyderabad"
}

data = pd.read_csv("Data/Salary_data.csv")

st.dataframe(a)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data,width=100, height=100)
# st.write(data)
st.table(data)
st.json(dic)
