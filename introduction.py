import streamlit as st
import base64
import pandas as pd
import numpy as np

# Set title
# st.title("About Myself")
def main():
    # st.set_page_config(layout="wide")

    menu = ["Myself","EDA","Recommend","Special Thanks"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Myself":
        st.markdown("<h1 style='text-align: center;'> About Myself </h1>", unsafe_allow_html=True)

        # Add Image
        main_bg = "bg1.jpg"
        main_bg_ext = "jpg"
        st.markdown(
            f"""
            <style>
            .reportview-container {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1,4,1])

        with col1:
            st.write("")

        with col2:
            st.image("sv.jpeg", width=420, caption="Introduction to Streamlit App")

        with col3:
            st.write("")


        st.write("Strong professional with a Bachelor of Business Administration Focused on business analytics from Panjab University."
                 " Experienced data scientist specialized in Recommendation systems, Natural language processing, Classification, and prediction problems. "
                 "Actively involved in data science projects for the past 1 year with hands-on experience in python, SQL, seaborn, scikit-learn, and streamlit.")

        st.write("I like to travel across different cities to attend business conferences and learn the latest disruptive technologies in the industry."
                 "Been a delegate at business conclaves at many prestigious B-schools across India."
                 "Member of 3 times capstone project champion team Space at Alma Better."
                 " Working on these projects helped me hone my technical skills along with soft skills such as Coordination, Decision-Making, teamwork, and management. Do connect with me if you want to chat about data science!")
    elif choice == "EDA":
        dataframe =  np.random.rand(10,20)
        st.dataframe(dataframe)
        st.text("--"*100)

        pass

if __name__ == '__main__':
    main()




