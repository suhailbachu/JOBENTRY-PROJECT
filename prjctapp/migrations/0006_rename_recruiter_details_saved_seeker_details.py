# Generated by Django 5.1.6 on 2025-04-16 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prjctapp', '0005_saved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saved',
            old_name='recruiter_details',
            new_name='seeker_details',
        ),
    ]
