# Generated by Django 3.2.3 on 2021-08-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employ_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='task_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('deadline', models.CharField(max_length=50)),
            ],
        ),
    ]
