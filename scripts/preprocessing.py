import pandas as pd
import os
import logging
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

# 🔹 Configuration du logging
logging.basicConfig(
    filename="logs/preprocessing.log",  # Enregistre les logs dans un fichier
    level=logging.INFO,  # Niveau INFO (enregistre aussi WARNING et ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format des logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format de la date
)

class DataProcessing:
    def __init__(self):
        """Initialisation du traitement des données."""
        self.raw_path = RAW_DATA_PATH
        self.processed_path = PROCESSED_DATA_PATH
        os.makedirs(self.processed_path, exist_ok=True)

    def load_data(self):
        """Charge les fichiers CSV avec gestion des erreurs."""
        logging.info("📥 Chargement des fichiers CSV...")
        try:
            self.category_tree = pd.read_csv(os.path.join(self.raw_path, "category_tree.csv"))
            self.events = pd.read_csv(os.path.join(self.raw_path, "events.csv"))
            self.item_properties_1 = pd.read_csv(os.path.join(self.raw_path, "item_properties_part1.csv"))
            self.item_properties_2 = pd.read_csv(os.path.join(self.raw_path, "item_properties_part2.csv"))
            logging.info("✅ Données chargées avec succès.")
        except Exception as e:
            logging.error(f"❌ Erreur lors du chargement des fichiers : {e}")

    def preprocess_data(self):
        """Nettoyage et preprocessing des données."""
        logging.info("🛠 Début du nettoyage et preprocessing...")
        try:
            # 🔹 Suppression des doublons dans events
            initial_rows = len(self.events)
            self.events.drop_duplicates(inplace=True)
            logging.info(f"✅ Suppression des doublons : {initial_rows - len(self.events)} supprimés.")

            # 🔹 Fusion des fichiers item_properties
            self.item_properties = pd.concat([self.item_properties_1, self.item_properties_2])
            logging.info("✅ Fusion des fichiers item_properties réussie.")

            # 🔹 Sauvegarde des fichiers nettoyés
            self.events.to_csv(os.path.join(self.processed_path, "events_cleaned.csv"), index=False)
            self.item_properties.to_csv(os.path.join(self.processed_path, "item_properties_cleaned.csv"), index=False)
            logging.info("✅ Fichiers nettoyés et sauvegardés avec succès.")

        except Exception as e:
            logging.error(f"❌ Erreur dans le preprocessing : {e}")

# 🔹 Lancer le script si exécuté directement
if __name__ == "__main__":
    processor = DataProcessing()
    processor.load_data()
    processor.preprocess_data()
    logging.info("🎉 Fin du script preprocessing.")
