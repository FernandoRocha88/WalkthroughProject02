
* AI to predict:
	- if a prospect will churn, if so, when?
	- from which group this prospect will belong, and based on that, present potential factors that could mantain/bring the customer to a non-churnable cluster
 
 <img src="https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/WalkthroughProject02%20-%20read%20me%20image.png" width="80%" height="80%"/>


## Variables Meaning


## Business Requirements
As a Data Analyst from CI AgroBusiness division, you are requested by a new Australian customer to provide actionable insights and data driven recommendations on weather information. This new customer has substantial agriculture business in Australia and understanding the rainfall level is critical for their farmer's network. Their clients needs to know precisely if it will rain in the next day, so they can plan accordingly how their routine will look like.
1 - As a customer I am interested to tell whether or not will rain in the next day in almost 50 Australian cities. In case of rain, I am interested to know the rainfall level.
2 - As a customer I am interested to cluster rainfall levels for Australian cities/regions
3 - As a customer I am interested to understand the rainfall seasonality for a given city in the last 5 years.

## Hypothesis and how to validate?
some region has more rainfall?
which region is more difficult to predict
xxxx


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
