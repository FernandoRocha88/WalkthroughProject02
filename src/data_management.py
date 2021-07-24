import streamlit as st
import pandas as pd
import numpy as np


def load_telco_data():
    return pd.read_csv("outputs/datasets/collection/TelcoCustomerChurn.csv")