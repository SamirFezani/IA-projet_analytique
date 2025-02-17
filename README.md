# 📊 IA-Projet Analytique - Dashboard E-commerce  

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Présentation  
Ce projet analyse le comportement des utilisateurs sur un **site e-commerce** à l’aide de **Python, Streamlit et Tableau Public**.  

### 🎯 Objectifs :  
✅ Nettoyer et analyser les événements (**events_cleaned.csv**)  
✅ Explorer les propriétés des articles (**item_properties_cleaned.csv**)  
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

## ⚙️ Installation (Windows)  

1. **Créer un environnement virtuel** :  
    ```sh
    python -m venv venv
    ```  
2. **Activer l’environnement virtuel** :  
    ```sh
    venv\Scripts\activate
    ```  
3. **Installer les dépendances** :  
    ```sh
    python -m pip install -r requirements.txt
    ```  
4. **Configurer le fichier `.env`** :  
    Dans le répertoire racine du projet, crée un fichier `.env` et ajoute :  
    ```env
    KAGGLE_USERNAME=remush
    KAGGLE_KEY=57f7efa8636e422fe361ee5fc13431fb
    RAW_DATA_PATH=data/raw
    PROCESSED_DATA_PATH=data/processed
    ```  
5. **Lancer le script principal** :  
    ```sh
    python main.py
    ```  
6. **Lancer l’application Streamlit** :  
    ```sh
    streamlit run dashboards/app.py
    ```  

---

## 📊 Fonctionnalités du Dashboard  
✅ **Vue générale** : Distribution des événements, analyse des comportements d'achat, insights utilisateur.  
🔍 **Tests A/B** : Optimisation des conversions.  
📊 **Tableau Public** : Intégration des visualisations interactives.  

---

## 📦 Dépendances principales (`requirements.txt`)  
```plaintext
contourpy==1.3.1
cycler==0.12.1
fonttools==4.56.0
kiwisolver==1.4.8
matplotlib==3.10.0
numpy==2.2.2
packaging==24.2
pandas==2.2.3
pillow==11.1.0
pyparsing==3.2.1
python-dateutil==2.9.0.post0
pytz==2025.1
six==1.17.0
tzdata==2025.1
streamlit
python-dotenv
```

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
```

---

## 📬 Contact  
**Samir Fezani**  
📧 Email : [samirfezani3@gmail.com](mailto:samirfezani3@gmail.com)  
🔗 GitHub : [github.com/SamirFezani](https://github.com/SamirFezani)  

