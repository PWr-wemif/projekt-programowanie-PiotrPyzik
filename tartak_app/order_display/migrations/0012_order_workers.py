# Generated by Django 4.2.7 on 2023-12-18 18:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_display', '0011_order_adres'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='workers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]