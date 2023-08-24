from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Indice, Concentracao
from datetime import datetime, date
import pytz
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

@csrf_protect
def busca_data(request):
    data = date.today()
    return render(request, 'data_form.html', {'data': data})

def lista_indice(request):
    if request.POST:
        #data vem do formulário como string
        form_date = request.POST.get('data')
        #transformar em datetime
        data = datetime.strptime(form_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
        indices = Indice.objects.filter(data=data.date())
        concentracoes = Concentracao.objects.filter(data=data)
        if indices:
            return render(request, 'indice_data.html', {'indices': indices, 'data': data.date(),'concentracoes': concentracoes})
        else:
            messages.info(request, "Não há dados para data fornecida.")
            return redirect('busca_data')
