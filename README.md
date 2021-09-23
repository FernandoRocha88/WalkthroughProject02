## Dataset Content
The dataset is sourced from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
Each row represents a customer, each column contains customer attribute. The data set includes information about:
* Services that each customer has signed up for, like phone, multiple lines, internet, online security, online backup, device protection, tech support, streaming TV and movies
* Customer information, like how long they’ve been a customer, if they churned their contract type, payment method, paperless billing, monthly charges, and total charges
* Customer profile, like gender, if they have partners and dependents


| Variable         | Meaning                                                     | Units                                                                                |
|------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
| customerID       | Customer identification                                     | Number and Letters code that form a unique identifier to a customer                  |
| gender           | Inform customer gender                                      | Female or Male                                                                       |
| SeniorCitizen    | Inform if the customer is a senior citizen or not           | 1 for is Senior and 0 for is not Senior                                              |
| Partner          | Inform if the customer has a partner or not                 | Yes or No                                                                            |
| Dependents       | Inform if the customer has dependents or not                | Yes or No                                                                            |
| tenure           | Number of months the customer has stayed with the company   | 0 to 72                                                                              |
| PhoneService     | Inform if the customer has a phone service or not           | Yes or No                                                                            |
| MultipleLines    | Inform if  the customer has   multiple lines or not         | Yes, No, No phone service                                                            |
| InternetService  | Inform if the customer has internet service provider        | DSL, Fiber optic, No                                                                 |
| OnlineSecurity   | Inform if  the customer has online   security or not        | Yes, No, No internet service                                                         |
| OnlineBackup     | Inform if the customer has online backup or not             | Yes, No, No internet service                                                         |
| DeviceProtection | Inform if the customer has device protection or not         | Yes, No, No internet service                                                         |
| TechSupport      | Inform if the customer has tech support or not              | Yes, No, No internet service                                                         |
| StreamingTV      | Inform if the customer has streaming TV or not              | Yes, No, No internet service                                                         |
| StreamingMovies  | Inform if the customer has streaming movies or not          | Yes, No, No internet service                                                         |
| Contract         | Inform the contract term of the customer                    | Month-to-month, One year, Two year                                                   |
| PaperlessBilling | Inform if the customer has paperless billing or not         | Yes, No                                                                              |
| PaymentMethod    | Inform the customer’s payment method                        | Electronic check, Mailed check, Bank transfer (automatic), Credit card   (automatic) |
| MonthlyCharges   | Inform the amount charged to the customer monthly           | 18.3 - 119                                                                           |
| TotalCharges     | Inform the total amount charged as a customerof our company | 18.8 - 8.68k                                                                         |
| Churn            | Inform the customer churned or not                          | Yes or No                                                                            |


* **Project Terms & Jargons**
	* A customer is a person who consumes your service or product.
	* A prospect is a potential customer.
	* A churned customer is a user who has stopped using your product or service.
	* This customer, has a tenure level, which is the number of months this person has used our product/service.

## Business Requirements
As a Data Analyst from Code Institute Consulting, you are requested by Telco division to provide actionable insights and data driven recommendations to a Telecom corporation. This client has substantial customer base and is interested to manage churn levels and understand how the sales team could better interact with prospects. The data has been shared by the client

* 1 - The client is interested to understand the patterns from customer base, so the client can learn the most relevant variables that are correlated to a churned customer.
* 2 - The client is interested to tell whether or not a given prospect will churn. If so, the client is interested to know when. In addition the client is interested to know from which cluster this prospect will belong in the customer base, and based on that, present potential factors that could mantain and/or bring the prospect to a non-churnable cluster.


## Hypothesis and how to validate?
* We suspect customers are churning with low tenure levels
	* A Correlation study can help in this investigation
* A customer survey showed Fiber Optic is very appreciated by our customers
	* A Correlation study can help in this investigation


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization and Correlation study
	* We will inspect the data related to customer base
	* We will conduct a correlation study (pearson and spearman) to better understand how the variables are correlated to Churn
	* We will plot the main variables against Churn to visualize insights.


* **Business Requirement 2**:  Classification, Regression, Cluster, Data Analysis
	* We want to predict if a prospect will churn or not. We want to build a binary classifier
	* We want to predict tenure level for a prospect that is expected to churn. We want to build a regression model or, depending on the regressor performance, change the ML task to classification
	* We want to cluster similar customers, to predict from which cluster a prospect will belong to.
	* We want to understand clusters profile, so we can present potential options that could mantain or bring the prospect to a non-churnable cluster




## ML Business Case

### Predict Churn
#### Classification Model
* We want a ML model to predict if a prospect will churn or not, based on historical data from customer base, which doesn't include tenure and total charges, since these values are zero for a prospect. The target variable is categorical and contains 2-classes. We consider a **classification model**, it is a supervised model, a 2-class, single-label, classification model output: 0 (no churn), 1 (yes churn)
* Our ideal outcome is provide to our sales team a reliable insight on how to onboard customer with a higher sense of loyalty.
* The model success metrics are
	* at least 85% Recall for Churn, on train and test set (We don't want to miss a potential churner)
	* The ML model is considered a failure if:
		* after 3 months of usage, more than 30% of new onboarded custormer churn (it is an indication that the offers are not working or the model is not detecting potential churners)
		* Precision for non churn customer is lower than 80% on train and test set. (We don't want to offer free discount to many non churnable prospects)
* The model output is defined as flag, indicating if a prospect will churn or not, and the associate probability of churning. If the prospect is online, the prospect will have already provided the input data via a form. If the prospect is talking to a sales person, the sales person will conduct a interview to gather the input data and feed into the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently there is no approach to predict churn on prospect
* The training data to fit the model come from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - target: Churn ; features: all other variables, but tenure, total charges and customerID

### Predict Tenure
#### Regression Model
* We want a ML model to predict tenure levels, in months, for a prospect that is expected to churn. The target variable is a discrete number. We consider a **regression model**. It is a supervised model, and uni-dimensional regression model.
* Our ideal outcome is provide to our sales team a reliable insight on how to onboard customer with a higher sense of loyalty.
* The model success metrics are
	* At least 0.7 for R2 score , on train and test set
	* The ML model is considered a failure if:
		* after 12 months of usage, model's predictions are 50% off more than 30% of the time. Say, a prediction is >50% off if predicted 10 months and the actual value was 2 months.
* The output is defined as a continious value for tenure, in months. It is assumed that this model will predict tenure if the ChurnClf model predicts 1 (yes for churn).  If the prospect is online, the prospect will have already provided the input data via a form. If the prospect is talking to a sales person, the sales person will conduct a interview to gather the input data and feed into the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently there is no approach to predict tenure levels on prospect or customer
* The training data to fit the model come from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - filter data where Churn == 1, then drop Churn variable. Target: tenure ; features: all other variables, but total charges and customerID


### Cluster Analysis
#### Clustering Model
* We want a ML model to cluster similar customer behaviour. It is an unsupervised model.
* Our ideal outcome is provide to our sales team a reliable insight on how to onboard customer with a higher sense of loyalty.
* The model success metrics are
	* at least 0.45 for silhoute socre
	* The ML model is considered a failure if: model suggests from than 15 clusters (might become too difficult to interpret in practical terms)
* The output is defined as an additional column appended to the dataset. This column represents the clusters suggestions. It is a categorical and nominal variable, represented by numbers, starting at 0.
* Heuristics: Currently there is no approach to group similar customers
* The training data to fit the model come from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - features: all variables, but customerID, TotalCharges, Churn, and tenure 


## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary
* Quick project summary
	* Project Terms & Jargons
	* Describe Project Dataset
	* State Business Requirements

### Page 2: Customer Base Churn Study
* It will answer business requirement 1

### Page 3: Prospect Churnometer
* User Interface with prospect inputs and predictions indicating if the prospect will churn or not, if so when, to which cluster the prospect belongs and an indication on which cluster the prospect belong to.
* In addition, present cluster profile; so the person who is attending the prospect can suggest a offer that will bring the prospect to a non churnable customer

### Page 4: Project Hypothesis and Validation
* For each project hypothesis, describe the conclusion on how you validated

### Page 5: Predict Churn
* Evaluation metrics/performance on ChurnClf
  * For both train and test set: Confusion Matrix and Classification Report

### Page 6: Predict Tenure
* Evaluation metrics/performance on TenureReg
  * For both train and test set: R2, RMSE, MSE, MAE

### Page 7: Cluster Analysis
* Evaluation metrics/performance on TelcoCluster:  Silhouete score
* Clusters distribution across Churn levels
* Relative Percentage (%) of Churn in each cluster
* Cluster Profile


