# components/tableau_embed.py
import streamlit as st

def tableau_dashboard():
    """Affiche un tableau de bord intégré depuis Tableau Public."""
    st.subheader("📊 Tableau de Bord - Analyse des Performances")
    
    # URL du tableau de bord à afficher
    tableau_url = "https://public.tableau.com/views/Analysedesvnements/Analysedesvnements#1"

    # Affichage du tableau
    st.markdown(
        f'<iframe src="{tableau_url}" width="1000" height="800"></iframe>',
        unsafe_allow_html=True
    )
    
    # Lien vers Tableau
    st.markdown(f"[🔗 Ouvrir dans un nouvel onglet]({tableau_url})")
