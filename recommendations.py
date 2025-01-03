import streamlit as st
import pandas as pd
import pathlib
import requests as re


def get_summary(tconst: str) -> str:
    """
    Retrieve the summary in French from tmdb

    Parameters:
    tconst: the IMDb identifier for the film
    """
    url = f"https://api.themoviedb.org/3/find/{tconst}?api_key={st.secrets["tmdb_api_key"]}&external_source=imdb_id&language=fr"
    try:
        response = re.get(url)
    except Exception:
        return "error"
    else:
        rep = response.json()
        resume = rep["movie_results"][0]["overview"]
        return resume


def get_title(tconst: str) -> str:
    """
    Retrieve the title in French from tmdb

    Parameters:
    tconst: the IMDb identifier for the film
    """
    url = f"https://api.themoviedb.org/3/find/{tconst}?api_key={st.secrets["tmdb_api_key"]}&external_source=imdb_id&language=fr"
    try:
        response = re.get(url)
    except Exception:
        return "error"
    else:
        rep = response.json()
        resume = rep["movie_results"][0]["title"]
        return resume


def retrieve_movie(tconst: str) -> None:
    link = pathlib.Path().cwd() / "datasets/df_recommandations.parquet"
    df = pd.read_parquet(link)

    movie = df.loc[df["tconst"] == tconst, :]
    col1, col2 = st.columns([0.2, 0.8])
    with col1:
        if not movie["poster_path"].empty:
            st.image(
                "https://image.tmdb.org/t/p/w1280/" + movie["poster_path"].values[0],
                width=200,
            )
        else:
            # Placeholder generated using https://placehold.co/300x400/black/red/png?text=Film&font=Lato
            st.image("assets/default-movie-image.png")
    with col2:
        title = get_title(movie["tconst"].values[0])
        st.markdown(
            f"**{title if (title != "error" and title != "") else ''}** \n {'('+movie['originalTitle'].values[0]+')' if title.lower() != movie['originalTitle'].values[0].lower() else ''}"
        )
        st.markdown(
            f"⭐ Note : {movie['averageRating'].values[0]} / 10 ({movie['numVotes'].values[0]} votes)"
        )
        summary = get_summary(movie["tconst"].values[0])
        st.markdown(
            f"__Résumé__ : {summary if (summary != "error" and summary != "") else "Pas de résumé disponible"}"
        )
        st.markdown(f"Genre : {movie['genres'].values[0]}")


def retrieve_recos(tconst: str) -> None:
    """
    Retrieve the information for the 5 recommended movies

    Parameters:
    tconst: the movie id for which the user is looking for recommandations
    """
    # Create a dataframe from the parquet file containing the recommandations obtained by machine learning
    link = pathlib.Path().cwd() / "datasets/df_recommandations.parquet"
    df = pd.read_parquet(link)
    # Retrieve the recommandations
    recommendations = df.loc[df["tconst"] == tconst, "nearest_neighbor_ids"].values[0]

    # Create a list of the recommended movies details
    results = []
    for reco_title in recommendations[1:6]:  # We limit to 5 films
        movie_info = df[df["tconst"] == reco_title].iloc[0].to_dict()
        results.append(movie_info)
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
            title = get_title(movie["tconst"])
            st.markdown(
                f"**{title if (title != "error" and title != "") else ''}**  {'('+movie['originalTitle']+')' if title.lower() != movie['originalTitle'].lower() else ''}"
            )
            st.markdown(f"⭐ Note : {movie['averageRating']} / 10")
            st.markdown(f"({movie['numVotes']} votes)")
            summary = get_summary(movie["tconst"])
            st.markdown(
                f"__Résumé__ : {summary if (summary != "error" and summary != "") else "Pas de résumé disponible"}"
            )
            st.markdown(f"Genre : {movie['genres']}")


# Page display
st.title("Mes films à voir")


link = pathlib.Path().cwd() / "datasets/df_fr_titles.parquet"
df = pd.read_parquet(link)

# User input to use for movie search
movie_options = [
    f"{title} ({year})" for title, year in zip(df["frTitle"], df["startYear"])
]

movie_selected = st.selectbox(
    label="De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?",
    options=movie_options,
    index=None,
    placeholder="Saisissez le nom du film",
)

if movie_selected:
    selected_title_split = movie_selected.split(" (")
    title = selected_title_split[0]
    year = selected_title_split[1].strip(")")
    movie_id = df.loc[
        (df["frTitle"] == title) & (df["startYear"] == year), "tconst"
    ].values[0]

    # Display info of selected movie
    retrieve_movie(movie_id)
    # Display the recommandations
    st.subheader(f"Recommandations pour {title}:")
    retrieve_recos(movie_id)
