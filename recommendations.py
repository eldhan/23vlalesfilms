import streamlit as st
import pandas as pd
import pathlib


def recos():
    st.title("Mes films à voir")
    film_input = st.text_input(
        "De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?"
    )
    if film_input:
        results = search_recos(film_input)


def search_recos(film):
    # lecture du dataframe de recommandations
    link = (
        pathlib.Path().cwd()
        / "Documents"
        / "23vlalesfilms"
        / "dataframe_recommandation_final.parquet"
    )
    df = pd.read_parquet(link)

    if film:
        # Recherche du film correspondant
        if film in df["originalTitle"].values:
            # Récupérer les informations des 5 films recommandés
            recommendations = df.loc[
                df["originalTitle"] == film, "nearest_neighbor_ids"
            ].values[0]

            # Créer une liste des données des films recommandés
            results = []
            for reco_title in recommendations[:5]:  # On limite à 5 films
                movie_info = df[df["tconst"] == reco_title].iloc[0].to_dict()
                results.append(movie_info)
    else:
        st.error("Film non trouvé dans la base de données.")
        results = []

    # Étape 2 : Afficher les films dans des colonnes
    if results:
        st.subheader(f"Recommandations pour : {film}")
        cols = st.columns(len(results))  # Créer une colonne par film

        for col, movie in zip(cols, results):
            with col:
                # st.image(movie["poster_path"], use_column_width=True)
                st.markdown(f"**{movie['originalTitle']}**")
                st.markdown(
                    f"⭐ Note : {movie['averageRating']} (Nombre de votes : {movie['numVotes']})"
                )
                st.markdown(f"Résumé : {movie['overview']}")
                st.markdown(f"Genre : {movie['genres']}")

    # TODO : gérer le fetch des images avec l'API
    # TODO : gérer la description en français (fetch with API)
    # TODO : gérer le cas des films sans image avec un placeholder
    # TODO : use difflib for approximation


recos()
