# Generated by Django 4.0.1 on 2022-01-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_alter_issue_type_names_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='type_names',
            field=models.ManyToManyField(related_name='issues', to='webapp.Type'),
        ),
    ]
