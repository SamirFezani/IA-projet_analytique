import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Définition des chemins
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH", "data/raw")
PROCESSED_DATA_PATH = os.getenv("PROCESSED_DATA_PATH", "data/processed")
PROCESSED_DATA_PATH = os.path.join(os.getcwd(), "data", "processed")
REPORTS_PATH = os.path.join(os.getcwd(), "reports")

# Dataset Kaggle
KAGGLE_DATASET = "retailrocket/ecommerce-dataset"
