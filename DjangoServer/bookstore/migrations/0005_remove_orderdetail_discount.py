# Generated by Django 5.0.8 on 2024-09-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='discount',
        ),
    ]
