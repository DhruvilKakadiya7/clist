# Generated by Django 4.2.11 on 2024-04-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0122_remove_countryaccount_ranking_cou_resourc_057da3_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_rating_activity',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
    ]
