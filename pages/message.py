import streamlit as st
import pandas as pd
import numpy as np
import time
import sqlite3
# from form.login import login
from form.signup import sign_up

st.title("Message us")


with st.expander("See explanation"):
    df = pd.read_csv("././us_births.csv")
    st.dataframe(df.head())

# SIMPLE FORM
# with st.form("my_form"):
#      st.write("Inside the form")
#      slider_val = st.slider("Form slider")
#      checkbox_val = st.checkbox("Form checkbox")

#      # Every form must have a submit button.
#      submitted = st.form_submit_button("Submit")
#      if submitted:
#          st.write("slider", slider_val, "checkbox", checkbox_val)
# st.write("Outside the form")




but = st.button("Sign up")
if but:

    sign_up()
