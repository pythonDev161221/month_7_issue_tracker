# Generated by Django 4.0.1 on 2022-01-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_basestr_name_status_name_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.PROTECT, to='webapp.type'),
        ),
    ]
