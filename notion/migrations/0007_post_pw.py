# Generated by Django 3.1.3 on 2020-11-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0006_auto_20201122_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pw',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
