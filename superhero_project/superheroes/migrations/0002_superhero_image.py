# Generated by Django 4.0.1 on 2022-01-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]