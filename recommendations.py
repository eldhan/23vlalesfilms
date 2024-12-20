import streamlit as st


def recos():
    st.title("Mes films à voir")
    film_input = st.text_input(
        "De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?"
    )
    if film_input:
        search_recos(film_input)


def search_recos(film):
    # TODO : algo qui retourne les résultats
    # TODO : gérer le cas des films sans image avec un placeholder
    # TODO : use difflib for approximation
    results = [
        {
            "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/fbxQ44VRdM2PVzHSNajUseUteem.jpg",
            "title": "Harry Potter à l'école des sorciers",
            "note": "7,7",
            "nb_votes": "884k",
            "summary": "Orphelin, le jeune Harry Potter peut enfin quitter ses tyranniques oncle et tante Dursley lorsqu'un curieux messager lui révèle qu'il est un sorcier. À 11 ans, Harry va enfin pouvoir intégrer la légendaire école de sorcellerie de Poudlard, y trouver une famille digne de ce nom et des amis, développer ses dons, et préparer son glorieux avenir.",
            "genre": "Aventure, Fantastique",
        },
        {
            "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8KpHRokGpiaqEGpjYe0rpywtvUx.jpg",
            "title": "Harry Potter et la Chambre des secrets",
            "note": "7,7",
            "nb_votes": "884k",
            "summary": "Orphelin, le jeune Harry Potter peut enfin quitter ses tyranniques oncle et tante Dursley lorsqu'un curieux messager lui révèle qu'il est un sorcier. À 11 ans, Harry va enfin pouvoir intégrer la légendaire école de sorcellerie de Poudlard, y trouver une famille digne de ce nom et des amis, développer ses dons, et préparer son glorieux avenir.",
            "genre": "Aventure, Fantastique",
        },
        {
            "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/t4P2079IyK19njHDP2GwQrKdvzd.jpg",
            "title": "Harry Potter et le Prisonnier d'Azkaban",
            "note": "7,7",
            "nb_votes": "884k",
            "summary": "Orphelin, le jeune Harry Potter peut enfin quitter ses tyranniques oncle et tante Dursley lorsqu'un curieux messager lui révèle qu'il est un sorcier. À 11 ans, Harry va enfin pouvoir intégrer la légendaire école de sorcellerie de Poudlard, y trouver une famille digne de ce nom et des amis, développer ses dons, et préparer son glorieux avenir.",
            "genre": "Aventure, Fantastique",
        },
        {
            "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/hBak1pn5pbI4ycAbrgMMn1YI7P1.jpg",
            "title": "Harry Potter et la Coupe de feu",
            "note": "7,7",
            "nb_votes": "884k",
            "summary": "Orphelin, le jeune Harry Potter peut enfin quitter ses tyranniques oncle et tante Dursley lorsqu'un curieux messager lui révèle qu'il est un sorcier. À 11 ans, Harry va enfin pouvoir intégrer la légendaire école de sorcellerie de Poudlard, y trouver une famille digne de ce nom et des amis, développer ses dons, et préparer son glorieux avenir.",
            "genre": "Aventure, Fantastique",
        },
        {
            "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/9ZfpCVNx0y8jpColnnfdA1HI4Zb.jpg",
            "title": "Harry Potter et l'Ordre du Phénix",
            "note": "7,7",
            "nb_votes": "884k",
            "summary": "Orphelin, le jeune Harry Potter peut enfin quitter ses tyranniques oncle et tante Dursley lorsqu'un curieux messager lui révèle qu'il est un sorcier. À 11 ans, Harry va enfin pouvoir intégrer la légendaire école de sorcellerie de Poudlard, y trouver une famille digne de ce nom et des amis, développer ses dons, et préparer son glorieux avenir.",
            "genre": "Aventure, Fantastique",
        },
    ]
    container = st.container(height=None, key="reco")
    with container:
        col1, col2, col3, col4, col5 = st.columns(5)
        columns_list = [col1, col2, col3, col4, col5]
        for i in range(5):
            with columns_list[i]:
                st.image(results[i]["image"])
                st.markdown(results[i]["title"])
                st.markdown(results[i]["note"] + "-" + results[i]["nb_votes"])
                st.markdown(results[i]["summary"])
                st.markdown(results[i]["genre"])


recos()
