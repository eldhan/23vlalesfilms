import streamlit as st


def about():
    st.title("A propos")
    st.image(
        image="assets/team_avatar.png",
        width=300,
    )
    st.markdown(
        "Cet outil a été codé avec passion par l'équipe des Pandas Dictateurs: Sophie, Romain, Léa, et Ely."
    )


def stats():
    st.title("Les statistiques sur le cinéma")


about()
