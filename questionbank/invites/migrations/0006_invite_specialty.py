# Generated by Django 2.2.1 on 2019-05-19 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_specialty'),
        ('invites', '0005_add_created_by_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='specialty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Specialty'),
            preserve_default=False,
        ),
    ]