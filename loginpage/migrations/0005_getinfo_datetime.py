# Generated by Django 3.1.1 on 2021-01-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0004_auto_20210111_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='getinfo',
            name='datetime',
            field=models.CharField(default='', editable=False, max_length=30),
        ),
    ]