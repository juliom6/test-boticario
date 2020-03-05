from django.views.generic import TemplateView
from django.http import JsonResponse
from datetime import datetime
from pytz import timezone
import time

class PaginaInicioView(TemplateView):
    template_name = 'inicio.html'

def tempoView(request):
    if request.method == 'GET':
        return JsonResponse({'unixtime': int(time.mktime(datetime.now(timezone('America/Sao_Paulo')).timetuple()))})
