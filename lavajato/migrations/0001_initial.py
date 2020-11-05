# Generated by Django 3.1.2 on 2020-10-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('ano', models.IntegerField()),
                ('modelo', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
    ]
