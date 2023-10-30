from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    inscricao_estadual = models.CharField(max_length=30)
    inscricao_municipal = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    TIPOS_CHOICES = (
        ('fixo', 'Fixo'),
        ('fax', 'Fax'),
        ('celular', 'Celular'),
    )
    tipo = models.CharField(max_length=10, choices=TIPOS_CHOICES)
    valor = models.CharField(max_length=100)
    empresa = models.ForeignKey('Empresa', related_name='contatos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}: {self.valor}"

class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    empresa = models.ForeignKey('Empresa', related_name='enderecos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.municipio}, {self.estado}"

