import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file

def page2_body():
	st.write("### User Interface")
	st.write("* Page with prospect inputs and predictive analysis")

	df = load_telco_data()
	st.write(df)



	# Generte Live Data
	X_live = DrawInputsWidgets(df)

	# load churn pipleline files
	churn_pipeline_dc_fe = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_data_cleaning_feat_eng.pkl")
	churn_pipeline_model = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_model.pkl")
	churn_features = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")

	# load tenure pipeline files
	tenure_pipeline = load_pkl_file("outputs/ml_pipeline/predict_tenure/clf_pipeline.pkl")
	tenure_labels_map = load_pkl_file("outputs/ml_pipeline/predict_tenure/LabelsMap.pkl")
	tenure_features = load_pkl_file("outputs/ml_pipeline/predict_tenure/X_train_columns.pkl")
	
	# load cluster pipeline files
	cluster_pipeline = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline.pkl")
	cluster_features = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline_features.pkl")
	cluster_profile = pd.read_csv("outputs/ml_pipeline/cluster_analysis/clusters_description.csv")


	# predict on live data
	churn_prediction = predict_churn(X_live, churn_features,
									churn_pipeline_dc_fe, churn_pipeline_model)
	

	if churn_prediction == 1:
		predict_tenure(X_live, tenure_features, tenure_pipeline, tenure_labels_map)
		

	X_live_cluster = X_live.filter(cluster_features)
	cluster_prediction = cluster_pipeline.predict(X_live_cluster)
	st.write(cluster_features)
	st.write(cluster_prediction)
	
	# a trick to not display index in st.table() or st.write()
	cluster_profile.index = [" "] * len(cluster_profile) 
	st.table(cluster_profile)

    # cluster
    # get inputs
    # predict prosecpt cluster
    # show cluster profile
    # show options for each variable in the profile




def predict_churn(X_live, churn_features, churn_pipeline_dc_fe, churn_pipeline_model):

	X_live_churn = X_live.filter(churn_features)
	X_live_churn_dc_fe = churn_pipeline_dc_fe.transform(X_live_churn)
	churn_prediction = churn_pipeline_model.predict(X_live_churn_dc_fe)
	churn_prediction_proba = churn_pipeline_model.predict_proba(X_live_churn_dc_fe)

	
	st.write(churn_features)
	st.write(churn_prediction_proba)
	st.write(churn_prediction)

	# Create a logic to display the results
	churn_chance = churn_prediction_proba[churn_prediction]
	churn_map = {0:"will not", 1:"will"}
	churn_result = churn_prediction.replace(churn_map)

	statement = (
		f'* There is {churn_chance}% probability '
		f'that this prospect {churn_result} churn.')

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


def DrawInputsWidgets(df):
	import pandas as pd
	import itertools

	# The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
	tenure_features = load_pkl_file("outputs/ml_pipeline/predict_tenure/X_train_columns.pkl")
	churn_features = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")
	cluster_features = load_pkl_file("outputs/ml_pipeline/cluster_analysis/cluster_pipeline_features.pkl")
	# We combine them only with unique values
	combined_features = set(
		list(
			itertools.chain(tenure_features, churn_features, cluster_features)
			)
		)
	# st.write(combined_features)
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

