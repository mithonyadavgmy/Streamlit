import streamlit as st

st.title("Hello Streamlit")

st.header("Header")

st.subheader("SubHeader")

st.text('This is a sample text')

st.markdown("""
            # h1 tag
            ## h2 tag
            ### h3 tag
            :moon: <br>
""", True)

# st.latex()

st.write("Golla","Mithon", "Yadav")
st.write("# Write")

dict = {
    1: ['a','b','c'],
    2: ['d','e','f'],
    3: ['g','h','i']
}
st.write(dict)