# Generated by Django 3.1.2 on 2020-11-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
