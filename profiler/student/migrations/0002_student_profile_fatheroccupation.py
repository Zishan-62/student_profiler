# Generated by Django 4.0.2 on 2022-03-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_profile',
            name='fatheroccupation',
            field=models.TextField(default='', max_length=50),
        ),
    ]
