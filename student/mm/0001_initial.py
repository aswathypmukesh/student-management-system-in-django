# Generated by Django 4.0.2 on 2022-03-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                # ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('img', models.ImageField(upload_to=None)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('standard', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
