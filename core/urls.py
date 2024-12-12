from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index),
    path('<int:produto_id>', views.details, name='details'),
    path('fornecedores', views.fornecedores, name='fornecedores'),
    path('categorias', views.categorias, name='categorias'),
]