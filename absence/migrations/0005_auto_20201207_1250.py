# Generated by Django 3.1 on 2020-12-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0004_auto_20201207_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='absence.course'),
        ),
    ]
