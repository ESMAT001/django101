# Generated by Django 3.1.6 on 2021-03-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_students_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='students',
            old_name='created',
            new_name='created_at',
        ),
    ]
