# Generated by Django 2.1.5 on 2019-01-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=250)),
                ('score', models.IntegerField(default=0)),
                ('update_time', models.DateTimeField(verbose_name='time updated')),
            ],
        ),
    ]
