# Generated by Django 3.2.3 on 2021-05-29 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='pwd',
            new_name='password',
        ),
    ]
