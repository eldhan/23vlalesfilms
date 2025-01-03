import streamlit as st


st.title("A propos")
col1, col2 = st.columns([0.2, 0.8], vertical_alignment="center")
with col1:
    st.image(
        image="assets/team_avatar.png",
        width=300,
    )
with col2:
    st.markdown(
        "Cet outil a été codé avec passion par l'équipe des Pandas Dictateurs: Sophie, Romain, Léa, et Ely."
    )
