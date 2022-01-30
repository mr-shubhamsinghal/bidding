# Generated by Django 4.0.1 on 2022-01-30 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bidding_app', '0003_alter_vendorbidding_is_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorbidding',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='vendorbidding', to='bidding_app.servicename'),
        ),
        migrations.AlterField(
            model_name='vendorbidding',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
