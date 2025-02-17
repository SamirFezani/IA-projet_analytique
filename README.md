# 📊 IA-Projet Analytique - Dashboard E-commerce  

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Présentation  
Ce projet analyse le comportement des utilisateurs sur un **site e-commerce** à l’aide de **Python, Streamlit et Tableau Public**.  

### 🔹 **Objectifs :**  
✅ Nettoyer et analyser les événements (`events_cleaned.csv`)  
✅ Explorer les propriétés des articles (`item_properties_cleaned.csv`)  
✅ Visualiser les insights clés via **Streamlit** et **Tableau Public**  

📌 **Accès rapide aux résultats** :  
- 🔗 **Tableau de bord Tableau Public** : [Voir ici](https://public.tableau.com/app/profile/samir.fezani/vizzes)  
- 🖥️ **Application Streamlit** : À exécuter en local (voir ci-dessous).  
- 📂 **Code source GitHub** : [Lien vers le repo](https://github.com/SamirFezani/IA-projet_analytique)  

---

## 🛠️ Technologies utilisées  
- **Python 3.9+**
- **Pandas, NumPy** (Traitement des données)
- **Matplotlib, Seaborn** (Visualisations)
- **Streamlit** (Dashboard interactif)
- **Tableau Public** (Visualisations avancées)

---

## 📂 Structure du projet  
```plaintext
IA-projet_analytique/
│── dashboards/                     # Interface utilisateur avec Streamlit
│   ├── app.py                      # Application principale
│   ├── config.py                    # Configuration
│   ├── utils.py                     # Fonctions d'aide pour chargement des données
│   ├── components/                   # Modules pour affichage des graphiques
│   │   ├── plots.py                  # Graphiques avec Matplotlib/Seaborn
│   │   ├── tableau_embed.py          # Intégration de Tableau Public
│── data/                            # Données brutes et nettoyées
│   ├── raw/                          # Données originales
│   │   ├── events.csv
│   │   ├── item_properties_part1.csv
│   │   ├── item_properties_part2.csv
│   ├── processed/                     # Données nettoyées
│   │   ├── events_cleaned.csv
│   │   ├── item_properties_cleaned.csv
│── logs/                             # Journaux de traitement des données
│   ├── ab_testing.log
│   ├── eda.log
│   ├── preprocessing.log
│── notebooks/                        # Explorations sous Jupyter Notebook
│── reports/                          # Résultats des tests A/B et visualisations
│   ├── ab_test_plot.png
│   ├── ab_test_results.csv
│   ├── event_distribution.png
│── scripts/                          # Scripts Python pour le traitement des données
│   ├── ab_testing.py
│   ├── download_data.py
│   ├── eda.py
│   ├── preprocessing.py
│── .gitignore                        # Fichiers à ignorer dans Git
│── .env                              # Variables d'environnement
│── main.py                           # Script principal
│── README.md                         # Documentation
