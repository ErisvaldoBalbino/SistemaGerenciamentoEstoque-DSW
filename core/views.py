from django.shortcuts import render, get_object_or_404, get_list_or_404
from core.models import Produto, Fornecedor, Categoria
from django.views.generic.list import ListView

# Create your views here.

def index(request):
    produtos = get_list_or_404(Produto)
    return render(request, 'core/index.html', {'produtos': produtos})

def details(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'core/details.html', {'produto': produto})

def fornecedores(request):
    fornecedores = get_list_or_404(Fornecedor)
    return render(request, 'core/fornecedores.html', {'fornecedores': fornecedores})

def categorias(request):
    categorias = get_list_or_404(Categoria)
    return render(request, 'core/categorias.html', {'categorias': categorias})

def produtosCategorias(request, categoria_nome):
    categoria = Categoria.objects.get(nome=categoria_nome)
    produtos = Produto.objects.filter(categorias=categoria)
    context = {'produtos': produtos, 'categoria': categoria}
    return render(request, 'core/categorias-produtos.html', context)