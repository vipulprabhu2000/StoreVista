# Generated by Django 4.2.4 on 2024-07-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price_alter_product_sale_price_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
