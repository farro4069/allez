# Generated by Django 2.1.4 on 2019-09-24 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='rider',
        ),
    ]
