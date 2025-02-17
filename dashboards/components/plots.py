import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def event_distribution(events):
    """Affiche une distribution des événements."""
    st.subheader("Distribution des Événements")

    # Afficher les colonnes disponibles dans le fichier
    st.write("Colonnes disponibles :", events.columns)

    # Vérifier que la colonne 'event' existe
    if 'event' in events.columns:  # La colonne est 'event' (minuscule)
        # Compter les occurrences de chaque événement
        event_counts = events['event'].value_counts()

        # Graphique de distribution
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=event_counts.index, y=event_counts.values, ax=ax)
        ax.set_title("Répartition des Types d'Événements")
        ax.set_xlabel("Type d'Événement")
        ax.set_ylabel("Nombre d'Événements")
        st.pyplot(fig)
    else:
        # Si la colonne n'existe pas, afficher un message d'erreur
        st.error("La colonne 'event' n'existe pas dans les données.")
