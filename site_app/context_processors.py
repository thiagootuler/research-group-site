from site_app.models import contato
from datetime import datetime

def inject_variables(request):
    return {
        'header_title': "<strong>NOME</strong> Research Group",
        'footer_contact': contato,
        'now': datetime.utcnow()
    }