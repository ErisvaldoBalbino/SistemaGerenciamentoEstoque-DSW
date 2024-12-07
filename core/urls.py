from django.urls import path
from core import views

urlpatterns = [
    path('', views.index),
    path('<int:produto_id>', views.details, name="details")
]
