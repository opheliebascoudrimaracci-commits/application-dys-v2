"""Point d’entrée de l’Application Dys."""
import traceback
import streamlit as st

try:
    import application_mathis  # Initialise les services et affiche le module sélectionné.
except Exception:
    st.error("Impossible de démarrer Application Dys.")
    st.code(traceback.format_exc())
