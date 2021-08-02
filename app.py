import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_ui import page_ui_body
from app_pages.page_customer_base_churn import page_customer_base_churn_body
from app_pages.page_predict_churn import page_predict_churn_body
from app_pages.page_predict_tenure import page_predict_tenure_body
from app_pages.page_cluster import page_cluster_body

# Create an instance of the app 
app = MultiPage() 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("User Interface", page_ui_body)
app.add_page("Customer Churn Study", page_customer_base_churn_body)
app.add_page("ML: Prospect Churn", page_predict_churn_body)
app.add_page("ML: Prospect Tenure", page_predict_tenure_body)
app.add_page("ML: Cluster Base", page_cluster_body)

# Run the  app
app.run()