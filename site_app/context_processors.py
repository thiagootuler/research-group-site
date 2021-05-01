from site_app.models import Contato
from datetime import datetime


def inject_variables(request):
    contato = Contato.objects.all().first()
    return {
        'header_title': "<strong>NOME</strong> Research Group",
        'footer_contact': contato,
        'now': datetime.utcnow()
    }
