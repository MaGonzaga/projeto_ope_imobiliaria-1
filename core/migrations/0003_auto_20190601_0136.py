# Generated by Django 2.2.1 on 2019-06-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190531_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='inquilino',
            field=models.BooleanField(default=False),
        ),
    ]