# Generated by Django 5.2.1 on 2025-06-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='token_confirmacao',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
