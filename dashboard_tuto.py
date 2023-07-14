import streamlit as st 
import pandas as pd
from flask import Flask
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown('<h1 style="color:blue;">ATSAMA AHANDA LIANNE CEDRIQUE</h1>', unsafe_allow_html=True)
st.write("Ravie de vous avoir sur mon application !") 

impression = pd.read_csv('impressions.csv')
clics = pd.read_csv('clics.csv')
achats = pd.read_csv('achats.csv')

base1 = pd.merge(impression,clics, on = 'cookie_id')
base = pd.merge(base1,achats, on = 'cookie_id')
base 

CA= base['price'].sum()
st.write(f"<span style='color:purple; font-size:40px;'>Chiffre d'affaires : {CA} € </span>", unsafe_allow_html=True)


st.subheader('Age en fonction des produits')
box= px.box(base, x= 'product_id' , y= 'age')
st.plotly_chart(box)

st.subheader('Prix en fonction des produits')
hist= px.histogram(base, x= 'product_id' , y= 'price')
st.plotly_chart(hist)


import plotly.express as px
import plotly.graph_objects as go 


# Créer le diagramme circulaire
fig = px.pie(base, values='dept', names='gender')

# Afficher le diagramme dans Streamlit
st.plotly_chart(fig)

graph= go.Figure(
     data=[go.Bar(y=base['age'])],
     layout_title_text='A Figure Displayed with graph.show()'
     )
st.write(graph) 







if __name__== '___dasboard_tuto__':
  app.run(debug= True)
