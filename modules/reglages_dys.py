# Module extrait de l’application originale.
_CODE = compile('afficher_reglages_dys()', __file__, "exec")

def render(context):
    exec(_CODE, context)
