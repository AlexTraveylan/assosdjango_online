# Generated by Django 4.1 on 2022-09-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assosparents', '0011_alter_eventdurate_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asso',
            name='logo',
            field=models.ImageField(default='default_profile.png', upload_to=''),
        ),
    ]