# Generated by Django 3.2 on 2022-03-29 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
