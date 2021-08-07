
import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
														predict_churn, 
														predict_tenure, 
														predict_cluster)

def page_ui_body():
	st.write("### User Interface")
	st.write("* Please insert prospect information for predictive analysis")

	
	# load churn pipleline files
	version = 'v1'
	churn_pipe_dc_fe = load_pkl_file(f'outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
	churn_pipe_model = load_pkl_file(f"outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_model.pkl")
	churn_features = (pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_train.csv")
					.columns
					.to_list()
					)


	# load tenure pipeline files
	version = 'v1'
	tenure_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
	tenure_labels_map = load_pkl_file(f"outputs/ml_pipeline/predict_tenure/{version}/LabelsMap.pkl")
	tenure_features = (pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
					.columns
					.to_list()
					)
	
	# load cluster pipeline files
	version = 'v1'
	cluster_pipe = load_pkl_file(f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
	cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
						.columns
						.to_list()
						)
	cluster_profile = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_description.csv")



	
	# Generte Live Data
	# check_variables_for_UI(tenure_features, churn_features, cluster_features)
	X_live = DrawInputsWidgets()


	# predict on live data
	if st.button("Run Analysis"): 
		churn_prediction = predict_churn(X_live, churn_features,
										churn_pipe_dc_fe, churn_pipe_model)
		
		if churn_prediction == 1:
			predict_tenure(X_live, tenure_features, tenure_pipe, tenure_labels_map)

		predict_cluster(X_live, cluster_features, cluster_pipe, cluster_profile)
			



def check_variables_for_UI(tenure_features, churn_features, cluster_features):
	import itertools

	# The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
	# We combine them only with unique values
	combined_features = set(
		list(
			itertools.chain(tenure_features, churn_features, cluster_features)
			)
		)
	st.write(f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")



def DrawInputsWidgets():

	# load dataset
	df = load_telco_data()
	# st.write(df)


    # we create input widgets only for 12 features
	col1, col2, col3, col4 = st.beta_columns(4)
	col5, col6, col7, col8 = st.beta_columns(4)
	col9, col10, col11, col12 = st.beta_columns(4)
	percentageMin, percentageMax = 0.5, 2.0


	X_live = pd.DataFrame([],index=[0])


	with col1:
		feature = "StreamingTV"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget
	
	with col2:
		feature = "MonthlyCharges"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget


	with col3:
		feature = "Contract"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col4:
		feature = "Partner"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget
	
	with col5:
		feature = "TechSupport"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col6:
		feature = "InternetService"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col7:
		feature = "OnlineBackup"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col8:
		feature = "OnlineSecurity"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col9:
		feature = "DeviceProtection"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col10:
		feature = "MultipleLines"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col11:
		feature = "PaymentMethod"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col12:
		feature = "StreamingMovies"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget


	return X_live
