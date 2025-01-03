import streamlit as st
import pandas as pd
import pathlib
import requests as re


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


def retrieve_recos(movie: str, df) -> None:
    """
    Retrieve the information for the 5 recommended movies

    Parameters:
    movie: the movie for which the user is looking for recommandations
    df: the dataframe containing all the information related to the movies
    """
    # Retrieve the recommandations
    recommendations = df.loc[
        df["originalTitle"].str.lower() == movie.lower(), "nearest_neighbor_ids"
    ].values[0]

    # Create a list of the recommended movies details
    results = []
    for reco_title in recommendations[1:6]:  # We limit to 5 films
        movie_info = df[df["tconst"] == reco_title].iloc[0].to_dict()
        results.append(movie_info)
    st.subheader(f"Recommandations pour : {movie}")
    display_recos(results)


def display_recos(results: list) -> None:
    # Create a column by movie
    cols = st.columns(len(results))

    for col, movie in zip(cols, results):
        with col:
            if movie["poster_path"]:
                st.image("https://image.tmdb.org/t/p/w1280/" + movie["poster_path"])
            else:
                # Placeholder generated using https://placehold.co/300x400/black/red/png?text=Film&font=Lato
                st.image("assets/default-movie-image.png")
            st.markdown(f"**{movie['originalTitle']}**")
            st.markdown(f"⭐ Note : {movie['averageRating']} / 10")
            st.markdown(f"({movie['numVotes']} votes)")
            summary = get_summary(movie["tconst"])
            st.markdown(
                f"Résumé : {summary if (summary != "error" and summary != "") else "Pas de résumé disponible"}"
            )
            st.markdown(f"Genre : {movie['genres']}")


# Page display
st.title("Mes films à voir")

# Create a dataframe from the parquet file containing the recommandations obtained by machine learning
link = pathlib.Path().cwd() / "dataframe_recommandation_final.parquet"
df = pd.read_parquet(link)

# User input to use for movie search

movie_options = [
    f"{title} ({year})" for title, year in zip(df["originalTitle"], df["startYear"])
]

movie_selected = st.selectbox(
    label="De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?",
    options=movie_options,
    index=None,
    placeholder="Saisissez le nom du film",
)

if movie_selected:
    selected_title_split = movie_selected.split(" (")
    original_title = selected_title_split[0]
    retrieve_recos(original_title, df)
