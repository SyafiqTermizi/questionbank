# Generated by Django 3.1.2 on 2020-10-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20201012_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
