# Generated by Django 5.0.7 on 2024-07-27 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_remove_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderposition',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='demo.order'),
        ),
    ]
