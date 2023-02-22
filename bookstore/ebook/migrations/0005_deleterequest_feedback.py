# Generated by Django 4.1.7 on 2023-02-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0004_rbook_alter_tbook_cover_alter_tbook_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deleterequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_request', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]