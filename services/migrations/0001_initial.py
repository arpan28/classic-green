# Generated by Django 2.2.8 on 2020-04-26 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('ScintificName', models.CharField(blank=True, max_length=30, null=True)),
                ('Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Height', models.FloatField(blank=True, max_length=1000, null=True)),
                ('Girth', models.FloatField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Variant', models.CharField(max_length=20)),
                ('VarientStockCount', models.IntegerField(max_length=10)),
                ('VarientItemImage', models.ImageField(null=True, upload_to='')),
                ('VarientItemPrice', models.FloatField(blank=True, max_length=30, null=True)),
                ('VarientItemDiscount', models.FloatField(blank=True, max_length=30, null=True)),
                ('VarientItemName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='services.Item')),
            ],
            options={
                'verbose_name_plural': 'Variants',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerName', models.CharField(max_length=100)),
                ('offerDescription', models.CharField(max_length=1000)),
                ('offerImage', models.ImageField(upload_to='offerImg')),
                ('offerDiscount', models.CharField(blank=True, max_length=15, null=True)),
                ('showOnCarousel', models.BooleanField(default=False)),
                ('liv', models.CharField(max_length=100)),
                ('offerItem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='services.Item')),
                ('offerItemCategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='services.ItemCat')),
                ('offerVarient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='services.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='services.ItemCat'),
        ),
    ]
