import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page1 import page1_body
from app_pages.page2 import page2_body
from app_pages.page3 import page3_body
from app_pages.page4 import page4_body
from app_pages.page5 import page5_body

app = MultiPage() # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Customer Churn Study", page1_body)
app.add_page("User Interface", page2_body)
app.add_page("ML: Prospect Churn", page3_body)
app.add_page("ML: Prospect Tenure", page4_body)
app.add_page("ML: Cluster Base", page5_body)

# Run the  app
app.run()