# Generated by Django 5.1.6 on 2025-03-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prjctapp', '0003_jobvacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobvacancy',
            name='salary',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
