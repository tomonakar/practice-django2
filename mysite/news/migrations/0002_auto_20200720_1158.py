# Generated by Django 2.2.5 on 2020-07-20 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
