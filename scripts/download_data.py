import os
import kaggle
import zipfile

# Définition des variables
DATASET_NAME = "retailrocket/ecommerce-dataset"
DATA_PATH = "data"
ZIP_FILE = os.path.join(DATA_PATH, "ecommerce-dataset.zip")

def setup_kaggle_api():
    """
    Vérifie si le fichier kaggle.json est bien configuré.
    """
    kaggle_config_path = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_config_path):
        raise FileNotFoundError(
            "❌ Le fichier kaggle.json est introuvable !\n"
            "Télécharge-le depuis ton compte Kaggle et place-le dans ~/.kaggle/ ou %USERPROFILE%/.kaggle/"
        )

def download_dataset():
    """
    Télécharge et extrait le dataset depuis Kaggle.
    """
    try:
        # Vérification de l'API Kaggle
        setup_kaggle_api()
        
        # Création du dossier 'data' s'il n'existe pas
        os.makedirs(DATA_PATH, exist_ok=True)

        # Vérifier si le fichier existe déjà
        if os.path.exists(ZIP_FILE) or any(os.scandir(DATA_PATH)):
            print("✅ Les données sont déjà présentes, aucun téléchargement nécessaire.")
            return

        # Téléchargement des fichiers
        print(f"📥 Téléchargement du dataset {DATASET_NAME}...")
        kaggle.api.dataset_download_files(DATASET_NAME, path=DATA_PATH, unzip=False)
        print(f"✅ Dataset téléchargé dans '{DATA_PATH}'.")
        
        # Vérifier si le fichier ZIP existe
        if os.path.exists(ZIP_FILE):
            print("📦 Extraction des fichiers...")
            with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
                zip_ref.extractall(DATA_PATH)
            print("✅ Extraction terminée.")

            # Supprimer le fichier ZIP après extraction
            os.remove(ZIP_FILE)

        # Lister les fichiers téléchargés
        print("📂 Fichiers disponibles dans 'data/':")
        for file in os.listdir(DATA_PATH):
            print(f"   - {file}")

    except Exception as e:
        print(f"❌ Erreur lors du téléchargement : {e}")

if __name__ == "__main__":
    download_dataset()
