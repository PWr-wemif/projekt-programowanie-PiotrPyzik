# Generated by Django 4.2.7 on 2023-12-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_display', '0007_alter_order_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='units',
            field=models.CharField(choices=[('szt', 'Sztuki'), ('m3', 'M3'), ('mb', 'Mb')], default='m3', max_length=3),
        ),
    ]