# Generated by Django 3.2.12 on 2023-07-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippingServive', models.DateField(auto_created=True)),
                ('shippingLocation', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ShippingMethod', models.CharField(max_length=32)),
                ('handlingTime', models.DurationField()),
                ('transitTime', models.DurationField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
