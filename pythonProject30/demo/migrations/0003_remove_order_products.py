# Generated by Django 5.0.7 on 2024-07-26 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_orderposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
