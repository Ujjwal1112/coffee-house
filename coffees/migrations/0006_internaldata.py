# Generated by Django 5.0.1 on 2024-01-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0005_alter_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_fee', models.IntegerField()),
                ('tax_percentage', models.IntegerField()),
            ],
        ),
    ]
