import streamlit as st
import streamlit.components.v1 as components
from file_helper import *

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Pet Projects", page_icon="💻", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.header("💻 Pet Projects",divider='rainbow')

    # page functions ----------------------------------------------------------------
    def project_component(header, content):
        st.subheader(header, divider='grey')
        st.write(content)

    # Quan Ly Chi Tieu - Expense Management
    project_component(Projects[1][0], Projects[1][1])
    st.link_button("Go to :red[Source Code]", "https://github.com/meotism/quan-ly-chi-tieu")

    # F&B Multi-channel
    project_component(Projects[2][0], Projects[2][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :green[Source Code]", "https://github.com/meotism/F-B-multi-channel")
    with col2:
        st.link_button("Go to :green[Website]", "https://meotism.github.io/F-B-multi-channel/")

    # Bomb IT 3D - Three.js Game
    project_component(Projects[3][0], Projects[3][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :blue[Source Code]", "https://github.com/meotism/Three.js")
    with col2:
        st.link_button("Go to :blue[Website]", "https://meotism.github.io/Three.js/")

    # cap cuu cuu ho
    project_component(Projects[4][0], Projects[4][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :red[Source Code]", "https://github.com/meotism/Cap-cuu-cuu-ho")
    with col2:
        st.link_button("Go to :red[Website]", "https://meotism.github.io/Cap-cuu-cuu-ho/")

    # Flashcard English
    project_component(Projects[5][0], Projects[5][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :green[Source Code]", "https://github.com/meotism/flashcard")
    with col2:
        st.link_button("Go to :green[Website]", "https://flashcard.pythonanywhere.com/")

    # Chatbot’s Phi  ----------------------------------------------------------------
    project_component(Projects[6][0], Projects[6][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :blue[Source Code]", "https://github.com/meotism/chatbot/blob/main/streamlit_app.py")
    with col2:
        st.link_button("Go to :blue[Website]","https://phi-chatbot.streamlit.app")

    # Review University ----------------------------------------------------------------
    project_component(Projects[7][0], Projects[7][1])
    st.link_button("Go to :orange[Source Code]", "https://github.com/meotism/Quality_Assessment_Review/tree/master")
    components.iframe("https://docs.google.com/presentation/d/1a14wXlSTbYt6-oknulVRM6DZLjObwIFTfY9725mR3fk/edit?usp=sharing", width=800, height=600, scrolling=True)

    # Swiftlet’s Nest Anh Xuan --------------------------------------------------------------
    project_component(Projects[8][0], Projects[8][1])
    st.video("https://www.youtube.com/watch?v=UMMOqetDDLg")

    # Video Conference meeting --------------------------------------------------------------
    project_component(Projects[9][0], Projects[9][1])
    st.link_button("Go to :red[Source Code]", "https://github.com/meotism/jitsi-meet")

    # My portfolio -----------------------------------------------------------
    project_component(Projects[10][0], Projects[10][1])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Go to :blue[Source Code]", "https://github.com/meotism/portfolio/tree/main")
    with col2:
        st.link_button("Go to :blue[Website]", "https://meotism.streamlit.app")
    footer()