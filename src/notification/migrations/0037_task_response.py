# Generated by Django 3.1.14 on 2022-10-02 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0036_auto_20220731_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='response',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
