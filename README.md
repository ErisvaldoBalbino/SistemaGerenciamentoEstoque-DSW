# Sistema de Gerenciamento de Estoque - Django

Este projeto foi desenvolvido como parte da disciplina de Desenvolvimento de Sistemas Web, com foco no aprendizado do framework Django.

## 📝 Sobre o Projeto

O sistema permite a administração de produtos, fornecedores e categorias, aplicando conceitos fundamentais do Django como:

- Models e relacionamentos
- Forms e validação de dados
- Templates
- URLs e roteamento
- Views
- Arquivos estáticos (CSS)

## 🚀 Funcionalidades

- **Produtos**
  - Cadastro de produtos com validações
  - Listagem de produtos
  - Visualização detalhada
  - Exclusão de produtos

- **Fornecedores**
  - Cadastro de fornecedores
  - Listagem de fornecedores

- **Categorias**
  - Cadastro de categorias
  - Associação de produtos a categorias
  - Listagem de categorias

## 🛠️ Instalação e Execução

1. Clone o repositório
```bash
git clone [url-do-repositório]
```

2. Crie um ambiente virtual
```bash
python -m venv venv
```

3. Ative o ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Execute as migrações
```bash
python manage.py migrate
```

6. Inicie o servidor
```bash
python manage.py runserver
```

## 📚 Conceitos Abordados

- **Models**
  - Relacionamentos (ForeignKey, ManyToManyField)
  - Campos personalizados
  - Validações de modelo

- **Forms**
  - ModelForms
  - Validações personalizadas (clean methods)
  - Widgets e atributos HTML

- **Templates**
  - Herança de templates
  - Tags e filtros
  - Arquivos estáticos

- **Views**
  - Class-based Views
  - Function-based Views
  - Manipulação de formulários

## 🎯 Objetivos de Aprendizado

- Compreender a estrutura MVC/MTV do Django
- Implementar CRUD básico
- Trabalhar com formulários e validações
- Entender o sistema de templates
- Praticar boas práticas de desenvolvimento web

## 👨‍🏫 Projeto Acadêmico

Este projeto é parte da disciplina de Desenvolvimento de Sistemas Web e foi desenvolvido com propósitos educacionais.