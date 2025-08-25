import streamlit as st
import time

@st.dialog("Log in")
def login():
    with st.form("Log in"):
        email = st.text_input("Email", max_chars=50)
        password = st.text_input("Password",max_chars=8, type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted and  email and password:
            with st.spinner("..."):
                time.sleep(5)
                st.write("Log in")
         
    
