# Generated by Django 2.2.1 on 2019-06-17 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190519_1441'),
        ('questions', '0004_auto_20190605_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Specialty'),
        ),
    ]
