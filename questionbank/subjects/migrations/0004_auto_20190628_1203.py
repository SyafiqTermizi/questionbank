# Generated by Django 2.2.1 on 2019-06-28 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20190613_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['code'], 'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
    ]