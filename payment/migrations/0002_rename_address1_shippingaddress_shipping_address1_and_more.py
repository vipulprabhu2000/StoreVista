# Generated by Django 4.2.4 on 2024-07-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='Shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='Shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='Shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='Shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='Shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='Shipping_state',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='Shipping_zipcode',
        ),
    ]