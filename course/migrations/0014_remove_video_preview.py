# Generated by Django 4.0.5 on 2022-09-27 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_remove_course_certificate_remove_course_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='preview',
        ),
    ]
