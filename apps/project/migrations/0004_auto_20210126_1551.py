# Generated by Django 3.1.5 on 2021-01-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='tasks',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
