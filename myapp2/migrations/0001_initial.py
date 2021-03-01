# Generated by Django 3.1.6 on 2021-03-01 04:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='student_images/%Y/%m/')),
            ],
        ),
    ]