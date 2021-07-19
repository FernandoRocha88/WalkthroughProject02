
* AI system to predict:
	- if a prospect will churn, if so, when?
	- from which group this prospect will belong, and based on that, present potential factors that could mantain/bring the customer to a non-churnable cluster
 
 <img src="https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/WalkthroughProject02%20-%20read%20me%20image.png" width="80%" height="80%"/>


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
As a Data Analyst from Code Institute Consulting, you are requested by Telco division to provide actionable insights and data driven recommendations a customer. This new customer has substantial agriculture business in Australia and understanding the rainfall level is critical for their farmer's network. Their clients needs to know precisely if it will rain in the next day, so they can plan accordingly how their routine will look like.
1- As a customer I am interested to understand the patterns from my customer base, so I can better manage churn levels.
2 - As a customer I am interested to tell whether or not a given prospect will churn. If so, when? In addition I am interested to from which customer group/cluster this prospect will belong, and based on that, present potential factors that could mantain/bring the prospect to a non-churnable cluster


## Hypothesis and how to validate?
* sth on churn levels and tenure
* sth on predict churn, but not tenure


## Rationale to map the business requirements to the Data Visualizations and ML tasks
Business Requirement 1: Classification and Regression

We build a Classifier (WeatherClf) to predict RainTomorro



## ML Business Case
WeatherClf
We want a ML model to predict if it will rain tomorrow. It is a supervised model, a 2-class, single-label, classification model: 0 (no), 1 (yes)
Our ideal outcome is provide to our farmer's network a reliable insight if it will rain or not tomorrow, so they can plan their immediate demand.



--

## Dashboard Design
Streamlit App User Interface
Page 1: Rainfall prediction
User Interface with inputs (city an
