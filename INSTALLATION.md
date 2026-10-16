# Application Dys — archive de test réorganisée

Cette archive corrige les chemins des modules qui avaient été envoyés à la racine de GitHub. Les activités sont conservées dans `modules/`, le stockage dans `services/` et `app.py` lance le programme principal.

## Mise en place

**Ne supprimez pas le dépôt existant.** Créez un nouveau dépôt de test et envoyez les fichiers en conservant les dossiers `modules/` et `services/`. Sur Streamlit, choisir `app.py`. Les anciens fichiers restés à la racine du dépôt de test ne sont pas nécessaires, mais peuvent y rester pendant les essais.

## Limites importantes

La compilation Python a été vérifiée, pas l’exécution complète sur Streamlit Cloud. Les modules utilisent encore les fonctions partagées de `application_mathis.py`. Les profils stockés dans le navigateur n’ont pas été testés pour la persistance, et peuvent être effacés avec les données du navigateur. Ne pas saisir de données réelles d’enfants avant vérification. Les polices Luciole et OpenDyslexic exigent des fichiers de police sous licence appropriée dans `fonts/`; ils ne sont pas fournis.
