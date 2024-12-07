from django.shortcuts import render, get_object_or_404
from core.models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "core/core-index.html", context)

def details(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    context = {'produto': produto}
    return render(request, "core/core-details.html", context)