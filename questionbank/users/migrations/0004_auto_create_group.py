from django.db import migrations

from ..constants import ADMIN, COORDINATOR, LECTURER


def forward_func(apps, shema_editor=None):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name=ADMIN),
        Group(name=COORDINATOR),
        Group(name=LECTURER),
    ])

def reverse_func(apps, schema_editor=None):
    Group = apps.get_model('auth', 'Group')
    Group.objects.using(db_alias).filter(name='Admin').delete()
    Group.objects.using(db_alias).filter(name='Coordinator').delete()
    Group.objects.using(db_alias).filter(name='Lecturer').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_make_email_unique'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]
