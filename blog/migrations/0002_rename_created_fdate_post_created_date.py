# Generated by Django 3.2.20 on 2023-08-24 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_fdate',
            new_name='created_date',
        ),
    ]
