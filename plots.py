import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.rand(100,3),
    columns=['a','b','c']
)

# chart = alt.Chart(data).mark_circle().encode(
#     x = 'a', y = 'b', tooltip=['a','b']
# )

# plt.scatter(data['a'], data['b'])
# plt.title("Scatter")
# st.pyplot()

st.write(data)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

st.graphviz_chart('''
digraph{
                  watch->like
                  like -> share
                  share -> Subscribe
                  share -> watch
}
''')

# st.image("path")

# st.audio("path")

# st.video("path")