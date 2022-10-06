# Generated by Django 3.2 on 2022-10-06 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_following', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('about_me', models.CharField(blank=True, max_length=140, null=True)),
                ('url_list', models.URLField(blank=True, max_length=140, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('friends', models.ManyToManyField(related_name='folowwed_by', through='account.Friends', to='account.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='friends',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='account.userprofile'),
        ),
        migrations.AddField(
            model_name='friends',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='account.userprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together={('followed', 'follower')},
        ),
    ]
