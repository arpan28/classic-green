# Generated by Django 2.2.8 on 2020-04-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200426_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offerItem',
        ),
        migrations.AddField(
            model_name='offer',
            name='offerItem',
            field=models.ManyToManyField(blank=True, null=True, to='services.Item'),
        ),
    ]
