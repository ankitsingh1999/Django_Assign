# Generated by Django 3.2.5 on 2021-07-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_userlogin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='password',
            field=models.IntegerField(),
        ),
    ]
