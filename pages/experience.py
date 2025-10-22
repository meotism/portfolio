import streamlit as st
from file_helper import *

st.set_page_config(page_title="Experience", page_icon="📚", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.header("📚 Experience",divider='rainbow')
    st.write("")

    def experience_unit(title, position, company, date, location, content, web_link, appstore_link, chplay_link):
        col1, _, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(title)
        with col3:
            st.write("")
            st.markdown("###### " + date)
        col1, _, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("###### " + position + " at " + company)
        with col3:
            st.markdown("######   " + location)
        st.write(content)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.link_button("Website", web_link)
        if exp[7] != "":
            with col2:
                st.link_button("App Store", appstore_link)
        if exp[8] != "":
            with col3:
                st.link_button("Google Play", chplay_link)
        st.divider()

    for exp in Experience:
        experience_unit(exp[0],exp[1],exp[2],exp[3],exp[4],exp[5],exp[6], exp[7], exp[8])
    footer()