import streamlit as st


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

# Define the navigation
pg = st.navigation([home, recos, about])
# Apply css
load_css("style.css")
# Start the app
pg.run()
