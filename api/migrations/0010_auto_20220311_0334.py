# Generated by Django 3.2 on 2022-03-11 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220310_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='enrolled_courses',
            field=models.ManyToManyField(blank=True, related_name='students', through='api.Enrolled_Course', to=settings.AUTH_USER_MODEL),
        ),
    ]
