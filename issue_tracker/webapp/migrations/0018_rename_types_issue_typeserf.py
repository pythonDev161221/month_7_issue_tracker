# Generated by Django 4.0.1 on 2022-01-16 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_alter_issuetype_type_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='types',
            new_name='typeserf',
        ),
    ]
