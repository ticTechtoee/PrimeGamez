# Generated by Django 3.2.10 on 2021-12-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='page1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.CharField(max_length=200)),
                ('postCode', models.CharField(max_length=200)),
            ],
        ),
    ]
