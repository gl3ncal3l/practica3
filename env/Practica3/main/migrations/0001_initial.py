# Generated by Django 2.0.4 on 2018-04-16 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('no_cuenta', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.FloatField(default=1000.0)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('cod_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(default=datetime.datetime.now)),
                ('monto', models.FloatField()),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'transaccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(default=datetime.datetime.now)),
                ('monto', models.FloatField()),
            ],
            options={
                'db_table': 'transferencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]