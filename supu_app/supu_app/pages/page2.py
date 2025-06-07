import streamlit as st
from PIL import Image
from datetime import date, datetime

with st.form(key='profile_form'):
	#入力
	name = st.text_input('名前')
	address = st.text_input('住所')

	#選択
	age_category = st.radio(
		'年齢層',
		('子供(18才未満)','大人(18才以上)')
	)

	#複数選択
	hobby = st.multiselect(
		'趣味',
		('スポーツ','散歩','読書','なし')
	)
	
	#チェックボックス
	mail_subscribe = st.checkbox('メルマガを購読する')

	#スライダー
	height = st.slider('身長',min_value=110,max_value=210)

	#日付
	start_date = st.date_input(
		'開始日',
		date(2025, 7, 1)

	)

	#カラーピッカー
	color = st.color_picker('色','#00f900')

	#ボタン
	submit_button = st.form_submit_button('送信')
	cancel_button = st.form_submit_button('キャンセル')

	if submit_button:
		st.text(f'ようこそ {address}の{name}さん！')
		st.text(f'年齢層:{age_category}')
		st.text(f'趣　味:{",".join(hobby)}')

