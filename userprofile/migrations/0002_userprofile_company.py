# Generated by Django 3.0.2 on 2020-01-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
    ]
