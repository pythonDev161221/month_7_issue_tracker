# Generated by Django 4.0.1 on 2022-01-16 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_rename_types_issue_typeserf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='typeserf',
            new_name='types',
        ),
    ]