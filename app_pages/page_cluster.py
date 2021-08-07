
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_telco_data, load_pkl_file

def page_cluster_body():
  st.write("### ML Pipeline: Cluster Customer Base")


  # load cluster analysis files
  version = 'v1'
  cluster_pipe = load_pkl_file(f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
  cluster_silhouette = plt.imread(f"outputs/ml_pipeline/cluster_analysis/{version}/features_importance.png")
  cluster_profile = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_description.csv")
  
  df_churn_vs_clusters = load_telco_data()[['Churn']]
  df_churn_vs_clusters['Clusters'] = cluster_pipe['model'].labels_


  st.write("#### Cluster ML Pipeline steps")
  st.write(cluster_pipe)

  st.write("#### Cluster Silhouette")
  st.image(cluster_silhouette)

  cluster_distribution_per_variable(df=df_churn_vs_clusters, target='Churn')

  st.write("#### Cluster Profile")
  statement = (
    f"We define that a cluster is churnable, when ther is **more than 30% churn**. \n"
    f"* We consider clusters 0 as churnable. "
    f"Technically, cluster 1 is almost churnable. "
    f"Clusters 2 and 3 are non-churnable. \n"
    f"* Consider the cluster profile below and the existing product offers to "
    f" suggest a plan that the prospect can move to a better or a non-churnable cluster.")
  st.write(statement)
  cluster_profile.index = [" "] * len(cluster_profile) 
  st.table(cluster_profile)






import plotly.express as px
def cluster_distribution_per_variable(df, target):


  df_bar_plot = df.value_counts(["Clusters", target]).reset_index() 
  df_bar_plot.columns = ['Clusters',target,'Count']
  df_bar_plot[target] = df_bar_plot[target].astype('object')

  st.write(f"#### Clusters distribution across {target} levels")
  fig = px.bar(df_bar_plot, x='Clusters', y='Count', color=target, width=800, height=350)
  fig.update_layout(xaxis=dict(tickmode= 'array',tickvals= df['Clusters'].unique()))
  st.plotly_chart(fig)
  # fig.show()


  df_relative = (df
                 .groupby(["Clusters", target])
                 .size()
                 .groupby(level=0)
                 .apply(lambda x:  100*x / x.sum())
                 .reset_index()
                 .sort_values(by=['Clusters'])
                 )
  df_relative.columns = ['Clusters',target,'Relative Percentage (%)']
 

  st.write(f"#### Relative Percentage (%) of {target} in each cluster")
  fig = px.line(df_relative, x='Clusters',y='Relative Percentage (%)', color=target,
                width=800, height=350)
  fig.update_layout(xaxis=dict(tickmode= 'array',tickvals= df['Clusters'].unique()))
  fig.update_traces(mode='markers+lines')
  st.plotly_chart(fig)
  # fig.show()
 
