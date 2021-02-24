# Generated by Django 3.1.5 on 2021-01-31 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_project_project_approval_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.user')),
            ],
        ),
    ]