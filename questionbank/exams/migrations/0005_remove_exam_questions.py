# Generated by Django 2.2.1 on 2019-06-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20190605_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='questions',
        ),
    ]