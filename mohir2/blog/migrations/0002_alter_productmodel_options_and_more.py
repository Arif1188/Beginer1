# Generated by Django 5.1.1 on 2024-09-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='company_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
