# Generated by Django 4.1.7 on 2023-04-01 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bit', '0004_rename_amount_customer_balance_customer_bonus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='balance',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='plan',
        ),
    ]
