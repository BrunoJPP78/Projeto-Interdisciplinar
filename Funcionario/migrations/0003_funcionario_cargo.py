# Generated by Django 4.2.4 on 2023-10-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0002_funcionario_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(default='Pintor', max_length=50),
            preserve_default=False,
        ),
    ]
