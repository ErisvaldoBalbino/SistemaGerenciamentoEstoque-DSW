from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastrar_produto', views.CadastrarProdutoView.as_view(), name='cadastrar_produto'),
    path('cadastrar_fornecedor', views.CadastrarFornecedorView.as_view(), name='cadastrar_fornecedor'),
    path('cadastrar_categoria', views.CadastrarCategoriaView.as_view(), name='cadastrar_categoria'),
    path('<int:pk>', views.DetailsView.as_view(), name='details'),
    path('fornecedores', views.FornecedoresView.as_view(), name='fornecedores'),
    path('categorias', views.CategoriasView.as_view(), name='categorias'),
    path('categorias/<str:categoria_nome>', views.ProdutosCategoriasView.as_view(), name='categorias_produtos'),
    path('deletar_produto/<int:pk>', views.DeletarProdutoView.as_view(), name='deletar_produto'),
    path('resultado_pesquisa/', views.ResultadosPesquisaView.as_view(), name='resultado_pesquisa')
]