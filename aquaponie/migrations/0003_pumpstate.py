# Generated by Django 2.0.4 on 2018-05-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaponie', '0002_waterlevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PumpState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('state', models.BooleanField()),
            ],
        ),
    ]
