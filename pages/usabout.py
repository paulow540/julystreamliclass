import streamlit as st

st.title("About us", anchor=False)



col1, col2, col3 = st.columns(3)

with col1:
     st.header("A cat", anchor=False)
     st.image(".\\.\\static\\cat.jpg")

with col2:
     st.header("A dog", anchor=False)
     st.image(".\\.\\static\\dog.jpg")

with col3:
     st.header("An owl",  anchor=False)
     st.image(".\\.\\static\\owl.jpg")
