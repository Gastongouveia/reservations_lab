# Generated by Django 5.1.4 on 2024-12-16 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lab',
            old_name='resouces',
            new_name='resources',
        ),
    ]