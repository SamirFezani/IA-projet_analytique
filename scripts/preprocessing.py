import pandas as pd
import os
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

class DataProcessing:
    def __init__(self):
        """Initialisation du traitement des données."""
        self.raw_path = RAW_DATA_PATH
        self.processed_path = PROCESSED_DATA_PATH
        os.makedirs(self.processed_path, exist_ok=True)

    def load_data(self):
        """Charge les fichiers CSV."""
        print("📂 Chargement des fichiers...")
        self.category_tree = pd.read_csv(os.path.join(self.raw_path, "category_tree.csv"))
        self.events = pd.read_csv(os.path.join(self.raw_path, "events.csv"))
        self.item_properties_1 = pd.read_csv(os.path.join(self.raw_path, "item_properties_part1.csv"))
        self.item_properties_2 = pd.read_csv(os.path.join(self.raw_path, "item_properties_part2.csv"))
        print("✅ Données chargées.")

    def preprocess_data(self):
        """Nettoyage et preprocessing."""
        print("🧹 Nettoyage des fichiers...")

        # Suppression des doublons dans events
        self.events.drop_duplicates(inplace=True)

        # Fusion des fichiers item_properties
        self.item_properties = pd.concat([self.item_properties_1, self.item_properties_2])

        print("✅ Prétraitement terminé.")

    def save_data(self):
        """Sauvegarde des fichiers nettoyés."""
        self.events.to_csv(os.path.join(self.processed_path, "events_cleaned.csv"), index=False)
        self.item_properties.to_csv(os.path.join(self.processed_path, "item_properties_cleaned.csv"), index=False)
        print("✅ Données nettoyées et enregistrées.")

if __name__ == "__main__":
    processor = DataProcessing()
    processor.load_data()
    processor.preprocess_data()
    processor.save_data()
