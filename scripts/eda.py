import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from config import PROCESSED_DATA_PATH

# Configuration du logging
logging.basicConfig(
    filename="logs/eda.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class ExploratoryDataAnalysis:
    def __init__(self):
        """Initialisation et chargement des données."""
        logging.info("Chargement des données nettoyées pour l'EDA...")
        try:
            self.events = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "events_cleaned.csv"))
            self.item_properties = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "item_properties_cleaned.csv"))
            logging.info("Données chargées avec succès.")
        except Exception as e:
            logging.error(f"Erreur lors du chargement des données : {e}")

    def check_missing_values(self):
        """Vérifier les valeurs manquantes."""
        logging.info("Vérification des valeurs manquantes...")
        print("\nValeurs manquantes avant traitement :")
        print(self.events.isnull().sum())
        print(self.item_properties.isnull().sum())

    def handle_missing_values(self):
        """Gérer les valeurs manquantes en supprimant transactionid."""
        logging.info("Nettoyage des valeurs manquantes...")
        
        # Suppression de la colonne transactionid si elle contient des NaN
        if "transactionid" in self.events.columns:
            self.events.drop(columns=["transactionid"], inplace=True)
            logging.info("Colonne transactionid supprimée (valeurs manquantes).")

        print("\nValeurs manquantes après traitement :")
        print(self.events.isnull().sum())
        print(self.item_properties.isnull().sum())

    def plot_event_distribution(self):
        """Visualiser la distribution des événements."""
        logging.info("Visualisation des événements...")
        plt.figure(figsize=(10, 5))
        sns.countplot(x="event", data=self.events, hue="event", palette="viridis", legend=False)  # Correction du warning
        plt.title("Distribution des événements")
        plt.xticks(rotation=45)
        plt.savefig("reports/event_distribution.png")
        plt.show()

    def run_eda(self):
        """Exécuter toute l'analyse exploratoire."""
        logging.info("Début de l'EDA...")
        self.check_missing_values()
        self.handle_missing_values()
        self.plot_event_distribution()
        logging.info("Fin de l'EDA.")

# Exécution du script
if __name__ == "__main__":
    eda = ExploratoryDataAnalysis()
    eda.run_eda()
