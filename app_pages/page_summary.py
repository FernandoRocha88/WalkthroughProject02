

import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **customer** is a person who consumes your service or product.\n"
        f"* A **prospect** is a potential customer.\n"
        f"* A **churned** customer is a user who has stopped using your product or service.\n "
        f"* This customer, has a **tenure** level, which is the number of months this person " 
        f"has used our product/service.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents a **customer base from a Telco company**, "
        f"containing individual customer data on the products and services "
        f"(like internet type, online security, online backup, tech support), "
        f"account information (like contract type, payment method, monthly charges) "
        f"and profile (like gender, partner, dependents).")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/FernandoRocha88/WalkthroughProject02/blob/main/README.md).")
    

    st.success(

        f"The project has 2 business requirements:\n"
        f"* 1 - Study Customer Base Churn: "
        f"I want to better manager customer churn levels by understanding the patterns "
        f"from my customer base.\n"
        f"* 2 - Predict if a prospect will churn, if so, when? "
        f"In addition, tell from which group this prospect will belong, and based on that, "
        f"present potential factors that could mantain/bring the prospect to "
        f"a non-churnable cluster."
        )

    project_snapshot = plt.imread("pictures/requirements.png")
    st.image(project_snapshot, caption='Representations for Business Requirements 1 and 2, respectively.')

   
