# products/serializers.py
from rest_framework import serializers

from Funcionario.serializers import FuncionarioSerializer
from .models import Contato, Empresa, Endereco

class EmpresaSerializer(serializers.ModelSerializer):
    funcionarios = FuncionarioSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('id', 'tipo', 'valor')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'estado')

