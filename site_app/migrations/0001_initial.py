# Generated by Django 3.2 on 2021-05-01 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apresentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('_autores', models.CharField(max_length=250)),
                ('capa', models.CharField(max_length=100)),
                ('miniatura', models.CharField(max_length=100)),
                ('resumo', models.TextField(max_length=500)),
                ('citacoes', models.CharField(max_length=250)),
                ('qualis', models.FloatField()),
                ('doi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coordenada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_logitude', models.FloatField()),
                ('_latitude', models.FloatField()),
                ('_altitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_logradouro', models.CharField(max_length=100)),
                ('_numero', models.CharField(max_length=10)),
                ('_bairro', models.CharField(max_length=50)),
                ('_cidade', models.CharField(max_length=100)),
                ('_uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=50)),
                ('lattes', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=50)),
                ('resumo', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.TextField(max_length=50)),
                ('instituicao', models.TextField(max_length=100)),
                ('departamento', models.TextField(max_length=100)),
                ('_cep', models.CharField(max_length=8)),
                ('_coordenada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.coordenada')),
                ('_localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_telefone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mapa', models.TextField(max_length=250)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.endereco')),
            ],
        ),
    ]
