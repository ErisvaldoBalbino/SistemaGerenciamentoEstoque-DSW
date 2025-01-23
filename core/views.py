from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from core.models import Produto, Fornecedor, Categoria
from core.forms import ProdutoForm, FornecedorForm, CategoriaForm

# Create your views here.

def index(request):
    produtos = get_list_or_404(Produto)
    return render(request, 'core/index.html', {'produtos': produtos})

def details(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    categorias = produto.categorias.all()
    context = {
        'produto': produto,
        'categorias': categorias
    }
    return render(request, 'core/details.html', context)

def fornecedores(request):
    fornecedores = get_list_or_404(Fornecedor)
    return render(request, 'core/fornecedores.html', {'fornecedores': fornecedores})

def categorias(request):
    categorias = get_list_or_404(Categoria)
    return render(request, 'core/categorias.html', {'categorias': categorias})

def produtosCategorias(request, categoria_nome):
    categoria = get_object_or_404(Categoria, nome=categoria_nome)
    produtos = Produto.objects.filter(categorias=categoria)
    context = {'produtos': produtos, 'categoria': categoria}
    return render(request, 'core/categorias_produtos.html', context)

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()
    return render(request, 'core/cadastrar_produto.html', {'form': form})

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'core/cadastrar_fornecedor.html', {'form': form})

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
    return render(request, 'core/cadastrar_categoria.html', {'form': form})
  