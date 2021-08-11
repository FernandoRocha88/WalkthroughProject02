import streamlit as st

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
		f'### There is {churn_chance.round(1)}% probability '
		f'that this prospect **{churn_result} churn**.')


	st.write(statement)
	return churn_prediction





def predict_tenure(X_live, tenure_features, tenure_pipeline, tenure_labels_map):

	X_live_tenure = X_live.filter(tenure_features)
	tenure_prediction = tenure_pipeline.predict(X_live_tenure)
	tenure_prediction_proba = tenure_pipeline.predict_proba(X_live_tenure)


	proba = tenure_prediction_proba[0,tenure_prediction][0]*100
	tenure_levels = tenure_labels_map[tenure_prediction[0]]

	# create a logic to display the results
	statement = (
		f"* In addition, there is a {proba.round(2)}% probability the prospect "
		f"will stay **{tenure_levels} months**. ")

	st.write(statement)



def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):
	X_live_cluster = X_live.filter(cluster_features)
	cluster_prediction = cluster_pipeline.predict(X_live_cluster)
	# st.write(cluster_features)
	# st.write(cluster_prediction)


	statement = (
		f"### The prospect is expected to belong to **cluster {cluster_prediction[0]}** \n"
		f" We consider **cluster 1 as churnable** and **cluster 3 as almost churnable**. "
		f" We consider **clusters 0 and 2 as non-churnable** \n"
		f"* Consider the cluster profile below and the existing product offers to "
		f" suggest a plan that the prospect can move to a better or a non-churnable cluster.")
	st.write("---")
	st.write(statement)


	# a trick to not display index in st.table() or st.write()
	cluster_profile.index = [" "] * len(cluster_profile) 
	st.table(cluster_profile)

