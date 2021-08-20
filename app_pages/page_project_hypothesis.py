import streamlit as st

def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")


    st.success(
        f"* We suspect customers are churning with low tenure levels: Correct, "
        f"the correlation study at Churned Customer Study supports that. \n\n"
        f"* A customer survey showed Fiber Optic is very appreciated by our customers: "
        f"a churned user typically has Fiber Optic at Churned Customer Study. " 
        f"The insight will be taken to the survey team for further discussions and investigations."
    )
        