# Generated by Django 5.1.6 on 2025-04-16 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prjctapp', '0004_jobvacancy_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prjctapp.jobvacancy')),
                ('recruiter_details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prjctapp.seeker')),
            ],
        ),
    ]
