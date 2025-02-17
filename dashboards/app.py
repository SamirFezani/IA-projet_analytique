import streamlit as st
from utils import load_data
from components.plots import event_distribution
from components.tableau_embed import tableau_dashboard

# Charger les données
events, item_properties = load_data()

# Interface utilisateur Streamlit
st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

st.title("📊 Dashboard - Analyse E-commerce")

# Menu latéral
menu = st.sidebar.radio("Navigation", ["Vue générale", "Tableau Public"])

if menu == "Vue générale":
    event_distribution(events)  # Appel de la fonction qui affiche la distribution

elif menu == "Tableau Public":
    tableau_dashboard()  # Affichage du tableau de bord intégré
