# Generated by Django 4.0 on 2022-01-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
