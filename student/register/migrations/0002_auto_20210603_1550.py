# Generated by Django 3.2.4 on 2021-06-03 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='studentname',
            new_name='yourname',
        ),
    ]
