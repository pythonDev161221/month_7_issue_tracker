# Generated by Django 4.0.1 on 2022-01-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_alter_issue_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='type',
        ),
    ]
