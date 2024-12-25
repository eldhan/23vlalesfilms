import streamlit as st


def menu():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.page_link("home.py", label="Accueil")
    with col2:
        st.page_link("recommendations.py", label="Recommandations")
    with col3:
        st.page_link("kpi.py", label="Indicateurs des tendances")
    with col4:
        st.page_link("about.py", label="A propos")
