import streamlit as st
from PIL import Image
from datetime import date, datetime
import pandas as pd
import os

#データ分析
st.text(os.path.abspath('./supu_app/data/sample.csv'))
df = pd.read_csv(os.path.abspath('./supu_app/data/sample.csv'),index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])

