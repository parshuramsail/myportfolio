# Generated by Django 4.0 on 2021-12-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_name',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
