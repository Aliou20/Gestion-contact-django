# Generated by Django 4.2 on 2023-04-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='archiver',
            field=models.BooleanField(default=False),
        ),
    ]