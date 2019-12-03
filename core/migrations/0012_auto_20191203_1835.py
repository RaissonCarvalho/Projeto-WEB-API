# Generated by Django 2.2.7 on 2019-12-03 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191203_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reciver_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reciver_messages', to='core.Profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to='core.Profile'),
        ),
    ]
