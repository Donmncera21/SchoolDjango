# Generated by Django 3.1.2 on 2020-11-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_student_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_profile',
            name='allergies',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
