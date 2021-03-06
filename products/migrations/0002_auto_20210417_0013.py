# Generated by Django 3.1.6 on 2021-04-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='district',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('O', 'Organic'), ('V', 'Vegetables'), ('L', 'Laptop')], max_length=2),
        ),
    ]
