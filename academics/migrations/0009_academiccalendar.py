# Generated by Django 5.2 on 2025-05-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0008_mission'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='academic_calendars/')),
            ],
        ),
    ]
