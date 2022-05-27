# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:47:23 2022

@author: AIWorld
"""

import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide")
st.title('Condo Price Prediction with Regression 😍')

df = pd.read_csv("condo_price_predict.csv")
df = df.drop(columns=["Unnamed: 0","price"],axis=1) 
column_names = list(df.columns.values)
input_df = pd.DataFrame(columns = column_names)

df = df.drop(columns=['size', 'floor', 'bed', 'toilet','bts','uni'],axis=1) 
location_lst = list(df.columns.values)


st.sidebar.header('Please insert your input here')
location = st.sidebar.selectbox('select location', location_lst)

size = st.sidebar.number_input('What size?', min_value=1, max_value=500, value=30, step=1)
floor = st.sidebar.number_input('What floor?', min_value=1, max_value=500, value=10, step=1)
bed = st.sidebar.slider("How many bedroom?", 1, 10, 1)
toilet = st.sidebar.slider("How many toilet?", 1, 10, 1)

nearBTS = st.sidebar.selectbox( 'near BTS?', ('no', 'yes'))
nearUniversity = st.sidebar.selectbox( 'near University?', ('yes', 'no'))
if nearBTS == 'yes':
    nearBTS = 1
else:
    nearBTS = 0

if nearUniversity == 'no':
    nearUniversity = 0
else:
    nearUniversity = 1


input_lst = {'size':size, 'floor':floor, 'bed':bed, 'toilet':toilet,'bts':nearBTS,'uni':nearUniversity,location:1 }
#append row to the dataframe
input_df = input_df.append(input_lst, ignore_index=True)
input_df = input_df.fillna(0)
input_df = input_df.astype(int)


with open('condo_price_pkl' , 'rb') as f:
    lr = pickle.load(f)

predict_price = lr.predict(input_df)

st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;text-align:center;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">The estimate price of condo is</p>', unsafe_allow_html=True)

original_title = '<p style="font-family:Cooper Black; color:Blue; font-size: 40px;text-align:center;">'+format(int(predict_price),',d')+' Bath</p>'
st.markdown(original_title, unsafe_allow_html=True)

