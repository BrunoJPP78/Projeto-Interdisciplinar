from rest_framework import serializers, generics
from .models import AtribuicaoFuncionario, ContatoFuncionario, EnderecoFuncionario, Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ContatoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoFuncionario
        fields = ('id', 'tipo', 'valor')

class EnderecoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoFuncionario
        fields = ('id', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'estado')

class AtribuicaoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtribuicaoFuncionario
        fields = ('id', 'cargo', 'salario', 'tipo_pix', 'chave_pix', 'banco', 'operacao', 'agencia', 'conta')

class AtribuicaoFuncionarioCreateView(generics.CreateAPIView):
    queryset = AtribuicaoFuncionario.objects.all()
    serializer_class = AtribuicaoFuncionarioSerializer

class AtribuicaoFuncionarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AtribuicaoFuncionario.objects.all()
    serializer_class = AtribuicaoFuncionarioSerializer
