import streamlit as st
from src.data_management import load_telco_data, load_pkl_file

def page2_body():
	st.write("### User Interface")
	st.write("* Page with prospect inputs and predictive analysis")

	df = load_telco_data()
	st.write(df)



	# inputs
	X_live = DrawInputsWidgets(df)

######### churn
	churn_pipeline_dc_fe = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_data_cleaning_feat_eng.pkl")
	churn_pipeline_model = load_pkl_file("outputs/ml_pipeline/predict_churn/clf_pipeline_model.pkl")


	# predict
	# predict_proba


	############ tenure
	tenure_pipeline = load_pkl_file("outputs/ml_pipeline/predict_tenure/clf_pipeline.pkl")
	tenure_labels_map = load_pkl_file("outputs/ml_pipeline/predict_tenure/LabelsMap.pkl")
	# if predict == 1
	# .predict



	####


    # cluster
    # get inputs
    # predict prosecpt cluster
    # show cluster profile
    # show options for each variable in the profile



def DrawInputsWidgets(df):
	import pandas as pd

	# The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
	tenure_train_set_columns = load_pkl_file("outputs/ml_pipeline/predict_tenure/X_train_columns.pkl")
	churn_train_set_columns = load_pkl_file("outputs/ml_pipeline/predict_churn/X_train_columns.pkl")
	# We combine them only with unique values
	combined_train_set_cols = list(churn_train_set_columns)
	combined_train_set_cols.extend(x for x in tenure_train_set_columns if x not in combined_train_set_cols)
	st.write(combined_train_set_cols)

	# We know which are the most relevant features for each pipeline
	tenure_best_feature = load_pkl_file("outputs/ml_pipeline/predict_tenure/best_features.pkl")
	churn_best_features = load_pkl_file("outputs/ml_pipeline/predict_churn/best_features.pkl")
	# We combine them only with unique values
	combined_best_features = list(churn_best_features)
	combined_best_features.extend(x for x in tenure_best_feature if x not in combined_best_features)
	st.write(combined_best_features)




    # we create input widgets only for the main features
    # for other features, we will assign the mean for numerical and mode for categorical
	

	col1, col2, col3, col4 = st.beta_columns(4)
	col5, col6, col7, col8 = st.beta_columns(4)
	col9, col10, col11, col12 = st.beta_columns(4)
	percentageMin, percentageMax = 0.5, 2.0


	X_live = pd.DataFrame([],index=[0])


	with col1:
		feature = "InternetService"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget
	
	with col2:
		feature = "Contract"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col3:
		feature = "PaymentMethod"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget
	
	with col4:
		feature = "MonthlyCharges"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget


	with col5:
		feature = "Partner"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col6:
		feature = "MultipleLines"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col7:
		feature = "OnlineSecurity"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col8:
		feature = "DeviceProtection"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col9:
		feature = "StreamingTV"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	st.write(X_live)


		

	# with col5:
	# 	mean_concave_points = st.number_input(
	# 		"mean concave points",min_value=X_train["mean concave points"].min()*percentageMin,
	# 		max_value=X_train["mean concave points"].max()*percentageMax,
	# 		value=X_train["mean concave points"].median())

	# with col6:
	# 	feature= "perimeter error"
	# 	perimeter_error = st.number_input(
	# 		feature,min_value=X_train[feature].min()*percentageMin,
	# 		max_value=X_train[feature].max()*percentageMax,
	# 		value=X_train[feature].median())

	# with col7:
	# 	worst_radius = st.number_input(
	# 		"worst radius",min_value=X_train["worst radius"].min()*percentageMin,
	# 		max_value=X_train["worst radius"].max()*percentageMax,
	# 		value= 18.0) #X_train["worst radius"].median())

	# with col8:
	# 	feature="worst smoothness"
	# 	worst_smoothness = st.number_input(
	# 		feature,min_value=X_train[feature].min()*percentageMin,
	# 		max_value=X_train[feature].max()*percentageMax,
	# 		value=X_train[feature].median())

	# with col9:
	# 	feature="worst compactness"
	# 	worst_compactness = st.number_input(
	# 		feature,min_value=X_train[feature].min()*percentageMin,
	# 		max_value=X_train[feature].max()*percentageMax,
	# 		value=X_train[feature].median())
		
	# with col10:
	# 	feature="worst symmetry"
	# 	worst_symmetry = st.number_input(
	# 		feature,min_value=X_train[feature].min()*percentageMin,
	# 		max_value=X_train[feature].max()*percentageMax,
	# 		value=X_train[feature].median())

	# with col11:
	# 	worst_concavity = st.number_input(
	# 		"worst concavity",min_value=X_train["worst concavity"].min()*percentageMin,
	# 		max_value=X_train["worst concavity"].max()*percentageMax,
	# 		value=X_train["worst concavity"].median())



	# dummy_value = worst_concavity
	# # weathersit = st.slider('Weathersit',1,4,2)
	# # temp = st.number_input("Temp", min_value=0.0, max_value=1.0,value=0.5)

	# X_live = pd.DataFrame(
	# 	data={
	# 		"mean radius":mean_radius,
	# 		"mean texture":dummy_value,
	# 		"mean perimeter":mean_perimeter,
	# 		"mean area":mean_area,
	# 		"mean smoothness":dummy_value,
	# 		"mean compactness":dummy_value,
	# 		"mean concavity":mean_concavity,
	# 		"mean concave points":mean_concave_points,
	# 		"mean symmetry":dummy_value,
	# 		"mean fractal dimension":dummy_value,
	# 		"radius error":dummy_value,
	# 		"texture error":dummy_value,
	# 		"perimeter error":perimeter_error,
	# 		"area error":dummy_value,
	# 		"smoothness error":dummy_value,
	# 		"compactness error":dummy_value,
	# 		"concavity error":dummy_value,
	# 		"concave points error":dummy_value,
	# 		"symmetry error":dummy_value,
	# 		"fractal dimension error":dummy_value,
	# 		"worst radius":worst_radius,
	# 		"worst texture":dummy_value,
	# 		"worst perimeter":dummy_value,
	# 		"worst area":dummy_value,
	# 		"worst smoothness":worst_smoothness,
	# 		"worst compactness":worst_compactness,
	# 		"worst concavity":worst_concavity,
	# 		"worst concave points":dummy_value,
	# 		"worst symmetry":worst_symmetry,
	# 		"worst fractal dimension":dummy_value,
	# 	},
	# 	index=[0]
	# 	)

	# return X_live
	return "X_live"

