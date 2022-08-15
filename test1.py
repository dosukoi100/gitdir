
#gitの練習です

import time

print('初めてのGit')

lists = [1,2,3,4,5]

for i in lists:
    print(i)
    time.sleep(0.4)

#ここからStreamlitのコードを書いて行きます

import streamlit as st

st.title('タイトルです')

text1 = st.text_input('ここに好きな言葉を入れてください')
st.write('あなたの好きな言葉は{}ですね?'.format(text1))

#ここからStreamlitのコードを書いて行きます

import streamlit as st

st.title('タイトルです')

text1 = st.text_input('ここに好きな言葉を入れてください')
st.write('あなたの好きな言葉は{}ですね?'.format(text1))

#プルリクエストの練習です
