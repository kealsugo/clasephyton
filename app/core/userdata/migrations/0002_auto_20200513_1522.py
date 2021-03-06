# Generated by Django 2.2.12 on 2020-05-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detaroles',
            options={'verbose_name': 'Roles de usuaio', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='rates',
            options={'verbose_name': 'niveles de usuarios', 'verbose_name_plural': 'niveles de usuarios'},
        ),
        migrations.AddField(
            model_name='datosuser',
            name='AddData',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='ApeUser',
            field=models.CharField(max_length=200, null=True, verbose_name='apellido usuario'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='GenUser',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], default='Otros', max_length=20),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='Modifiat',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='NombUser',
            field=models.CharField(max_length=200, null=True, verbose_name='nombre usuario'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='ProfeUser',
            field=models.CharField(max_length=100, null=True, verbose_name='profesion usuario'),
        ),
    ]
