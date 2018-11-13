# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-12 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20181001_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.Order', verbose_name='Pedido'),
        ),
    ]
