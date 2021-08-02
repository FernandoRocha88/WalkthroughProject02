

import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Summary")
    st.write(
        f"* A **churned** customer is a user who has stopped using your product/service. "
        f"This customer, has a **tenure** level, which is the number of months this person " 
        f"has used our product/service. \n"
        f"* We are interested to build an AI system to predict: \n"
        f"  * If a prospect will churn, if so, when? \n"
        f"  * From which group this prospect will belong, and based on that, "
        f"present potential factors that could mantain/bring the prospect to "
        f"a non-churnable cluster."
        )

    project_snapshot = plt.imread("pictures/WalkthroughProject02 - read me image.png")
    st.image(project_snapshot)

    st.write(
        f"* For additional information, please **visit and read** the "
        f"[Project README file](https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/README.md).")
    
