from django.contrib import admin
from core.models import Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "preco", "quantidade", "data_criacao"]
    list_filter = ["data_criacao"]
    search_fields = ["codigo", "nome"]
    ordering = ["-data_criacao"]

admin.site.register(Produto, ProdutoAdmin)