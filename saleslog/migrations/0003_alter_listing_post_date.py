# Generated by Django 4.0.4 on 2022-04-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleslog', '0002_character_guild_listing_post_date_listing_posted_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
