# Generated by Django 4.2.6 on 2023-10-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Dept_name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Facultyid', models.IntegerField()),
                ('room_no', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Degreeprogram',
            fields=[
                ('Deg_name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttgapp.department')),
            ],
        ),
    ]
