# Generated by Django 4.2.7 on 2023-12-03 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='senha',
        ),
    ]