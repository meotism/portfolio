import streamlit as st
from file_helper import *

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide",initial_sidebar_state="collapsed") 

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    #sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    with st.sidebar:
        st.success("Select a page above.")
        
    #main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("About Me",divider='rainbow')

    col1, col2, col3 = st.columns([1.3 ,0.2, 1])

    with col1:
        
        st.write(info['brief'])
        st.markdown(f"###### 🇻🇳 I'm a {info['title']}")
        st.markdown(f"###### 😄 Full name: {info['fullname']}")
        st.markdown(f"###### 👉 Graduated at: {info['study']}")
        st.markdown(f"###### 📍 Location: {info['location']}")
        st.markdown(f"###### 📸 Interest: {info['interest']}")
        st.markdown(f"###### 👀 Linkedin: {linkedin_link}")
        
        # with open("assets/resume.pdf", "rb") as file:
        #     pdf_file = file.read()

        # st.download_button(
        #     label="Download my :blue[resume]",
        #     data=pdf_file,
        #     file_name="resume",
        #     mime="application/pdf")
        st.markdown("""
            <a href="https://docs.google.com/document/d/1KmfB0SgKI2zO4GEtd_9q8f5mJbwdgYlcLyGVxPhRjfs/edit?usp=sharing" 
            target="_blank" 
            rel="noopener noreferrer"
            style="text-decoration:none;">
                <button style="
                    background-color:#4CAF50; 
                    color:white; 
                    padding:10px 20px; 
                    border:none; 
                    border-radius:5px; 
                    cursor:pointer;
                    font-size:16px;
                ">
                    Open my resume
                </button>
            </a>
        """, unsafe_allow_html=True)


    with col3:
        st.image("assets/itsme.jpg", width=360)

    # skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("My :blue[skills] ⚒️",divider='rainbow') #,divider='rainbow'

    def skill_tab():
        rows,_ = len(info['skills'])//skill_col_size, skill_col_size
        skills = iter(info['skills'])
        if len(info['skills'])%skill_col_size!=0:
            rows+=1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    columns[index_].button(next(skills))
                except:
                    break
    with st.spinner(text="Loading section..."):
        skill_tab()
    footer()