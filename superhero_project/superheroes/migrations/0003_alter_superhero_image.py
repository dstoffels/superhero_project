# Generated by Django 4.0.1 on 2022-01-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_superhero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.FileField(default='', upload_to='superhero_project/superheroes/images/'),
        ),
    ]