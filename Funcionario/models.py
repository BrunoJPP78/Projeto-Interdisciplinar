from django.db import models
from Empresa.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    cargo = models.CharField(max_length= 50)
    empresa = models.ForeignKey(Empresa, related_name='funcionarios', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class AtribuicaoFuncionario(models.Model):
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pix = models.CharField(max_length=50, null=True, blank=True)
    chave_pix = models.CharField(max_length=255, null=True, blank=True)
    banco = models.CharField(max_length=100, null=True, blank=True)
    operacao = models.CharField(max_length=50, null=True, blank=True)
    agencia = models.CharField(max_length=50, null=True, blank=True)
    conta = models.CharField(max_length=50, null=True, blank=True)
    
    funcionario = models.OneToOneField('Funcionario', related_name='atribuicao', on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo


class ContatoFuncionario(models.Model):
    TIPOS_CHOICES = (
        ('telefone', 'Telefone'),
        ('email', 'E-mail'),
    )
    tipo = models.CharField(max_length=10, choices=TIPOS_CHOICES)
    valor = models.CharField(max_length=100)
    funcionario = models.ForeignKey('Funcionario', related_name='contatos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}: {self.valor}"

class EnderecoFuncionario(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    funcionario = models.ForeignKey('Funcionario', related_name='enderecos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.municipio}, {self.estado}"
