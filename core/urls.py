from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_produto', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar_fornecedor', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('<int:produto_id>', views.details, name='details'),
    path('fornecedores', views.fornecedores, name='fornecedores'),
    path('categorias', views.categorias, name='categorias'),
    path('categorias/<str:categoria_nome>', views.produtosCategorias, name='categorias_produtos'),
]