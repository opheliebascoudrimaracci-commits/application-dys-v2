# Application Dys — version corrigée de travail

Lancement : `streamlit run app.py`. Déploiement Streamlit Community Cloud : fichier principal `app.py`.

## Organisation
- `app.py` : point d’entrée.
- `modules/` : un fichier par onglet (certaines fonctions restent dans `application_mathis.py` ; refonte progressive).
- `services/local_storage.py` et `services/browser_storage/` : sauvegarde des profils côté navigateur.
- `atelier_familles.py` : module conservé, option « Adapter et imprimer » masquée.

## Confidentialité des profils
- **Aucune base SQLite partagée n'est écrite sur le serveur** : les données de chaque session sont en mémoire vive, et une copie est conservée dans `localStorage` du navigateur.
- Le code Python Streamlit fonctionne **sur le serveur** : les données sont transmises pendant la session pour les traiter. Cette architecture ne garantit donc **pas** que les données ne quittent jamais l’appareil.
- Les profils sont isolés par navigateur et origine web, pas par mot de passe. Un appareil/navigateur partagé partage aussi les profils.
- Navigation privée, effacement des données du navigateur ou changement de navigateur peuvent faire perdre les profils. Utiliser « Sauvegarder mes profils » régulièrement et « Restaurer une sauvegarde » si besoin.
- Le stockage navigateur a une limite de taille et peut être bloqué selon les réglages du navigateur. **À tester sur l'hébergement réel avant usage avec de vrais élèves.**
- L'IA transmet le contenu des demandes au prestataire d'IA configuré ; ne pas y saisir de données sensibles.

## Polices
Verdana et Arial fonctionnent en tant que polices du navigateur. Luciole et OpenDyslexic nécessitent les fichiers autorisés `fonts/Luciole-Regular.ttf` et `fonts/OpenDyslexic-Regular.otf` ; sans eux, le programme signale une police de secours. Les PDF ReportLab utilisent Helvetica par défaut et ne reprennent pas automatiquement la police de l'écran.

## Avant mise en ligne
Ne pas effacer le dépôt existant. Déployer sur une branche ou une nouvelle application Streamlit de test, vérifier chaque onglet, la persistance des profils après fermeture, la restauration, l'impression, les appels IA et l'absence de page blanche. Les secrets API sont à configurer dans Streamlit Secrets, jamais dans le code.

## Limites
Version corrigée à partir du ZIP enrichi fourni, pas de l'intégralité de l'historique GitHub. Les modules sont encore liés aux fonctions partagées dans `application_mathis.py`. Tests statiques réalisés ; test navigateur/Streamlit Cloud non exécuté.
