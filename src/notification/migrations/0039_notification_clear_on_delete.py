# Generated by Django 3.1.14 on 2022-10-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0038_auto_20221002_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='clear_on_delete',
            field=models.BooleanField(default=True),
        ),
    ]
