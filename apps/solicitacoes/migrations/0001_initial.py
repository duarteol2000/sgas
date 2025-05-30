# Generated by Django 5.2.1 on 2025-05-23 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arvores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10)),
                ('tipo_logradouro', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=2)),
                ('motivo', models.TextField()),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_analise', 'Em Análise'), ('atendido', 'Atendido'), ('indeferida', 'Indeferida')], default='pendente', max_length=20)),
                ('parecer_tecnico', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='solicitacoes/')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arvores.especiearvore')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
