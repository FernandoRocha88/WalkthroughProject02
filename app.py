import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page1 import page1_body

app = MultiPage() # Create an instance of the app 



# Add all your applications (pages) here
app.add_page("Customer Churn Study", page1_body)
# app.add_page("Change Metadata", metadata.app)
# app.add_page("Machine Learning", machine_learning.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()