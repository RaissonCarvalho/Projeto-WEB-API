# Generated by Django 2.2.7 on 2019-11-28 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191128_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descripton',
            new_name='description',
        ),
    ]
