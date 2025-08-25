import streamlit as st
import pandas as pd

with st.expander("See explanation"):
    df = pd.read_csv(".\\.\\us_births.csv")
    st.dataframe(df.head())

st.subheader("Table analysis")
tab1, tab2, tab3 = st.tabs(["Total Birth", "Maximum Birth", "Minimum Birth"])
    
with tab1:
        st.markdown("*Total* **Birth**.")
        total_birth = df["births"].sum()
        st.write(total_birth)
    
with tab2:
        st.markdown("*Maximum* **Birth**.")
        max_birth = df["births"].max()
        st.write(max_birth)

with tab3:
        st.markdown("*Maximum* **Birth**.")
        min_birth = df["births"].min()
        st.write(min_birth)

st.subheader("Birth analysis")
sectab1, sectab2, sectab3 = st.tabs(["Gender by Birth", "Day by Birth", "Month by Birth"])
with sectab1:
        gender_by_birth = df.groupby("gender")["births"].count()
        st.table(gender_by_birth)

with sectab2:
        daybybirth =df.groupby("day")["births"].count()
        # st.dataframe(daybybirth)
        daybybirth_drop99 = daybybirth.loc[0:len(daybybirth)-1]
        st.dataframe(daybybirth_drop99)

with sectab3:
        monthbybirth = df.groupby("month")["births"].count().sort_values(ascending=False)
        st.dataframe(monthbybirth)