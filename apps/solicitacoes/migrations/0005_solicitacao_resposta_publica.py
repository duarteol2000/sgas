# Generated by Django 5.2.1 on 2025-06-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0004_solicitacao_protocolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='resposta_publica',
            field=models.TextField(blank=True, null=True, verbose_name='Resposta para o Solicitante'),
        ),
    ]
