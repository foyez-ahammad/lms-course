# Generated by Django 4.0.5 on 2022-09-04 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_author_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.level'),
        ),
    ]