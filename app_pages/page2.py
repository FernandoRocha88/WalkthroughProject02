import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file

def page2_body():
	st.write("### User Interface")
	st.write("* Please insert prospect information for predictive analysis")


	# load churn pipleline files
	churn_pipeline_dc_fe = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_data_cleaning_feat_eng.pkl")
	churn_pipeline_model = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_model.pkl")
	churn_features = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")

	# load tenure pipeline files
	# tenure_pipeline = load_pkl_file("outputs/ml_pipeline/predict_tenure/clf_pipeline.pkl")
	# tenure_labels_map = load_pkl_file("outputs/ml_pipeline/predict_tenure/LabelsMap.pkl")
	tenure_features = load_pkl_file("outputs/ml_pipeline/predict_tenure/X_train_columns.pkl")
	
	# load cluster pipeline files
	cluster_pipeline = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline.pkl")
	cluster_features = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline_features.pkl")
	cluster_profile = pd.read_csv("outputs/ml_pipeline/cluster_analysis/clusters_description.csv")

	df = load_telco_data()
	# st.write(df)

	
	# Generte Live Data
	# check_variables_for_UI(tenure_features, churn_features, cluster_features)
	X_live = DrawInputsWidgets(df)


	# predict on live data
	if st.button("Run Analysis"): 
		churn_prediction = predict_churn(X_live, churn_features,
										churn_pipeline_dc_fe, churn_pipeline_model)
		

		# if churn_prediction == 1:
		# 	predict_tenure(X_live, tenure_features, tenure_pipeline, tenure_labels_map)

		predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile)
			




def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):
	X_live_cluster = X_live.filter(cluster_features)
	cluster_prediction = cluster_pipeline.predict(X_live_cluster)
	# st.write(cluster_features)
	# st.write(cluster_prediction)

	statement = (
		f"* The prospect is expected to belong to cluster {cluster_prediction[0]} \n"
		f"* This cluster is considered xxx% of time churnable, "
		f"consider the cluster profile below and the existing product offers to "
		f" suggest a plan that the prospect can move to a non-churnable cluster.")
	st.write(statement)


	# a trick to not display index in st.table() or st.write()
	cluster_profile.index = [" "] * len(cluster_profile) 
	st.table(cluster_profile)

  




def predict_churn(X_live, churn_features, churn_pipeline_dc_fe, churn_pipeline_model):

	X_live_churn = X_live.filter(churn_features)
	X_live_churn_dc_fe = churn_pipeline_dc_fe.transform(X_live_churn)
	churn_prediction = churn_pipeline_model.predict(X_live_churn_dc_fe)
	churn_prediction_proba = churn_pipeline_model.predict_proba(X_live_churn_dc_fe)

	# during the app development, it is useful to display the variables you are
	# working with. It is a type of debug, so you can be informed on what is happening
	# in the back-end.
	# st.write(churn_features)
	# st.write(churn_prediction_proba) # result is an array, we subset the value based on churn_prediction
	# st.write(churn_prediction) # result is an array and is used to set the statement msg

	# Create a logic to display the results
	churn_chance = churn_prediction_proba[0,churn_prediction][0]*100
	if churn_prediction == 1: churn_result = 'will'
	else: churn_result = 'will not'

	statement = (
		f'* There is {churn_chance.round(1)}% probability '
		f'that this prospect **{churn_result} churn**.')

	st.write(statement)
	st.write("---")
	return churn_prediction



def predict_tenure(X_live, tenure_features, tenure_pipeline, tenure_labels_map):

	X_live_tenure = X_live.filter(tenure_features)
	tenure_prediction = tenure_pipeline.predict(X_live_tenure)
	tenure_prediction_proba = tenure_pipeline.predict_proba(X_live_tenure)

	# create a logic to display the results
	statement = (
		f"* There is a % probability the prospect will stay in the following range "
		f"of months ")



	st.write(tenure_pipeline)
	st.write(tenure_prediction_proba)
	st.write(tenure_prediction)
	st.write("---")



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



def DrawInputsWidgets(df):
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

