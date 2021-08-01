import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_churn import PerformanceTrainTestSet
from config import config

def page3_body():
    st.write("### ML Pipeline: Predict Prospect Churn")

    
    # load files and pipelines
    churn_pipeline_dc_fe = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_data_cleaning_feat_eng.pkl")
    churn_pipeline_model = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_model.pkl")
    churn_features = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")
    churn_best_features = plt.imread("outputs/ml_pipeline/predict_churn/features_importance.png")

    # load dataset
    df = load_telco_data().filter(list(churn_features)+['Churn'] , axis=1)


    # show pipeline
    st.write(
        f"#### This is made of 2 ML Pipelines arragended in series. \n"
        f"  * That was needed since the target was imbalanced, and we used SMOTE technique")
    st.write("  * The first is responsible for data cleaning and feature engineering.")

    st.write(churn_pipeline_dc_fe)
    st.write("  * The second for feature scaling and modelling. ")
    st.write(churn_pipeline_model)
    st.write("---")

  
    
    st.write("* The features the model was trained and its importance")
    st.write(churn_features.to_list())
    st.image(churn_best_features)
    st.write("---")


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
    st.write("### Pipeline Performance")
    PerformanceTrainTestSet(X_train,y_train,
                            X_test,y_test,
                            pipeline = churn_pipeline_model,
                            LabelsMap = {0:"No Churn", 1:"Yes Churn"})


