# Generated by Django 2.2.12 on 2020-05-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20200514_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categproye',
            name='Arquitectura',
            field=models.CharField(max_length=150, null=True, verbose_name='Arquitectura'),
        ),
        migrations.AlterField(
            model_name='categproye',
            name='Lenguaje',
            field=models.CharField(max_length=150, null=True, verbose_name='lenguaje'),
        ),
        migrations.AlterField(
            model_name='categproye',
            name='MotorDB',
            field=models.CharField(max_length=150, null=True, verbose_name='motor BD'),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='NombDoc',
            field=models.CharField(max_length=100, null=True, verbose_name='nombre documento'),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='PathDoc',
            field=models.CharField(max_length=100, null=True, verbose_name='pathdocu'),
        ),
        migrations.AlterField(
            model_name='tipodocu',
            name='NombTipoDoc',
            field=models.CharField(max_length=50, null=True, verbose_name='tipo documento'),
        ),
    ]