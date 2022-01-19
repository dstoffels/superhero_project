# Generated by Django 4.0.1 on 2022-01-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=50)),
                ('primary_ability', models.CharField(max_length=50)),
                ('secondary_ability', models.CharField(max_length=50)),
                ('catchphrase', models.CharField(max_length=50)),
            ],
        ),
    ]
