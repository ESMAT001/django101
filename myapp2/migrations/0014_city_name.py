# Generated by Django 3.1.6 on 2021-03-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0013_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
