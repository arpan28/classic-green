# Generated by Django 2.2.8 on 2020-04-26 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200426_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='liv',
        ),
    ]
