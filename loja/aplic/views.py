from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from aplic.models import Celular, Cliente, User
from django.shortcuts import render, get_object_or_404

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['celular'] = Celular.objects.all()
        return context


class ContatoView(TemplateView):
    template_name = 'contato.html'

class CelularesView(TemplateView):
    template_name = 'celulares.html'

class ManutencaoView(TemplateView):
    template_name = 'manutencao.html'

def cadastro (request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        
        username = request.POST.get('username')
        password = request.POST.get('senha')

        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
            return HttpResponse("Já existe usuario com esse cpf")
        
        user = User.objects.create_user(username=username, password=password)
        cliente = Cliente.objects.create(nome=nome, cpf=cpf, user=user)
        cliente.save()

        return redirect("127.0.0.1:8000")


def cliente_login(request):
    if request.method == 'POST':
    
        nome = request.POST.get['username']
        senha = request.POST.get['password']
        

        cliente = authenticate(request, username=nome, password=senha)

        if cliente is not None:         
            login(request, cliente)
            return redirect('http://127.0.0.1:8000')
    
    return render(request, 'login.html')

def detalhes_celular(request, celular_id):
    celular = get_object_or_404(Celular, pk=celular_id)
    return render(request, 'detalhes_celular.html', {'celular': celular})

def celular(request):
    search_term = request.GET.get('search', '')
    print(f"Termo de pesquisa: {search_term}")
    Celular = Celular.objects.filter(nome__icontains=search_term)
    return render(request, 'index', {'celular': celular, 'search_term': search_term})