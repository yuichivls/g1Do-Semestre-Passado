# Generated by Django 2.2.7 on 2019-12-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_g2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacoes',
            name='data',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Data e hora: '),
        ),
    ]
