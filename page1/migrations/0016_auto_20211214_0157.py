# Generated by Django 3.2.10 on 2021-12-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0015_auto_20211214_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='is_app_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page1',
            name='is_payment_received_through_app',
            field=models.BooleanField(default=False),
        ),
    ]