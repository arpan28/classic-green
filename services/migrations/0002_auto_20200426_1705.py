# Generated by Django 2.2.8 on 2020-04-26 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offerItem',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='services.Item'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerItemCategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='services.ItemCat'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerVarient',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='services.Variant'),
        ),
    ]