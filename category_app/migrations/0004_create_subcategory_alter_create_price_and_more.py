# Generated by Django 4.2 on 2023-04-21 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0003_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category_app.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='create',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='create',
            name='product',
            field=models.CharField(max_length=100),
        ),
    ]