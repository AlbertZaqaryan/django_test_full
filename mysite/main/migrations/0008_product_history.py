# Generated by Django 4.2 on 2023-04-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='history',
            field=models.TextField(default=1, verbose_name='Product History'),
            preserve_default=False,
        ),
    ]
