
import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file

def page_cluster_body():
    st.write("### ML Pipeline: Cluster Customer Base")
        
        

    # load cluster pipeline files
    cluster_pipeline = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline.pkl")
    cluster_features = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline_features.pkl")
    cluster_profile = pd.read_csv("outputs/ml_pipeline/cluster_analysis/clusters_description.csv")

    # load dataset
    df = load_telco_data().filter(list(cluster_features) , axis=1)


    #
    st.write("* Cluster ML Pipeline steps")
    st.write(cluster_pipeline)




    st.write("* Cluster Silhouette")
    # show picture silhouete


    st.write("* Cluster Chutn Levels")
    # show churn levels per cluster
    st.write("* Relative Percentage (%) of Churn in each cluster")
    # Relative Percentage (%) of Churn in each cluster

    # show cluster profile
    statement = (
		f"* We consider clusters **0 and 1 as churnable**. "
		f"We defined that a cluster is churnable, when more than 30% has churned. \n"
        f"Technically, cluster 1 is almost churnable, but we will be conservative and "
        f"consider it as churnable. \n"
		f"* Consider the cluster profile below and the existing product offers to "
		f" suggest a plan that the prospect can move to a better or a non-churnable cluster.")
    st.write(statement)
    cluster_profile.index = [" "] * len(cluster_profile) 
    st.table(cluster_profile)
