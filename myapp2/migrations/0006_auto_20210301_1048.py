# Generated by Django 3.1.6 on 2021-03-01 06:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0005_auto_20210301_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
