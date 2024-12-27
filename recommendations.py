import streamlit as st
import pandas as pd
import pathlib
import requests as re
from difflib import get_close_matches


def get_summary(tconst):
    url = f"https://api.themoviedb.org/3/find/{tconst}?api_key={st.secrets["tmdb_api_key"]}&external_source=imdb_id&language=fr"
    try:
        response = re.get(url)
    except Exception:
        return "error"
    else:
        rep = response.json()
        resume = rep["movie_results"][0]["overview"]
        return resume


def recos():
    st.title("Mes films à voir")
    film_input = st.text_input(
        "De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?"
    )
    if film_input:
        search_recos(film_input)


def search_recos(film):
    # lecture du dataframe de recommandations
    link = pathlib.Path().cwd() / "dataframe_recommandation_final.parquet"
    df = pd.read_parquet(link)
    # Recherche du film correspondant
    best_matches = get_close_matches(
        film.lower(), df["originalTitle"].str.lower().values, n=3, cutoff=0.8
    )
    if best_matches:
        # si le premier résultat approchant correspond exactement au film recherché
        if best_matches[0].lower() == film.lower():
            # Récupérer les informations des 5 films recommandés
            recommendations = df.loc[
                df["originalTitle"].str.lower() == film.lower(), "nearest_neighbor_ids"
            ].values[0]

            # Créer une liste des données des films recommandés
            results = []
            for reco_title in recommendations[1:6]:  # On limite à 5 films
                movie_info = df[df["tconst"] == reco_title].iloc[0].to_dict()
                results.append(movie_info)
            st.subheader(f"Recommandations pour : {film}")
            show_recos(results)
        elif best_matches:
            st.write("Vouliez-vous dire : ")
            for match in best_matches:
                clicked_button = st.button(label=match)
            if clicked_button:
                search_recos(match)
    else:
        st.error("Film non trouvé dans la base de données.")


def show_recos(results):
    # TODO : afficher le nom du film en français
    cols = st.columns(len(results))  # Créer une colonne par film

    for col, movie in zip(cols, results):
        with col:
            if movie["poster_path"]:
                st.image("https://image.tmdb.org/t/p/w1280/" + movie["poster_path"])
            else:
                # Placeholder generated using https://placehold.co/300x400/black/red/png?text=Film&font=Lato
                st.image("assets/default-movie-image.png")
            st.markdown(f"**{movie['originalTitle']}**")
            st.markdown(
                f"⭐ Note : {movie['averageRating']} (Nombre de votes : {movie['numVotes']})"
            )
            summary = get_summary(movie["tconst"])
            st.markdown(
                f"Résumé : {[summary if summary != "error" else movie['overview']]}"
            )
            st.markdown(f"Genre : {movie['genres']}")


recos()
