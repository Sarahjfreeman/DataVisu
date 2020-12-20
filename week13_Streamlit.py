#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:10:13 2020

@author: sarahjuliettefreeman
"""

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time

import streamlit as st

@st.cache
def load_hospitals():
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2

@st.cache
def load_inatpatient():
    df_inpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_2

@st.cache
def load_outpatient():
    df_outpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_2


st.title('Patient Care Quality and Estimated ')

df_hospital_2 = load_hospitals()
df_inpatient_2 = load_inatpatient()
df_outpatient_2 = load_outpatient()





hospitals_CA = df_hospital_2[df_hospital_2['state'] == 'CA']



#Bar Chart
st.subheader('Patient Experience CA Statewide')
bar1 = hospitals_CA['patient_experience_national_comparison'].value_counts().reset_index()
st.dataframe(bar1)

st.markdown('On an average, the patient experience with in the state of Oregon is above the national average')


st.subheader('Patient Experience Pie Chart')
fig = px.pie(bar1, values='patient_experience_national_comparison', names='index')
st.plotly_chart(fig)

# --------------

#Effectiveness of Care
st.subheader(' Hospitals in California- Effectiveness of Care')
bar2 = hospitals_CA['effectiveness_of_care_national_comparison'].value_counts().reset_index()
fig2 = px.bar(bar2, x='index', y='effectiveness_of_care_national_comparison')
st.plotly_chart(fig2)

#----------------


st.subheader('Map of Oregon Hospital Locations')

hospitals_CA_gps = hospitals_CA['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 
hospitals_CA_gps['lon'] = hospitals_CA_gps['lon'].str.strip('(')
hospitals_CA_gps = hospitals_CA_gps.dropna()
hospitals_CA_gps['lon'] = pd.to_numeric(hospitals_CA_gps['lon'])
hospitals_CA_gps['lat'] = pd.to_numeric(hospitals_CA_gps['lat'])

st.map(hospitals_CA_gps)



# ---------------
st.subheader(' Hospitals in Oregon- Safety of Care')
bar3 = hospitals_CA['safety_of_care_national_comparison'].value_counts().reset_index()
fig3 = px.bar(bar3, x='index', y='safety_of_care_national_comparison')
st.plotly_chart(fig2)


