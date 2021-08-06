
import streamlit as st
from config import config
import pandas as pd
import matplotlib.pyplot as plt

from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance_train_test_set



def page_predict_tenure_body():
    st.write("### ML Pipeline: Predict Prospect Tenure")    

    # load tenure pipeline files
    version = 'v1'
    tenure_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/LabelsMap.pkl")
    tenure_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    tenure_labels_map = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/LabelsMap.pkl")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

 

    # show pipeline steps
    st.write("* ML pipeline to predict tenure when prospect is expected to churn")
    st.write(tenure_pipe)

    # show best features
    st.write("* The features the model was trained and its importance")
    st.image(tenure_feat_importance)



    # evaluate performance on both
    st.write("### Pipeline Performance")
    clf_performance_train_test_set(X_train,y_train,
                                X_test,y_test,
                                pipeline = tenure_pipe,
                                LabelsMap = tenure_labels_map)


#

    