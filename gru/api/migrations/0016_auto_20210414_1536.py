# Generated by Django 3.1.7 on 2021-04-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210414_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferreduni',
            name='preferred_uni_name',
            field=models.TextField(null=True),
        ),
    ]
