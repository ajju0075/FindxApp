# Generated by Django 4.1.4 on 2022-12-16 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_userproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
