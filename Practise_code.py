import streamlit as st
import plotly
import numpy as np
import pandas as pd
import plotly.figure_factory as ff

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)-2

hist_data = [x1,x2,x3]
group_labels = ['Group1', 'Group2','Group3']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2,.25,.5])

st.plotly_chart(fig, use_container_width=True)

st.text("_____"*100)

df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76, -122.4], columns= ['lat', 'lon'])

st.map(df)