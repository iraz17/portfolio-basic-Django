# Generated by Django 5.0.1 on 2024-01-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_technology_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='project_images/'),
        ),
    ]
