from site_app.models import CarregaDados
from datetime import datetime

dados = CarregaDados()


def inject_variables(request):
    return {
        'header_title': "<strong>NOME</strong> Research Group",
        'footer_contact': dados.contato,
        'now': datetime.utcnow()
    }
