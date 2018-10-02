# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-26 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do Carrinho')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalago.Product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do Carrinho',
                'verbose_name_plural': 'Itens do Carrinho',
            },
        ),
    ]
