# Generated by Django 4.0.1 on 2022-01-31 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0035_rename_projects_issue_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
