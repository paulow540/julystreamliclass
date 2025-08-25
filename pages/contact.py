import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly as px




st.title("Contact us")


with st.expander("See explanation"):
    df = pd.read_csv(".\\.\\us_births.csv")
    st.dataframe(df.head())


col1, col2 = st.columns(2)


with col1:
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

with col2:
    st.subheader("Chart analysis")
    charttab1, charttab2, charttab3 = st.tabs(["Gender by Birth", "Day by Birth", "Month by Birth"])
    
    with charttab1:
        
        fig_gender_births = px.plot(
            df.groupby("gender")["births"].sum(),
            kind="bar",
            x='births',
            # y='Total births',
            title='Total births by Gender',
            # color='Gender'
        )
        st.plotly_chart(fig_gender_births, use_container_width=True)

    with charttab2:

        fig_day_births = px.plot(
            daybybirth_drop99 ,
            kind="bar",
            x="births",
            title = "Total births by day"

        )
        st.plotly_chart(fig_day_births, use_container_width=True)

    with charttab3:

        fig_month_births = px.plot(
            monthbybirth ,
            kind="bar",
            x="births",
            title = "Total births by Month"

        )
        st.plotly_chart(fig_month_births, use_container_width=True)


