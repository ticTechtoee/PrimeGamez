# Generated by Django 3.2.10 on 2021-12-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0005_auto_20211209_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='is_otp_correct',
            field=models.BooleanField(default=True),
        ),
    ]
