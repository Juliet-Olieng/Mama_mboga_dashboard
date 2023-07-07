# Generated by Django 3.2.12 on 2023-07-07 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_remove_order_shippings'),
        ('cart', '0002_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Order.order'),
            preserve_default=False,
        ),
    ]