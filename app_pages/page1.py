import streamlit as st
from src.data_management import load_telco_data
from src.correlation_analysis import CalculateCorrAndPPS, DisplayCorrAndPPS

def page1_body():
    st.write("### Customer Base Churn Study")
    st.write(
        f"* It answers biz requirement 1 \n\n"
        f"As a customer I am interested to understand the patterns from my customer base, "
        f"so I can better manage churn levels.")


    # load data
    df = load_telco_data()

    # Check collected data
    if st.checkbox("Check Collected Data"):
        st.write("#### Snapshot: Collected Data")
        st.write(f"Dataset shape: {df.shape}")
        st.write(df)
        st.write("---")


    # correlation and pps analysis
    if st.checkbox("Conduct Correlation and PPS Analysis on collected Data"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        DisplayCorrAndPPS(
            df_corr_pearson, df_corr_spearman, pps_matrix,
            CorrThreshold=0.4, PPS_Threshold=0.2)


    # how is churn level across tenure
    if st.checkbox("Churn level across tenure"):
        import matplotlib.pyplot as plt
        import seaborn as sns
        fig, axes = plt.subplots(nrows=1, ncols=2)
        sns.boxplot(data=df,x='Churn', y='tenure', ax=axes[0])
        sns.histplot(data=df, x='tenure', hue='Churn', kde=True, ax=axes[1])
        st.pyplot(fig)



    # how is churn levels across main variables at clf
    if st.checkbox("Churn across main variables at clf"):
        import matplotlib.pyplot as plt
        import plotly.express as px
        
        fig = px.parallel_coordinates(df[['Churn','MonthlyCharges','tenure',]], color="Churn")
        st.pyplot(fig)

