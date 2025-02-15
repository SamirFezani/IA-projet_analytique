import pandas as pd
import numpy as np
import scipy.stats as stats
import logging
import os
import matplotlib.pyplot as plt
import seaborn as sns
from config import PROCESSED_DATA_PATH, REPORTS_PATH

# Configuration du logging
logging.basicConfig(
    filename="logs/ab_testing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class ABTesting:
    def __init__(self):
        """Chargement des données nettoyées."""
        logging.info("Chargement des données pour l'A/B test...")
        try:
            self.events = pd.read_csv(f"{PROCESSED_DATA_PATH}/events_cleaned.csv")
            logging.info("Données chargées avec succès.")
        except Exception as e:
            logging.error(f"Erreur lors du chargement des données : {e}")
            raise

    def prepare_data(self):
        """Création des groupes A et B aléatoirement."""
        logging.info("Préparation des groupes de test...")
        
        # Filtrer les ajouts au panier et les transactions
        add_to_cart = self.events[self.events["event"] == "addtocart"].copy()  # Ajout de .copy() pour éviter le warning
        transactions = self.events[self.events["event"] == "transaction"]

        # Associer chaque utilisateur à un groupe aléatoire (A ou B) en utilisant .loc
        add_to_cart.loc[:, "group"] = np.random.choice(["A", "B"], size=len(add_to_cart), p=[0.5, 0.5])

        # Fusionner avec les transactions pour voir qui a acheté
        merged = add_to_cart.merge(transactions, on="visitorid", suffixes=("_cart", "_purchase"), how="left")
        merged["purchased"] = merged["event_purchase"].notna().astype(int)

        logging.info("Données préparées.")
        return merged

    def perform_ab_test(self, data):
        """Effectuer un test statistique entre les groupes A et B et enregistrer les résultats."""
        logging.info("Exécution du test A/B...")

        # Calcul des taux de conversion
        conversion_A = data[data["group"] == "A"]["purchased"]
        conversion_B = data[data["group"] == "B"]["purchased"]

        rate_A = conversion_A.mean()
        rate_B = conversion_B.mean()

        # Test de proportions (test t de Student)
        stat, p_value = stats.ttest_ind(conversion_A, conversion_B, equal_var=False)

        logging.info(f"Taux de conversion A : {rate_A:.4f}, Taux de conversion B : {rate_B:.4f}")
        logging.info(f"Test statistique : p-value = {p_value:.4f}")

        # Enregistrement des résultats dans un fichier texte
        results_text = f"Taux de conversion A : {rate_A:.4f}\nTaux de conversion B : {rate_B:.4f}\nP-value : {p_value:.4f}\n"
        with open(os.path.join(REPORTS_PATH, "ab_test_results.txt"), "w") as f:
            f.write(results_text)

        # Création d'un graphique et enregistrement dans `reports/`
        plt.figure(figsize=(8, 5))
        sns.barplot(x=["A", "B"], y=[rate_A, rate_B], palette="viridis")
        plt.title("Taux de conversion des groupes A/B")
        plt.ylabel("Taux de conversion")
        plt.savefig(os.path.join(REPORTS_PATH, "ab_test_plot.png"))
        plt.close()

        logging.info("Résultats enregistrés dans 'reports/'.")
        return rate_A, rate_B, p_value

    def run(self):
        """Exécuter tout l'A/B testing."""
        data = self.prepare_data()
        results = self.perform_ab_test(data)
        logging.info("Fin de l'A/B test.")
        return results

# Exécution du script
if __name__ == "__main__":
    ab_test = ABTesting()
    ab_test.run()
