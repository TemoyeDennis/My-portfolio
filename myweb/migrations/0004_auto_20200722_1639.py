# Generated by Django 3.0.8 on 2020-07-22 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20200722_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='Services_title',
            new_name='title',
        ),
    ]
