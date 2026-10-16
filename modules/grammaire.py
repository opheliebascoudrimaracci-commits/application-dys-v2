# Module extrait de l’application originale.
_CODE = compile('afficher_page_grammaire(interroger_ia)\n', __file__, "exec")

def render(context):
    exec(_CODE, context)
