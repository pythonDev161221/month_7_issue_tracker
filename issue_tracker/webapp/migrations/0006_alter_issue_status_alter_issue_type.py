# Generated by Django 4.0.1 on 2022-01-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_issue_status_alter_issue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.status'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.type'),
        ),
    ]
