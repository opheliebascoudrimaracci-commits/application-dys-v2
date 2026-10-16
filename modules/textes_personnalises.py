# Module extrait de l’application originale.
_CODE = compile('afficher_textes_personnalises(eleve_actif, niveau_actif)\n', __file__, "exec")

def render(context):
    exec(_CODE, context)
