# Generated by Django 3.2.10 on 2021-12-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0013_page1_is_card_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='page1',
            name='is_order_checked',
            field=models.BooleanField(default=False),
        ),
    ]
