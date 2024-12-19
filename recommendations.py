import streamlit as st


def recos():
    st.title("Mes films à voir")
    film_input = st.text_input(
        "De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?"
    )
    if film_input:
        results = search_recos(film_input)


def search_recos(film):
    # TODO : algo qui retourne les résultats
    # TODO : gérer le cas des films sans image avec un placeholder
    # TODO : use difflib for approximation
    results = [
        {'image':'', 'title':'', 'note':'','nb_votes':'','summary':''},
        {'image':'', 'title':'', 'note':'','nb_votes':'','summary':''},
        {'image':'', 'title':'', 'note':'','nb_votes':'','summary':''},
        {'image':'', 'title':'', 'note':'','nb_votes':'','summary':''},
        {'image':'', 'title':'', 'note':'','nb_votes':'','summary':''}
    ]


recos()
