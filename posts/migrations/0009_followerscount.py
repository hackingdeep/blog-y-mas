# Generated by Django 4.2 on 2023-04-23 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_alter_comment_options_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siguiendo', to=settings.AUTH_USER_MODEL)),
                ('siguiendo_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]