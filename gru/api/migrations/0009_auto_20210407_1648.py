# Generated by Django 3.1.7 on 2021-04-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210407_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='extracurricularofferings',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'managed': False, 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ranking',
            options={'managed': False, 'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'managed': False, 'ordering': ['name']},
        ),
    ]
