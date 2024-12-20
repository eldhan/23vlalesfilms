import streamlit as st
import pandas as pd
import pathlib
import requests as re


def get_summary():
    url = f"https://api.themoviedb.org/3/find/{tconst}?api_key={API_KEY}&external_source=imdb_id&language=fr"
    response = re.get(url)
    rep = response.json()
    resume = rep["movie_results"][0]["overview"]
    return resume


def recos():
    st.title("Mes films à voir")
    film_input = st.text_input(
        "De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?"
    )
    if film_input:
        results = search_recos(film_input)


def search_recos(film):
    # lecture du dataframe de recommandations
    link = pathlib.Path().cwd() / "dataframe_recommandation_final.parquet"
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
            for reco_title in recommendations[1:6]:  # On limite à 5 films
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
                st.image("https://image.tmdb.org/t/p/w1280/" + movie["poster_path"])
                st.markdown(f"**{movie['originalTitle']}**")
                st.markdown(
                    f"⭐ Note : {movie['averageRating']} (Nombre de votes : {movie['numVotes']})"
                )
                st.markdown(f"Résumé : {movie['overview']}")
                st.markdown(f"Genre : {movie['genres']}")

    # TODO : gérer la description en français (fetch with API)
    # TODO : gérer le cas des films sans image avec un placeholder
    # TODO : use difflib for approximation


recos()
