import pandas as pd
import os
from config import PROCESSED_DATA_PATH

def load_data():
    """Charge les fichiers de données nettoyés."""
    events_path = os.path.join(PROCESSED_DATA_PATH, "events_cleaned.csv")
    item_properties_path = os.path.join(PROCESSED_DATA_PATH, "item_properties_cleaned.csv")

    if not os.path.exists(events_path):
        raise FileNotFoundError(f"❌ ERREUR: Le fichier {events_path} est introuvable !")

    if not os.path.exists(item_properties_path):
        raise FileNotFoundError(f"❌ ERREUR: Le fichier {item_properties_path} est introuvable !")

    # Charger les données
    events = pd.read_csv(events_path)
    item_properties = pd.read_csv(item_properties_path)

    # Afficher les premières lignes et les colonnes pour inspecter le fichier
    print("Premières lignes du fichier events_cleaned.csv :")
    print(events.head())  # Affiche les 5 premières lignes
    print("Colonnes du fichier events_cleaned.csv :")
    print(events.columns)  # Affiche les noms des colonnes

    return events, item_properties
