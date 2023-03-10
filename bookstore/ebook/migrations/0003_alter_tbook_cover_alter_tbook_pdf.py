# Generated by Django 4.1.7 on 2023-02-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0002_tbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbook',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/tbook/covers'),
        ),
        migrations.AlterField(
            model_name='tbook',
            name='pdf',
            field=models.FileField(upload_to='media/tbook/pdfs'),
        ),
    ]
