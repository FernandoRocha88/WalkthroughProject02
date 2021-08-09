import streamlit as st
from src.data_management import load_telco_data
from src.correlation_analysis import CalculateCorrAndPPS, DisplayCorrAndPPS

def page_customer_base_churn_body():
    st.write("### Customer Base Churn Study")
    st.write(
        f"#### As a customer I am interested to understand the patterns from my customer base, "
        f"so I can better manage churn levels.")


    # load data
    df = load_telco_data()

    # hard copied from data visualization notebook
    vars_to_study = ['Contract', 'InternetService',
                    'OnlineSecurity', 'PaymentMethod',
                    'TechSupport', 'tenure']

    # inspect collected data
    if st.checkbox("Inspect Customer Base"):
        inspect_data(df)
    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"The most correlated variable are: **{vars_to_study}**")

    df_eda = df.filter(vars_to_study + ['Churn'])
        

    # Individual plots per variable
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.checkbox("Churn Levels per Variable Distribution"):
        churn_level_per_variable(df_eda)
        
    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write("asasd")
        # churn_across_features(df[vars_to_study])
        


def inspect_data(df):
    st.write(
        f"For dataset explanation, visit project "
        f"[repo](https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/README.md)")
    st.write(f"Dataset shape: {df.shape}")
    st.write(df)
    


import matplotlib.pyplot as plt
import seaborn as sns
def plot_categorical(df, col, target_var):

  plt.figure(figsize=(12, 5))
  sns.countplot(data=df, x=col, hue=target_var,order = df[col].value_counts().index)
  plt.xticks(rotation=90) 
  plt.title(f"{col}", fontsize=20,y=1.05)        
  st.pyplot()

def plot_numerical(df, col, target_var):
  plt.figure(figsize=(8, 5))
  sns.histplot(data=df, x=col, hue=target_var, kde=True,element="step") 
  plt.title(f"{col}", fontsize=20,y=1.05)
  st.pyplot()


def churn_level_per_variable(df_eda):
    target_var = 'Churn'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)




