# Generated by Django 3.2.5 on 2021-07-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
