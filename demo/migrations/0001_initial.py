# Generated by Django 5.0.6 on 2024-07-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Task name')),
                ('status', models.CharField(choices=[('u', 'Not started yet'), ('o', 'On going'), ('f', 'Finished')], max_length=1, verbose_name='Task status')),
            ],
        ),
    ]