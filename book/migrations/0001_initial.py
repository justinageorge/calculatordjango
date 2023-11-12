# Generated by Django 4.2.7 on 2023-11-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=200)),
            ],
        ),
    ]
