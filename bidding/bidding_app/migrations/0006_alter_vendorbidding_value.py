# Generated by Django 4.0.1 on 2022-01-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding_app', '0005_rename_servicename_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorbidding',
            name='value',
            field=models.PositiveIntegerField(),
        ),
    ]
