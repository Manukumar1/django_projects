# Generated by Django 2.2 on 2019-05-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NextDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=100)),
                ('simple_cluster', models.CharField(max_length=100)),
                ('detailed_cluster', models.CharField(max_length=100)),
                ('open_value', models.FloatField(max_length=20)),
                ('high_value', models.FloatField(max_length=20)),
                ('low_value', models.FloatField(max_length=20)),
                ('close_value', models.FloatField(max_length=20)),
                ('oc_d_value', models.FloatField(max_length=20)),
                ('oh_d_value', models.FloatField(max_length=20)),
                ('ol_d_value', models.FloatField(max_length=20)),
                ('co_d1_value', models.FloatField(max_length=20)),
            ],
        ),
    ]
