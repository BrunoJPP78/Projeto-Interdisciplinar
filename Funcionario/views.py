from rest_framework import generics
from django.shortcuts import render
from .models import ContatoFuncionario, EnderecoFuncionario, Funcionario
from .serializers import ContatoFuncionarioSerializer, EnderecoFuncionarioSerializer, FuncionarioSerializer

class FuncionarioListCreateView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ContatoFuncionarioListCreateView(generics.ListCreateAPIView):
    queryset = ContatoFuncionario.objects.all()
    serializer_class = ContatoFuncionarioSerializer

class ContatoFuncionarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContatoFuncionario.objects.all()
    serializer_class = ContatoFuncionarioSerializer

class EnderecoFuncionarioListCreateView(generics.ListCreateAPIView):
    queryset = EnderecoFuncionario.objects.all()
    serializer_class = EnderecoFuncionarioSerializer

class EnderecoFuncionarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnderecoFuncionario.objects.all()
    serializer_class = EnderecoFuncionarioSerializer
