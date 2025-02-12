from scripts.download_data import DataLoader
from scripts.preprocessing import DataProcessing

def main():
    print("Début du processus de traitement des données...")

    # Étape 1 : Télécharger les données
    loader = DataLoader()
    loader.download_data()

    # Étape 2 : Prétraiter les données
    processor = DataProcessing()
    processor.load_data()
    processor.preprocess_data()
    processor.save_data()

    print("Processus terminé.")

if __name__ == "__main__":
    main()
