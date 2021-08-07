import streamlit as st
from src.data_management import load_telco_data
from src.correlation_analysis import CalculateCorrAndPPS, DisplayCorrAndPPS

def page_customer_base_churn_body():
    st.write("### Customer Base Churn Study")
    st.write(
        f"* It answers biz requirement 1 \n\n"
        f"As a customer I am interested to understand the patterns from my customer base, "
        f"so I can better manage churn levels.")


    # load data
    df = load_telco_data()

    # Check collected data
    if st.checkbox("Check Collected Data"):
        check_data(df)
        


    # correlation and pps analysis
    if st.checkbox("Conduct Correlation and PPS Analysis on collected Data"):
        correlation_study(df)
        


    # how is churn level across tenure
    # if st.checkbox("Churn level across tenure"):
    #     import matplotlib.pyplot as plt
    #     import seaborn as sns
    #     fig, axes = plt.subplots(nrows=1, ncols=2)
    #     sns.boxplot(data=df,x='Churn', y='tenure', ax=axes[0])
    #     sns.histplot(data=df, x='tenure', hue='Churn', kde=True, ax=axes[1])
    #     st.pyplot(fig)



    # how is churn levels across main variables at clf
    if st.checkbox("Churn across main variables at clf"):
        churn_across_features(df)
        


def check_data(df):
    st.write("#### Snapshot: Collected Data")
    st.write(f"Dataset shape: {df.shape}")
    st.write(df)
    st.write("---")



def correlation_study(df):
    from feature_engine.encoding import OrdinalEncoder
    encoder = OrdinalEncoder(encoding_method='ordered', variables = df.select_dtypes(include=['object']).columns.to_list())
    df_processed = encoder.fit_transform(df, df['Churn'])
    # st.write(df_processed)

    df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df_processed)
    DisplayCorrAndPPS(
        df_corr_pearson, df_corr_spearman, pps_matrix,
        CorrThreshold=0.2, PPS_Threshold=0.2)



def churn_across_features(df):
    import matplotlib.pyplot as plt
    import plotly.express as px
    from feature_engine.encoding import OrdinalEncoder

    encoder = OrdinalEncoder(encoding_method='ordered', variables = df.select_dtypes(include=['object']).columns.to_list())
    df_processed = encoder.fit_transform(df, df['Churn'])
    fig = px.parallel_coordinates(df_processed[['Churn','Contract','tenure']], color="Churn")
    st.plotly_chart(fig)