import streamlit as st
import pathlib
from menu import menu


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Define the pages
home = st.Page(
    page="home.py", title="Accueil", default=True, icon=":material/theaters:"
)
recos = st.Page(
    page="recommendations.py",
    title="Recommandations",
    url_path="recos",
    default=False,
    icon=":material/theaters:",
)
about = st.Page(
    page="about.py",
    title="A propos",
    url_path="about",
    default=False,
    icon=":material/theaters:",
)

kpi = st.Page(
    page="kpi.py",
    title="Indicateurs des tendances",
    url_path="kpi",
    default=False,
    icon=":material/theaters:",
)

# Define the navigation
st.set_page_config(layout="wide")
pg = st.navigation([home, recos, kpi, about], position="hidden")
menu()
# Apply css
css = pathlib.Path().cwd() / "style.css"
load_css(css)
# Start the app
pg.run()
