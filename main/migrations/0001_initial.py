# Generated by Django 4.1.5 on 2023-03-24 13:22

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
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=100)),
                ('shorturl', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('custom', models.CharField(max_length=50, null=True)),
                ('visits', models.PositiveIntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
                ('page_url', models.URLField()),
                ('device_type', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('referrer', models.URLField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.url')),
            ],
        ),
    ]