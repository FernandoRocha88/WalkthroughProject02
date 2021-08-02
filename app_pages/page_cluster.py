
import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file

def page_cluster_body():
    st.write("### ML Pipeline: Cluster Customer Base")
    st.write(
        f"* It shows ML pipeline performance cluster customer base. "
        f"It will be used to evaluate prospect profile.")    
        
        

    # load cluster pipeline files
    cluster_pipeline = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline.pkl")
    cluster_features = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline_features.pkl")
    cluster_profile = pd.read_csv("outputs/ml_pipeline/cluster_analysis/clusters_description.csv")

    # load dataset
    df = load_telco_data().filter(list(cluster_features) , axis=1)



    # aply pca to data, reduce to 3 components, plot 3D scatter colored by cluser

    # calculate and show silhouete

    # show churn levels per cluster
    # Relative Percentage (%) of Churn in each cluster

    # show cluster profile
