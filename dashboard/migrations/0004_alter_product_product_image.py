# Generated by Django 3.2.7 on 2021-10-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_images'),
        ),
    ]
