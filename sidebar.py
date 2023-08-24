import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")

data = {
    "num": [x for x in range(1,11)],
    "square": [x**2 for x in range(1,11)],
    "Twice": [x*2 for x in range(1,11)],
    "Trice": [x*3 for x in range(1,11)],
}

df = pd.DataFrame(data = data)

rad = st.sidebar.radio("Navigation",['Home','About us'],index = 0)

if rad == 'Home':
    col = st.sidebar.selectbox("Select a Columns: ",df.columns)

    plt.plot(df['num'],df[col])

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

else:
    st.write("Your in About us page")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    else:
        st.balloons()
        time.sleep(5.0)
        st.error("Error")
        st.success("Success")
        st.info("Information")
        st.exception(RuntimeError("This is an exception"))
        st.warning("This is a Warning")

