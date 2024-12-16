import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd
import csv
import os

# lire le dataframe
#link = '/content/drive/MyDrive/WCS - Projet 2/database.parquet'
#df = pd.read_parquet(link)

# Nom du fichier CSV
USERS_FILE = "users.csv"


# Fonction pour vérifier si le fichier CSV existe
def ensure_csv_exists():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # En-têtes

# Fonction pour ajouter un nouvel utilisateur
def add_user(username, password):
    ensure_csv_exists()
    with open(USERS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

# Fonction pour vérifier les identifiants
def authenticate_user(username, password):
    ensure_csv_exists()
    with open(USERS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False




# Lire le fichier CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Appliquer le CSS
load_css("style.css")

# l'appli démarre sur la page d'accueil
# Initialiser l'état de la page si ce n'est pas encore fait
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

# les différentes pages de l'appli
def accueil():
    st.title("23 v'là les films !")
    st.header("Recommandations de films pour la Creuse")
    st.image("https://uploads.lebonbon.fr/source/2022/june/2032909/cin-plein-air-lille_1_2000.jpg")


def recos():
    st.title("Mes films à voir")
    film_modele = st.text_input("De quel film souhaitez-vous que nous nous inspirions pour vous proposer une sélection de films à regarder ?")


def stats():
    st.title("Les statistiques sur le cinéma")

def connect():
    st.write("Connectez-vous")


# on crée les boutons de navigation en haut
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Accueil", type="primary", use_container_width=True):
        st.session_state.page = "Accueil"

with col2:
    if st.button("Recherche", type="primary", use_container_width=True):
        st.session_state.page = "Recherche"

with col3:
    if st.button("Statistiques", type="primary", use_container_width=True):
        st.session_state.page = "Statistiques"

with col4:
    if st.button("Se connecter", type="primary", use_container_width=True):
       # if# st.button("Créer un compte"):
            #if new_password != confirm_password:
                #st.error("Les mots de passe ne correspondent pas.")
            #elif authenticate_user(new_username, new_password):
                #st.error("Ce nom d'utilisateur existe déjà.")
            #else:
                #add_user(new_username, new_password)
             #st.success("Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
        st.session_state.page = "Se connecter"


# Afficher le contenu de la page active
if st.session_state.page == "Accueil":
    accueil()
elif st.session_state.page == "Recherche":
    recos()
elif st.session_state.page == "Statistiques":
    stats()
elif st.session_state.page == "Se connecter":
    connect()