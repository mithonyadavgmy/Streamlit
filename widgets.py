import streamlit as st

st.title('Widgets')

name = st.text_input("Name")
st.write(name)

address = st.text_area("Address")
st.write(address)

st.date_input("Date")

st.time_input("Enter time")
if st.checkbox("Accept the terms & conditions", value=False):
    st.write("Thank You")

gen = st.radio("Gender",['M','F','O'], index = 0)
col = st.selectbox("Colors", ['r','g','b'],index=2)

st.write(gen,col)

colors = st.multiselect("Colors",['r','g','b'])
st.write(colors)

st.slider("Age", min_value=18, max_value=80,value=30, step=2)

st.number_input("Numbers:")

img = st.file_uploader("Upload a file: ")

if st.button("Submit"):
    st.write("Submission successfull")