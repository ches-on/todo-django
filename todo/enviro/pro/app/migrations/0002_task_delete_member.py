# Generated by Django 5.0.6 on 2024-05-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=250)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
