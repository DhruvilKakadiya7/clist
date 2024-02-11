# Generated by Django 4.2.7 on 2024-02-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0138_contest_trial_standings_url'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['end_time', 'id'], name='clist_conte_end_tim_d0f3eb_idx'),
        ),
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['-end_time', '-id'], name='clist_conte_end_tim_3ad98e_idx'),
        ),
    ]
