# Generated by Django 3.1.1 on 2021-01-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0005_getinfo_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getinfo',
            name='datetime',
            field=models.CharField(max_length=30),
        ),
    ]