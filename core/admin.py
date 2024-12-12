from django.contrib import admin
from core.models import Fornecedor, Produto, Categoria

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 0

class ProdutosCategoriasInline(admin.TabularInline):
    model = Produto.categorias.through
    extra = 0

class FornecedorAdmin(admin.ModelAdmin):
    inlines = [ProdutoInline]
    list_display = ["nome", "cnpj"]
    ordering = ["nome"]

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProdutosCategoriasInline]
    list_display = ["nome"]
    ordering = ["nome"]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "preco", "quantidade", "data_criacao"]
    list_filter = ["data_criacao"]
    search_fields = ["codigo", "nome"]
    ordering = ["-data_criacao"]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)