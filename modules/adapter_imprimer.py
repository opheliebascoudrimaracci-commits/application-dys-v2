# Module extrait de l’application originale.
_CODE = compile('st.info("Le module Adapter et imprimer est conservé, mais désactivé temporairement pendant la stabilisation.")\n', __file__, "exec")

def render(context):
    exec(_CODE, context)
