import streamlit as st
from PIL import Image
from datetime import date, datetime
import pandas as pd
import matplotlib.pyplot as plt

#データ分析
df = pd.read_csv('./data/sample.csv',index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])

fig, ax = plt.subplots()
ax.plot(df.index, df['2021年'])
ax.set_title('matplotlib graph')
st.pyplot(fig)
