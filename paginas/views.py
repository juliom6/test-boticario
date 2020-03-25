from django.views.generic import TemplateView
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
import time

class PaginaInicioView(TemplateView):
    template_name = 'inicio.html'

def tempoView(request):
    if request.method == 'GET':
        return JsonResponse({'unixtime': int(time.mktime(datetime.now().timetuple()))})

def contatoView(request):
    if request.method == 'GET':
        print(request.GET.get('nome'))
        print(request.GET.get('email'))
        print(request.GET.get('mensagem'))
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        mensagem = request.GET.get('mensagem')
        return HttpResponse('<h2>Obrigado ' + nome.split()[0] + '!!</h2><br /><h3>Recebemos sua requisicao GET.</h3>', content_type='text/html', status=201)

    if request.method == 'POST':
        print(request.POST.get('nome'))
        print(request.POST.get('email'))
        print(request.POST.get('mensagem'))
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        return HttpResponse('<h2>Obrigado ' + nome.split()[0] + '!!</h2><br /><h3>Recebemos sua requisicao POST.</h3>', content_type='text/html', status=201)
