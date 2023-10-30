# Generated by Django 4.2.4 on 2023-10-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18)),
                ('inscricao_estadual', models.CharField(max_length=30)),
                ('inscricao_municipal', models.CharField(max_length=30)),
            ],
        ),
    ]