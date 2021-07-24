import streamlit as st
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def load_telco_data():
    df = pd.read_csv("outputs/datasets/collection/TelcoCustomerChurn.csv")
    return df