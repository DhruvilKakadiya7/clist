# Generated by Django 4.2.11 on 2024-04-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clist', '0145_resource_has_country_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='merging_contests',
            field=models.ManyToManyField(blank=True, related_name='merged_set', to='clist.contest'),
        ),
    ]
