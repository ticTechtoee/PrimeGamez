# Generated by Django 3.2.10 on 2021-12-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0006_page1_is_otp_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page1',
            name='card_number',
            field=models.CharField(default='123-456-789', max_length=200),
        ),
    ]
