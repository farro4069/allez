# Generated by Django 2.1.4 on 2019-09-23 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('club', models.CharField(max_length=40)),
                ('license_number', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=10)),
            ],
        ),
    ]
