# Generated by Django 3.1.2 on 2020-10-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20190625_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]