# Generated by Django 3.1.5 on 2021-01-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210127_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='status',
            field=models.CharField(choices=[('Invited', 'invited'), ('accepted', 'Accepted')], default='Invited', max_length=20),
        ),
    ]