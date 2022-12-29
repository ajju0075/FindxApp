# Generated by Django 4.1.4 on 2022-12-15 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productsmodel')),
            ],
        ),
    ]