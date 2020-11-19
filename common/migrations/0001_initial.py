# Generated by Django 3.0.3 on 2020-11-18 11:10

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_string', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.BigIntegerField(blank=True, null=True)),
                ('updated_by', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 18, 16, 40, 26, 892178), null=True)),
                ('updated_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 18, 16, 40, 26, 892178), null=True)),
            ],
        ),
    ]
