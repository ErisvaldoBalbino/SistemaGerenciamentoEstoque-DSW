from django import forms
from core.models import Produto, Fornecedor, Categoria

class ProdutoForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'descricao', 'preco', 'quantidade', 'fornecedor', 'categorias']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input'}),
            'codigo': forms.TextInput(attrs={'class': 'form-input'}),
            'descricao': forms.TextInput(attrs={'class': 'form-input'}),
            'preco': forms.NumberInput(attrs={'class': 'form-input'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-input'}),
        }


class CategoriaForm(forms.ModelForm):
    produtos = forms.ModelMultipleChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-input'}),
        required=False
    )

    class Meta:
        model = Categoria
        fields = ['nome', 'produtos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input'}),
        }