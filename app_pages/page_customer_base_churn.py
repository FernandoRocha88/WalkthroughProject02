import streamlit as st
from src.data_management import load_telco_data

def page_customer_base_churn_body():
    st.write("### Customer Base Churn Study")
    st.write(
        f"* As a customer I am interested to understand the patterns from my customer base, "
        f"so I can better manage churn levels.")


    # load data
    df = load_telco_data()

    # hard copied from data visualization notebook
    vars_to_study = ['Contract', 'InternetService', 'OnlineSecurity', 'TechSupport', 'tenure']

    # inspect collected data
    if st.checkbox("Inspect Customer Base"):
        inspect_data(df)
    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* A churned customern typically has a month to month contract \n"
        f"* A churned customer typically has fiber optic. \n"
        f"* A churned customer typically doesn't have tech support. \n"
        f"* A churned customer doesn't have online security. \n"
        f"* A churned customer typically has low tenure levels. \n"
        f"The insights above will be used as reference additional investigations. "
        f"Like: why high churn levels in fiber optic? "
        f"But for the present project, it answers business requeriment 1."
    )



    st.success(
        f"Find below how the insights can be used when predicting prospect that might churn\n\n"
        f"* If a prospect looks to be churnable, and is not showing openness to our offers, "
        f"we will concede free tech support and online security for 18 months. \n"
        f"* We will offer 15% discount for a year when the prospect switch from "
        f"month to month to year plan. \n"
        f"* We will give 5% discount when the prospect switch to an automated payment method.")

    df_eda = df.filter(vars_to_study + ['Churn'])
    # Individual plots per variable
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.checkbox("Churn Levels per Variable"):
        churn_level_per_variable(df_eda)
        
    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a churned customer")
        parallel_plot_churn(df_eda)

    st.write("---")
    if st.checkbox("Project Hypothesis and Validation"):
        project_hypothesis()
        

def project_hypothesis():
    st.success(
        f"* We suspect customers are churning with low tenure levels: Correct, "
        f"the correlation study supports that. \n"
        f"* A customer survey showed Fiber Optic is very appreciated by our customers: "
        f"a churned user typically has Fiber Optic. The insight will be taken to the "
        f"survey team for further discussions and investigations."
    )
        


def inspect_data(df):
    st.write(
        f"For dataset explanation, visit project "
        f"[repo](https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/README.md)")
    st.write(f"Dataset shape: {df.shape}")
    st.write(df)
    


import matplotlib.pyplot as plt
import seaborn as sns
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,order = df[col].value_counts().index)
    plt.xticks(rotation=90) 
    plt.title(f"{col}", fontsize=20,y=1.05)        
    st.pyplot(fig)

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True,element="step") 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig)


def churn_level_per_variable(df_eda):
    target_var = 'Churn'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)



def parallel_plot_churn(df_eda):
    from feature_engine.discretisation import ArbitraryDiscretiser
    import numpy as np
    import plotly.express as px

    tenure_map = [-np.Inf, 6, 12, 18, 24, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'tenure': tenure_map})
    df_parallel = disc.fit_transform(df_eda)
    
    n_classes = len(tenure_map) - 1
    classes_ranges = disc.binner_dict_['tenure'][1:-1]

    LabelsMap = {}
    for n in range(0,n_classes):
        if n == 0: LabelsMap[n] = f"<{classes_ranges[0]}"
        elif n == n_classes-1: LabelsMap[n] = f"+{classes_ranges[-1]}"
        else: LabelsMap[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"


    df_parallel['tenure'] = df_parallel['tenure'].replace(LabelsMap)
    fig = px.parallel_categories(df_parallel, color="Churn", width=750, height=500)
    st.plotly_chart(fig)


