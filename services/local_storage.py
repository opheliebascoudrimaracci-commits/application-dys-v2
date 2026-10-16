"""Sauvegarde des profils dans le navigateur; aucune base SQLite partagée sur le serveur.
La session Streamlit traite les données en mémoire pendant l'utilisation.
"""
import base64
import sqlite3
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

_component = components.declare_component('dys_browser_storage', path=str(Path(__file__).parent/'browser_storage'/'frontend'))


def prepare_storage():
    """Attend le navigateur AVANT toute création de profil ou lecture de données."""
    if st.session_state.get('_dys_db_loaded'):
        return
    saved = _component(mode='load', key='dys_browser_load', default=None)
    if saved is None:
        st.warning(
            "Le stockage local ne répond pas encore. "
            "Vérifie que le navigateur autorise les données de ce site."
        )
        st.stop()
    if isinstance(saved,str) and saved.startswith('STORAGE_ERROR:'):
        st.error('Le navigateur bloque le stockage local. Activez le stockage pour ce site ou utilisez un autre navigateur.')
        st.stop()
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    if saved:
        try:
            raw = base64.b64decode(saved,validate=True)
            if len(raw)>12_000_000: raise ValueError('sauvegarde trop volumineuse')
            conn.deserialize(raw)
        except Exception:
            st.error('La sauvegarde locale est illisible. Rien n’a été effacé. Contactez le support avant de continuer.')
            st.stop()
    st.session_state['_dys_db_conn'] = conn
    st.session_state['_dys_db_loaded'] = True


def connexion_db():
    return st.session_state['_dys_db_conn']


def exporter_base():
    conn = connexion_db()
    conn.commit()
    return conn.serialize()


def sauvegarder_navigateur():
    """Écrit la base en localStorage du navigateur (pas sur le disque du serveur)."""
    blob = exporter_base()
    _component(mode='save', data=base64.b64encode(blob).decode('ascii'), key='dys_browser_save')


def importer_base(fichier):
    raw = fichier.read()
    if len(raw)>12_000_000 or not raw.startswith(b'SQLite format 3\x00'):
        raise ValueError('Ce fichier ne correspond pas à une sauvegarde Application Dys.')
    conn = sqlite3.connect(':memory:',check_same_thread=False)
    conn.deserialize(raw)
    conn.row_factory=sqlite3.Row
    st.session_state['_dys_db_conn'] = conn
