# Generated by Django 3.0.2 on 2020-08-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessionapp', '0004_auto_20200814_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf',
            name='img',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
