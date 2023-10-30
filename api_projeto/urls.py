from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from Empresa.views import ContatoListCreateView, ContatoRetrieveUpdateDestroyView, EmpresaListCreateView, EmpresaRetrieveUpdateDestroyView, EnderecoListCreateView, EnderecoRetrieveUpdateDestroyView
from Funcionario.serializers import AtribuicaoFuncionarioCreateView, AtribuicaoFuncionarioRetrieveUpdateDestroyView
from Funcionario.views import ContatoFuncionarioListCreateView, ContatoFuncionarioRetrieveUpdateDestroyView, EnderecoFuncionarioListCreateView, EnderecoFuncionarioRetrieveUpdateDestroyView, FuncionarioListCreateView, FuncionarioRetrieveUpdateDestroyView
from Produto.views import ProdutoListCreateView, ProdutoRetrieveUpdateDestroyView

router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/produtos/', ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('api/v1/produtos/<int:pk>/', ProdutoRetrieveUpdateDestroyView.as_view(), name='produto-detail'),  

    path('api/v1/empresas/', EmpresaListCreateView.as_view(), name='empresa-list-create'),
    path('api/v1/empresas/<int:pk>/', EmpresaRetrieveUpdateDestroyView.as_view(), name='empresa-detail'),
    path('api/v1/contatos/', ContatoListCreateView.as_view(), name='contato-list-create'),
    path('api/v1/contatos/<int:pk>/', ContatoRetrieveUpdateDestroyView.as_view(), name='contato-detail'),
    path('api/v1/enderecos/', EnderecoListCreateView.as_view(), name='endereco-list-create'),
    path('api/v1/enderecos/<int:pk>/', EnderecoRetrieveUpdateDestroyView.as_view(), name='endereco-detail'),

    path('api/v1/funcionarios/', FuncionarioListCreateView.as_view(), name='funcionario-list-create'),
    path('api/v1/funcionarios/<int:pk>/', FuncionarioRetrieveUpdateDestroyView.as_view(), name='funcionario-detail'),
    path('api/v1/contatos/', ContatoFuncionarioListCreateView.as_view(), name='contato-funcionario-list-create'),
    path('api/v1/contatos/<int:pk>/', ContatoFuncionarioRetrieveUpdateDestroyView.as_view(), name='contato-funcionario-detail'),
    path('api/v1/enderecos/', EnderecoFuncionarioListCreateView.as_view(), name='endereco-funcionario-list-create'),
    path('api/v1/enderecos/<int:pk>/', EnderecoFuncionarioRetrieveUpdateDestroyView.as_view(), name='endereco-funcionario-detail'),
    path('api/v1/atribuicao/', AtribuicaoFuncionarioCreateView.as_view(), name='atribuicao-funcionario-create'),
    path('api/v1/atribuicao/<int:pk>/', AtribuicaoFuncionarioRetrieveUpdateDestroyView.as_view(), name='atribuicao-funcionario-detail'),
]
