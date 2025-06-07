import streamlit as st
from PIL import Image
from datetime import date, datetime
import os

#タイトルや文字列
st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

#画像
st.text(os.path.abspath('./supu_app/data/Sample01.jpg'))
image = Image.open(os.path.abspath('./supu_app/data/Sample01.jpg'))
st.image(image, width=200)

