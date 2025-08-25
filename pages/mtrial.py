import streamlit as st
import numpy as np
import pandas as pd

st.title("Trail us")


tab1, tab2, tab3, tab4 = st.tabs(["Cat", "Dog", "Owl", "Data"])

with tab1:
     st.header("A cat")
     st.image("././static/cat.jpg", width=200)
with tab2:
     st.header("A dog")
     st.image("././static/dog.jpg", width=200)
with tab3:
     st.header("An owl")
     st.image("././static/owl.jpg", width=200)

with tab4:
    df = pd.read_csv("././us_births.csv")
    st.dataframe(df.head())