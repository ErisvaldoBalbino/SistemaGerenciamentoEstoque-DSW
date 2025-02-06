#from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from core.models import Produto, Fornecedor, Categoria
from core.forms import ProdutoForm, FornecedorForm, CategoriaForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    model = Produto
    template_name = 'core/index.html'
    context_object_name = 'produtos'
    paginate_by = 5
    page_kwarg = "pagina"

    
class DetailsView(DetailView):
    model = Produto
    template_name = 'core/details.html'
    context_object_name = 'produto'

class FornecedoresView(ListView):
    model = Fornecedor
    template_name = 'core/fornecedores.html'
    context_object_name = 'fornecedores'
    paginate_by = 5
    page_kwarg = "pagina"

class CategoriasView(ListView):
    model = Categoria
    template_name = 'core/categorias.html'
    context_object_name = 'categorias'
    paginate_by = 5
    page_kwarg = "pagina"

class ProdutosCategoriasView(ListView):
    model = Produto
    template_name = 'core/categorias_produtos.html'
    context_object_name = 'produtos'
    paginate_by = 5
    page_kwarg = "pagina"

    def get_queryset(self):
        categoria_nome = self.kwargs['categoria_nome']
        return Produto.objects.filter(categorias__nome=categoria_nome)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.get(nome=self.kwargs['categoria_nome'])
        return context

class CadastrarProdutoView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'core/cadastrar_produto.html'
    success_url = reverse_lazy('index')

class CadastrarFornecedorView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'core/cadastrar_fornecedor.html'
    success_url = reverse_lazy('fornecedores')

class CadastrarCategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'core/cadastrar_categoria.html'
    success_url = reverse_lazy('categorias')

class DeletarProdutoView(DeleteView):
    model = Produto
    template_name = 'core/deletar_produto.html'
    success_url = reverse_lazy('index')

class ResultadosPesquisaView(ListView):
    model = Produto
    template_name = 'core/resultado_pesquisa.html'
    context_object_name = 'resultados'
    paginate_by = 5
    page_kwarg = "pagina"

    def get_queryset(self):
        queryset = Produto.objects.all()
        
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(nome__icontains=query)
        
        try:
            start_value = self.request.GET.get("start_value")
            end_value = self.request.GET.get("end_value")
            
            if start_value:
                queryset = queryset.filter(preco__gte=start_value)
            if end_value:
                queryset = queryset.filter(preco__lte=end_value)
        except (ValueError, TypeError):
            pass
            
        return queryset
        



        