# Generated by Django 3.2.10 on 2021-12-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0017_auto_20211214_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='payment_through_app_button_clicked',
            field=models.CharField(default='No', max_length=3),
        ),
    ]
