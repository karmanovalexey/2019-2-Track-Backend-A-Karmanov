# Generated by Django 2.2.5 on 2019-10-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial=True

    dependencies=[
    ]

    operations=[
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField()),
                ('title', models.CharField(max_length=50)),
                ('last_message', models.CharField(max_length=50)),
            ],
        ),
    ]
