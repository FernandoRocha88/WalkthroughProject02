
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance_train_test_set


def page_predict_churn_body():
    st.write("### ML Pipeline: Predict Prospect Churn")

    
    st.info(
        f"* We tuned this pipeline for Recall on 'Yes Churn' class, "
        f"since we are interested in this project to not leave a potential churner behind. \n"
        f"* We also accept the fact prospects that will likely not churn may be "
        f"identified as potential churners.")
    st.write("---")

    version = 'v1'
    # load files and pipelines
    churn_pipe_dc_fe = load_pkl_file(f'outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    churn_pipe_model = load_pkl_file(f"outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_model.pkl")
    churn_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_churn/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/y_train.csv").values
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/y_test.csv").values



    # show pipeline
    st.write(
        f"#### 2 ML Pipelines arragended in series. \n"
        f"That was needed since the target was imbalanced, and we used SMOTE technique")
    st.write("  * The first is responsible for data cleaning and feature engineering.")

    st.write(churn_pipe_dc_fe)
    st.write("  * The second for feature scaling and modelling. ")
    st.write(churn_pipe_model)
    st.write("---")

  
    
    st.write("* The features the model was trained and its importance")
    st.write(X_train.columns.to_list())
    st.image(churn_feat_importance)
    st.write("---")


    # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the notebook

    # evaluate performance on train and test set
    st.write("### Pipeline Performance")
    clf_performance_train_test_set(X_train,y_train,
                                X_test,y_test,
                                pipeline = churn_pipe_model,
                                LabelsMap = {0:"No Churn", 1:"Yes Churn"})


#