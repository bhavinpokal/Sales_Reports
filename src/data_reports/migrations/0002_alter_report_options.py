# Generated by Django 4.1.7 on 2023-03-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-created_at',)},
        ),
    ]
