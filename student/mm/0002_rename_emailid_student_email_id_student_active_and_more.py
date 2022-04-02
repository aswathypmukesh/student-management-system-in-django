# Generated by Django 4.0.2 on 2022-03-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='emailid',
            new_name='email_id',
        ),
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(max_length=100),
        ),
    ]