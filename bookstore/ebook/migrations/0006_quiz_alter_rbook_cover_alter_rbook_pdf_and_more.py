# Generated by Django 4.1.7 on 2023-03-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0005_deleterequest_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='rbook',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='ebook/static/ebook/media/rbook/covers'),
        ),
        migrations.AlterField(
            model_name='rbook',
            name='pdf',
            field=models.FileField(upload_to='ebook/static/ebook/media/rbook/pdfs'),
        ),
        migrations.AlterField(
            model_name='tbook',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='ebook/static/ebook/media/tbook/covers'),
        ),
        migrations.AlterField(
            model_name='tbook',
            name='pdf',
            field=models.FileField(upload_to='ebook/static/ebook/media/tbook/pdfs'),
        ),
    ]
