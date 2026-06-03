import streamlit as st
from file_helper import *

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Certifications", page_icon="🏆", layout="wide", initial_sidebar_state="collapsed")
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.header("🏆 Certifications", divider='rainbow')
    st.write("")

    # page functions ----------------------------------------------------------------
    def cert_unit(name, issuer, date, verify_link, extra):
        col1, _, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(name)
        with col3:
            st.write("")
            st.markdown("###### " + date)
        st.markdown("###### Issued by " + issuer)
        if extra:
            st.write(extra)
        if verify_link:
            st.link_button("Show credential", verify_link)
        st.divider()

    for cert in Certifications:
        cert_unit(cert[0], cert[1], cert[2], cert[3], cert[4])
    footer()
