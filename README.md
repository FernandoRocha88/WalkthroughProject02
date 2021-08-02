
* AI system to predict:
	- if a prospect will churn, if so, when?
	- from which group this prospect will belong, and based on that, present potential factors that could mantain/bring the prospect to a non-churnable cluster
 
 <img src="https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/images/WalkthroughProject02%20-%20read%20me%20image.png" width="80%" height="80%"/>




## Variables Meaning
Each row represents a customer, each column contains customer attribute
The data set includes information about:
* Services that each customer has signed up for, like phone, multiple lines, internet, online security, online backup, device protection, tech support, streaming TV and movies
* Customer information, like how long they’ve been a customer, if they churned their contract type, payment method, paperless billing, monthly charges, and total charges
* Customer profile, like gender, if they have partners and dependents


| Heading          | Meaning                                                     | Units                                                                                |
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


## Business Requirements
As a Data Analyst from Code Institute Consulting, you are requested by Telco division to provide actionable insights and data driven recommendations to a Telecom corporation. This company has substantial customer base and is interested to manage churn levels and understand how the sales team could better interact with prospects.

* 1 - As a customer I am interested to understand the patterns from my customer base, so I can better manage churn levels.
* 2 - As a customer I am interested to tell whether or not a given prospect will churn. If so, when? In addition I am interested to from which customer group/cluster this prospect will belong, and based on that, present potential factors that could mantain/bring the prospect to a non-churnable cluster


## Hypothesis and how to validate?
* sth on churn levels and tenure
* sth on predict churn, tenure


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization and Correlation study
	* We will display a DataFrame for all customer base
	* We will conduct a correlation and PPS analysis to better understand how the variable are correlated to Churn
	* We will plot...


* **Business Requirement 2**:  Classification, Regression, Cluster, Data Analysis
	* We want to predict if a prospect will churn or not. We want to build a binary classifier
	* We want to predict tenure level for a prospect that is expected to churn. We want to build a regression model or, depending on the regressor performance, switch the ML task to classification
	* We want to cluster similar customer, to predict from which cluster a prospect will belong to.
	* We want to understand clusters profile, so we can present potential options that could mantain or bring the prospect to a non-churnable cluster






## ML Business Case

### ChurnClf
* We want a ML model to predict


### TenureReg
* We want a ML model


### TelcoCluster
* We want a ML model



--

## Dashboard Design (Streamlit App User Interface)

### Page 1: Customer Base Churn Study
* Quick project summary

### Page 2: User Inteface
* User Interface with prospect inputs and predictions indicating if the prospect will churn or not, if so when, to which cluster the prospect belongs and an indication on which cluster the prospect belong to.
* In addition, present cluster profile; so the person who is attending the prospect can suggest a offer that will bring the prospect to a non churnable customer

### Page 3: Customer Base Churn Study
* answers biz requirement 1


### Page 4: Predict Churn
* Evaluation metrics/performance on ChurnClf
  * For both train and test set: Confusion Matrix and Classification Report

### Page 5: Predict Tenure
* Evaluation metrics/performance on TenureReg
  * For both train and test set: R2, RMSE, MSE, MAE

### Page 6: Cluster Analysis
* Evaluation metrics/performance on TelcoCluster
  * Silhouete score
