# Generated by Django 4.2.6 on 2023-10-29 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttgapp', '0013_alter_subject_sem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttgapp.semester'),
        ),
    ]
