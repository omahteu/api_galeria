# Generated by Django 4.2.7 on 2023-12-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fila', '0005_alter_imagem_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='estado',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
