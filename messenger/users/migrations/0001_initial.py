# Generated by Django 2.2.5 on 2019-10-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nick', models.CharField(max_length=30)),
                ('avatar', models.CharField(max_length=100)),
            ],
        ),
    ]