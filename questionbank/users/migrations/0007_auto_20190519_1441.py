# Generated by Django 2.2.1 on 2019-05-19 14:41

from django.db import migrations

def forward_func(apps, schema_editor=None):
    Specialty = apps.get_model('users', 'Specialty')

    Specialty.objects.bulk_create([
        Specialty(name='Anatomy'),
        Specialty(name='Physiology'),
        Specialty(name='Biochemistry'),
        Specialty(name='Genetic'),
        Specialty(name='Microbiology'),
        Specialty(name='Parasitology'),
        Specialty(name='Haematology'),
        Specialty(name='Immunology'),
        Specialty(name='Pathology'),
        Specialty(name='Pharmacology'),
        Specialty(name='Radiology'),
        Specialty(name='Nutrition'),
        Specialty(name='Community Health'),
        Specialty(name='Medicine'),
        Specialty(name='Paediatric'),
        Specialty(name='Psychiatry'),
        Specialty(name='Family Medicine'),
        Specialty(name='Surgery'),
        Specialty(name='ENT'),
        Specialty(name='Ophthalmology'),
        Specialty(name='O&G'),
        Specialty(name='Orthopaedic'),
        Specialty(name='Anaesthesiology'),
    ])

def reverse_func(apps, schema_editor=None):
    Specialty = apps.get_model('users', 'specialty')

    Specialty.objects.using(db_alias).get(name='Anatomy').delete()
    Specialty.objects.using(db_alias).get(name='Physiology').delete()
    Specialty.objects.using(db_alias).get(name='Biochemistry').delete()
    Specialty.objects.using(db_alias).get(name='Genetic').delete()
    Specialty.objects.using(db_alias).get(name='Microbiology').delete()
    Specialty.objects.using(db_alias).get(name='Parasitology').delete()
    Specialty.objects.using(db_alias).get(name='Haematology').delete()
    Specialty.objects.using(db_alias).get(name='Immunology').delete()
    Specialty.objects.using(db_alias).get(name='Pathology').delete()
    Specialty.objects.using(db_alias).get(name='Pharmacology').delete()
    Specialty.objects.using(db_alias).get(name='Radiology').delete()
    Specialty.objects.using(db_alias).get(name='Nutrition').delete()
    Specialty.objects.using(db_alias).get(name='Community Health').delete()
    Specialty.objects.using(db_alias).get(name='Medicine').delete()
    Specialty.objects.using(db_alias).get(name='Paediatric').delete()
    Specialty.objects.using(db_alias).get(name='Psychiatry').delete()
    Specialty.objects.using(db_alias).get(name='Family Medicine').delete()
    Specialty.objects.using(db_alias).get(name='Surgery').delete()
    Specialty.objects.using(db_alias).get(name='ENT').delete()
    Specialty.objects.using(db_alias).get(name='Ophthalmology').delete()
    Specialty.objects.using(db_alias).get(name='O&G').delete()
    Specialty.objects.using(db_alias).get(name='Orthopaedic').delete()
    Specialty.objects.using(db_alias).get(name='Anaesthesiology').delete()



class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_specialty'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]
