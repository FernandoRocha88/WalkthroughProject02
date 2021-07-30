import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_churn import PerformanceTrainTestSet
from config import config

def page3_body():
    st.write("### ML Pipeline: Predict Prospect Churn")

    
    # load 2 pipelines
    churn_pipeline_dc_fe = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_data_cleaning_feat_eng.pkl")
    churn_pipeline_model = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_model.pkl")
    churn_features = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")

    # load dataset
    df = load_telco_data().filter(list(churn_features)+['Churn'] , axis=1)
  

    # show best features
    st.write("* The pipeline was trained on the feaures below:")
    st.write(list(churn_features))

    # split train test set
    from sklearn.model_selection import train_test_split
    X_train, X_test,y_train, y_test = train_test_split(
        df.drop(['Churn'],axis=1),
        df['Churn'],
        test_size = config.TEST_SIZE,
        random_state = config.RANDOM_STATE,
    )

    # apply dc_fe pipeline (data cleaninig and feature engineering)
    X_train = churn_pipeline_dc_fe.transform(X_train)
    X_test = churn_pipeline_dc_fe.transform(X_test)


    # evaluate performance on train and test set
    PerformanceTrainTestSet(X_train,y_train,
                            X_test,y_test,
                            pipeline = churn_pipeline_model,
                            LabelsMap = {0:"No Churn", 1:"Yes Churn"})


