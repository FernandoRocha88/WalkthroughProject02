import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps

def heatmap_corr(df,threshold):
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=(20,12))
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": 15}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig=fig, clear_figure=True)


def heatmap_pps(df,threshold):
    if len(df.columns) > 1:

      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=(20,12))
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                        mask=mask,cmap='rocket_r', annot_kws={"size": 15},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig=fig, clear_figure=True)
    #   plt.show()


@st.cache(suppress_st_warning=True)
def CalculateCorrAndPPS(df):
  df_corr_spearman = df.corr(method="spearman")
  df_corr_pearson = df.corr(method="pearson")

  pps_matrix_raw = pps.matrix(df)
  pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

  pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
  st.write("PPS threshold - check PPS score IQR to decide threshold for heatmap \n")
  st.write(pps_score_stats.round(3))

  return df_corr_pearson, df_corr_spearman, pps_matrix


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,CorrThreshold,PPS_Threshold):

  st.write("* Analyze how the target variable for your ML models are correlated with other variables (features and target)")
  st.write("* Analyze multi colinearity, that is, how the features are correlated among themselves")

  st.write("\n")
  st.write("*** Heatmap: Spearman Correlation ***")
  st.write("It evaluates monotonic relationship \n")
  heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold)

  print("\n")
  st.write("*** Heatmap: Pearson Correlation ***")
  st.write("It evaluates the linear relationship between two continuous variables \n")
  heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold)

  print("\n")
  print("*** Heatmap: Power Predictive Score (PPS) ***")
  print(f"PPS detects linear or non-linear relationships between two columns.\n"
        f"The score ranges from 0 (no predictive power) to 1 (perfect predictive power) \n")
  heatmap_pps(df=pps_matrix,threshold=PPS_Threshold)