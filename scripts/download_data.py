import kaggle
import os

# Définir le chemin où les données seront téléchargées
download_path = 'data/'

# Créer le répertoire si il n'existe pas déjà
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Spécifier le nom du dataset Kaggle à télécharger
dataset_name = 'retailrocket/ecommerce-dataset'

# Télécharger les données
print(f"Téléchargement des données depuis Kaggle: {dataset_name} ...")
kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

print(f"Données téléchargées dans le répertoire: {download_path}")