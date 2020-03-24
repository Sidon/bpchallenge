from django.urls import path

from web.base_django.api import (CadastroClienteView, AtualizarClienteView, CadastroClienteEnderecoView,
                                 AtualizarClienteEnderecoView, ListaClienteView, DetalhesClienteView,
                                 ExcluirClienteView)

__author__ = "Gilson Paulino"
__date__ = "Created by 01/08/18"
__copyright__ = "Copyright 2018"
__email__ = "gilsonbp@gmail.com"

app_name = 'cliente'

urlpatterns = (
    path('lista', ListaClienteView.as_view(), name='lista'),
    path('cadastro', CadastroClienteView.as_view(), name='cadastro'),
    path('atualizar/<uuid:pk>', AtualizarClienteView.as_view(), name='atualizar'),
    path('detalhes/<uuid:pk>', DetalhesClienteView.as_view(), name='detalhes'),
    path('excluir/<uuid:pk>', ExcluirClienteView.as_view(), name='excluir'),
    path('cadastro/endereco', CadastroClienteEnderecoView.as_view(), name='cadastro_endereco'),
    path('atualizar/endereco/<int:pk>', AtualizarClienteEnderecoView.as_view(), name='atualizar_endereco'),
)
