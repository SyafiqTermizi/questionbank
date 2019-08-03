# Generated by Django 2.2.1 on 2019-07-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='discrimination_index',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Discrimination Index (DI)'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='passing_index',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Passing Index (PI)'),
        ),
    ]