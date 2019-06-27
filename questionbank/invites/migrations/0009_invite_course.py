# Generated by Django 2.2.1 on 2019-06-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20190613_1228'),
        ('invites', '0008_auto_20190529_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Subject'),
        ),
    ]