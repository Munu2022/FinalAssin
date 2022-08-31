# Generated by Django 4.1 on 2022-08-25 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('roll_number', models.IntegerField()),
                ('department', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('semester_num', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departmant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('num_course', models.IntegerField()),
                ('num_teachers', models.IntegerField()),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Details.students')),
            ],
        ),
    ]