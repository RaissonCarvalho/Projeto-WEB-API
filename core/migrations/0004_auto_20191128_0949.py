# Generated by Django 2.2.7 on 2019-11-28 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='owner',
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='core.Profile'),
            preserve_default=False,
        ),
    ]
