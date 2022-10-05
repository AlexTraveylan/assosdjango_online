# Generated by Django 4.1 on 2022-09-29 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assosparents', '0013_ressource_message'),
        ('authentication', '0009_alter_vote_user_voted_alter_vote_user_voteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='RessourceLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('asso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assosparents.asso')),
                ('ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assosparents.ressource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('asso', 'user')},
            },
        ),
        migrations.CreateModel(
            name='MessageVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assosparents.asso')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assosparents.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('asso', 'user')},
            },
        ),
    ]