from django.shortcuts import render
from rest_framework import generics
from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# Empresa/views.py
from rest_framework import generics
from .models import Contato, Endereco
from .serializers import ContatoSerializer, EnderecoSerializer

class ContatoListCreateView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class EnderecoListCreateView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


