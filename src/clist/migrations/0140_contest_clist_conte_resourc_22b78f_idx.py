# Generated by Django 4.2.7 on 2024-02-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0139_contest_clist_conte_end_tim_d0f3eb_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['resource', '-end_time', '-id'], name='clist_conte_resourc_22b78f_idx'),
        ),
    ]
