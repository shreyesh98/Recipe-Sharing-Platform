# Generated by Django 5.0.7 on 2024-09-30 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_fav_view'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fav',
            old_name='view',
            new_name='viewer',
        ),
    ]
