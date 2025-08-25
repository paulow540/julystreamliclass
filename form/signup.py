import streamlit as st
import time

@st.dialog("Sign up")
def sign_up():
    with st.form("Sign up"):
        first = st.text_input("First name", max_chars=20)
        last = st.text_input("Last name",max_chars=20)
        email = st.text_input("Email", max_chars=50)
        password = st.text_input("Password",max_chars=8, type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted and first and last and email and password:
            with st.spinner("..."):
                time.sleep(5)
                st.write("Log in")
            if not first:
                st.write("invalide")
    
