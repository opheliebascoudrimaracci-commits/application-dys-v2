# Contrôles de cette version de travail

Source : archive `application-dys-v2-main (1).zip` transmise le 16 octobre 2026.

## Changements limités et vérifiables
- Message explicite pendant le chargement du stockage navigateur (au lieu d’une alerte suggérant immédiatement une panne).
- Choix CP / CE1 / CE2 transmis au générateur de phrases de grammaire (auparavant toujours niveau 1).
- Conservation de tous les modules, des activités COD/COI et du stockage navigateur.

## Ce qui reste à valider sur Streamlit
- Démarrage réel sur Streamlit Community Cloud et chaque onglet.
- Persistance et restauration des profils dans le navigateur réel.
- Activités COD/COI, IA et PDF avec les secrets configurés.
- Polices Luciole/OpenDyslexic : fichiers absents de cette archive, polices de secours utilisées.

Les modules sont encore couplés à `application_mathis.py`. Une séparation complète nécessite des tests interactifs et sera effectuée progressivement, sans supprimer le moteur existant.

## Contrôle complémentaire
- Importation SQLite durcie : contrôle d'intégrité et vérification des tables attendues avant remplacement des données en mémoire.
- En cas de fichier invalide, la base existante reste intacte.
- Syntaxe de tous les fichiers Python vérifiée par `compileall`.
- **Limite :** tests réels Streamlit/navigateur non effectués dans cet environnement ; ne pas remplacer la version en production avant validation.
