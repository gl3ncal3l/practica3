# Generated by Django 2.2 on 2019-04-18 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cuenta',
            table='CUENTA',
        ),
        migrations.AlterModelTable(
            name='tipo',
            table='TIPO',
        ),
        migrations.AlterModelTable(
            name='transaccion',
            table='TRANSACCION',
        ),
        migrations.AlterModelTable(
            name='transferencia',
            table='TRANSFERENCIA',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='USUARIO',
        ),
    ]