# Generated by Django 3.2.6 on 2021-09-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0006_auto_20210902_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Скидка'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Скидка'),
        ),
    ]