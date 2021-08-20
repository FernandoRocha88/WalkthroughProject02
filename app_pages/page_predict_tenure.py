
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance_train_test_set



def page_predict_tenure_body():
    st.write("### ML Pipeline: Predict Prospect Tenure")    


    st.info(
        f"* Initially we wanted to have a Regressor model to predict tenure for a likely "
        f"churnable prospect, but regressor performance was weak. We converted the target to "
        f"classes and transformed the ML task to a classification problem. \n"
        f"* We tuned this pipeline for Recall on '<4.0' class, "
        f"since we are interested in this project to detect any prospect that may churn soon. \n"
        f"* We notice that <4.0 and +20.0 classes have reasonable levels of performance, where "
        f"'4.0 to 20.0' performance is poor. This will be a limitation of our project and we "
        f"accept that a prediction on <4.0 and +20.0 will be handled as a <4.0.")
    st.write("---")

    # load tenure pipeline files
    version = 'v1'
    tenure_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/labels_map.pkl")
    tenure_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

 

    # show pipeline steps
    st.write("* ML pipeline to predict tenure when prospect is expected to churn")
    st.write(tenure_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and its importance")
    st.write(X_train.columns.to_list())
    st.image(tenure_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    clf_performance_train_test_set(X_train,y_train,
                                X_test,y_test,
                                pipeline = tenure_pipe,
                                LabelsMap = tenure_labels_map)


#

    