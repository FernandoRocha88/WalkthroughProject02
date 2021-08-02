
import streamlit as st
from config import config
import pandas as pd
import matplotlib.pyplot as plt

from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance_train_test_set



def page_predict_tenure_body():
    st.write("### ML Pipeline: Predict Prospect Tenure")
    st.write(
        f"* It shows ML pipeline performance to predict prospect tenure "
        f"when it is predicted that prospect will churn")


    

    # load pipeline files
    tenure_pipe = load_pkl_file("outputs/ml_pipeline/predict_tenure/clf_pipeline.pkl")
    tenure_features = load_pkl_file("outputs/ml_pipeline/predict_tenure/X_train_columns.pkl")
    tenure_feat_importance = plt.imread("outputs/ml_pipeline/predict_tenure/features_importance.png")
    tenure_labels_map = load_pkl_file("outputs/ml_pipeline/predict_tenure/LabelsMap.pkl")

    # load dataset
    df = (
        load_telco_data()
        .query("Churn == 1")  
        .filter(tenure_features + ['tenure'] , axis=1)
        )
    st.write(df.shape,df)

    # show pipeline steps
    st.write("* ML pipeline to predict tenure when prospect is expected to churn")
    st.write(tenure_pipe)

    # show best features
    st.write("* The features the model was trained and its importance")
    st.image(tenure_feat_importance)

    # split train test set
    # split train test set
    from sklearn.model_selection import train_test_split
    X_train, X_test,y_train, y_test = train_test_split(
        df.drop(['tenure'],axis=1),
        df['tenure'],
        test_size = config.TEST_SIZE,
        random_state = config.RANDOM_STATE,
    )

    # evaluate performance on both
    st.write("### Pipeline Performance")
    st.write(tenure_pipe.predict(X_train))
    clf_performance_train_test_set(X_train,y_train,
                                X_test,y_test,
                                pipeline = tenure_pipe,
                                LabelsMap = tenure_labels_map)


#

    