import streamlit as st

st.title("registration Form")

first,last = st.beta_columns(2)

first.text_input("First Name")
last.text_input("Last Name")