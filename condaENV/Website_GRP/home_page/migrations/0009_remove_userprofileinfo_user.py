# Generated by Django 3.1.5 on 2021-02-08 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_userprofileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
    ]
