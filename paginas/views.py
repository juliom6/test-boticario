from django.views.generic import TemplateView
from django.http import JsonResponse
from datetime import datetime
import time

class PaginaInicioView(TemplateView):
    template_name = 'inicio.html'

def tempoView(request):
    if request.method == 'GET':
        return JsonResponse({'unixtime': int(time.mktime(datetime.now().timetuple()))})

def contatoView(request):
    if request.method == 'GET':
        return JsonResponse({'a' : 'b'}, status=200)
