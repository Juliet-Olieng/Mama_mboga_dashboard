# Generated by Django 3.2.12 on 2023-07-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_order_shippings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Shippings',
        ),
    ]
