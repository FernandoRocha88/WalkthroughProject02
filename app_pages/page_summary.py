

import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **customer** is a person who uses/pays your service or product.\n"
        f"* A **prospect** is a potential customer.\n"
        f"* A **churned** customer is a user who has stopped using your product/service.\n "
        f"* This customer, has a **tenure** level, which is the number of months this person " 
        f"has used our product/service. \n")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/README.md).")
    

    st.success(

        f"The project has 2 business requirements:\n"
        f"* 1 - Study Customer Base Churn: "
        f"Understand the patterns from my customer base, so I can better manage churn levels.\n"
        f"* 2 - Predict if a prospect will churn, if so, when? "
        f"In addition, tell from which group this prospect will belong, and based on that, "
        f"present potential factors that could mantain/bring the prospect to "
        f"a non-churnable cluster."
        )

    project_snapshot = plt.imread("pictures/requirements.png")
    st.image(project_snapshot, caption='Business Requirements 1 and 2, respectively.')

   
