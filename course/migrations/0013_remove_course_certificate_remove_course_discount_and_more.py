# Generated by Django 4.0.5 on 2022-09-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_author_name_alter_author_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='course',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.BooleanField(default=True),
        ),
    ]