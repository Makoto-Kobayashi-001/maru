import streamlit as st
from PIL import Image
from datetime import date, datetime
import pandas as pd

#データ分析
df = pd.read_csv('sample.csv',index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])

