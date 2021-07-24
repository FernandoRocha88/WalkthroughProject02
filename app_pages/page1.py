import streamlit as st
from src.data_management import load_telco_data

def page1_body():
    st.write("### Customer Base Churn Study")
    st.write(
        f"* It answers biz requirement 1 \n\n"
        f"As a customer I am interested to understand the patterns from my customer base, "
        f"so I can better manage churn levels.")


    # load data
    df = load_telco_data()
    st.write("#### Snapshot: Collected Data")
    st.write(f"Dataset shape: {df.shape}")
    st.write(df)
    st.write("---")


    # correlation

